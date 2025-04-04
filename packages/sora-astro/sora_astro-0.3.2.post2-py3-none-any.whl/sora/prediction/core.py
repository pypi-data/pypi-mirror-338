import warnings

import astropy.constants as const
import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.time import Time

from sora.body import Body
from sora.ephem.meta import BaseEphem
from sora.star import Star
from sora.config.decorators import deprecated_alias

__all__ = ['occ_params', 'prediction']


def occ_params(star, ephem, time, n_recursions=5, max_tdiff=None, reference_center='geocenter'):
    """Calculates the parameters of the occultation, as instant, CA, PA.

    Parameters
    ----------
    star : `sora.Star`
        The coordinate of the star in the same reference frame as the ephemeris.
        It must be a Star object.

    ephem : `sora.Ephem*`
        Object ephemeris. It must be an Ephemeris object.

    time : `astropy.time.Time`
        Time close to occultation epoch to calculate occultation parameters.

    n_recursions : `int`, default=5
        The number of attempts to try obtain prediction parameters in case the
        event is outside the previous range of time.

    max_tdiff : `int`, default=None
        Maximum difference from given time it will attempt to identify the
        occultation, in minutes. If given, 'n_recursions' is ignored.

    reference_center : `str`, `sora.Observer`, `sora.Spacecraft`
            A SORA observer object or a string 'geocenter'.
            The occultation parameters will be calculated in respect
            to this reference as center of projection.

    Returns
    -------
     Oredered list : `list`
        - Instant of CA (Time): Instant of Closest Approach.\n
        - CA (arcsec): Distance of Closest Approach.\n
        - PA (deg): Position Angle at Closest Approach.\n
        - vel (km/s): Velocity of the occultation.\n
        - dist (AU): the object geocentric distance.\n
    """
    from sora.ephem import EphemPlanete
    from sora.observer import Observer, Spacecraft
    from astropy.coordinates import SkyOffsetFrame

    n_recursions = int(n_recursions)
    n_iter = n_recursions
    if type(star) != Star:
        raise ValueError('star must be a Star object')
    if not isinstance(ephem, BaseEphem):
        raise ValueError('ephem must be an Ephemeris object')
    if reference_center != 'geocenter' and not isinstance(reference_center, (Observer, Spacecraft)):
        raise ValueError('reference_center must be "geocenter" or an observer object.')

    time = Time(time)
    pos_star = star.get_position(time=time, observer=reference_center)

    if isinstance(ephem, EphemPlanete):
        ephem.fit_d2_ksi_eta(star=pos_star, verbose=False)

    def calc_min(time0, time_interval, delta_t, n_recursions=5, max_tdiff=None):
        if max_tdiff is not None:
            max_t = u.Quantity(max_tdiff, unit=u.min)
            if np.absolute((time0 - time).sec*u.s) > max_t - time_interval*u.s:
                raise ValueError('Occultation is farther than {} from given time'.format(max_t))
        if n_recursions == 0:
            raise ValueError('Occultation is farther than {} min from given time'.format(n_iter*time_interval/60))
        tt = time0 + np.arange(-time_interval, time_interval, delta_t)*u.s
        pos_ephem = ephem.get_position(time=tt, observer=reference_center)
        _, f, g, = - pos_ephem.transform_to(SkyOffsetFrame(origin=pos_star)).cartesian.xyz.to(u.km).value
        dd = np.sqrt(f*f+g*g)
        min = np.argmin(dd)
        if min < 2:
            return calc_min(time0=tt[0], time_interval=time_interval, delta_t=delta_t,
                            n_recursions=n_recursions-1, max_tdiff=max_tdiff)
        elif min > len(tt) - 2:
            return calc_min(time0=tt[-1], time_interval=time_interval, delta_t=delta_t,
                            n_recursions=n_recursions-1, max_tdiff=max_tdiff)

        return tt[min]

    tmin = calc_min(time0=time, time_interval=900, delta_t=20, n_recursions=4, max_tdiff=max_tdiff)
    tmin = calc_min(time0=tmin, time_interval=20, delta_t=0.5, n_recursions=4, max_tdiff=max_tdiff)
    tmin = calc_min(time0=tmin, time_interval=1, delta_t=0.02, n_recursions=5, max_tdiff=max_tdiff)

    pos_ephem = ephem.get_position(time=tmin, observer=reference_center)
    _, f, g, = - pos_ephem.transform_to(SkyOffsetFrame(origin=pos_star)).cartesian.xyz.to(u.km).value
    dd = np.sqrt(f * f + g * g)
    dist = pos_ephem.distance
    ca = np.arcsin(dd * u.km / dist).to(u.arcsec)
    pa = (np.arctan2(-f, -g) * u.rad).to(u.deg)
    if pa < 0 * u.deg:
        pa = pa + 360 * u.deg

    pos_ephem = ephem.get_position(time=tmin + 1 * u.s, observer=reference_center)
    _, f2, g2, = - pos_ephem.transform_to(SkyOffsetFrame(origin=pos_star)).cartesian.xyz.to(u.km).value
    df = f2 - f
    dg = g2 - g
    vel = np.sqrt(df ** 2 + dg ** 2) / 1
    vel = vel * np.sign(-df) * (u.km / u.s)

    return tmin, ca, pa, vel, dist.to(u.AU)


@deprecated_alias(log='verbose')  # remove this line in v1.0
def prediction(time_beg, time_end, body=None, ephem=None, mag_lim=None, catalogue='gaiadr3', step=60, divs=1, sigma=1,
               radius=None, verbose=True, reference_center='geocenter'):
    """Predicts stellar occultations.

    Parameters
    ----------
    time_beg : `str`, `astropy.time.Time`, required
        Initial time for prediction.

    time_end : `str`, `astropy.time.Time`, required
        Final time for prediction.

    body : `sora.Body`, `str`, default=None
        Object that will occult the stars. It must be a Body object or its name
        to search in the Small Body Database.

    ephem : `sora.Ephem`, default=None
        object ephemeris. It must be an Ephemeris object.
        If using a EphemHorizons object, please use 'divs' to make division
        at most a month, or a timeout error may be raised by the Horizon query.

    mag_lim : `int`, `float`, `dict`, default=None
        Faintest magnitude allowed in the search. If the catalogue has more
        than one band defined in the catalogue object, the magnitude limit can
        be done for a specific band or a set of band. Ex: ``mag_lim={'V': 15}``,
        which will only download stars with V<=15 or ``mag_lim={'V': 15, 'B': 14}``
        which will download stars with V<=15 AND B<=14.

    catalogue : `str`, `VizierCatalogue`
        The catalogue to download data. It can be ``'gaiadr2'``, ``'gaiaedr3'``,
        ``'gaiadr3'``, or a VizierCatalogue object. default='gaiadr3'

    step : `int`, `float`, default=60
        Step, in seconds, of ephem times for search

    divs : `int`, default=1
        Number of regions the ephemeris will be split for better search of
        occultations.

    sigma : `int`, `float`, default=1
        Ephemeris error sigma for search off-Earth.

    radius : `int`, `float`, default=None
        The radius of the body. It is important if not defined in body or ephem.

    verbose : `bool`, default=True
        To show what is being done at the moment.

    reference_center : `str`, `sora.Observer`, `sora.Spacecraft`
        A SORA observer object or a string 'geocenter'.
        The occultation parameters will be calculated in respect
        to this reference as center of projection. If a Spacecraft
        is used, please use smaller step since the search will be based
        on the target size and ephemeris error only.


    Important
    ---------
    When instantiating with "body" and "ephem", the user may call the function
    in 3 ways:

    1 - With "body" and "ephem".

    2 - With only "body". In this case, the "body" parameter must be a Body
    object and have an ephemeris associated (see Body documentation).

    3 - With only "ephem". In this case, the "ephem" parameter must be one of
    the Ephem Classes and have a name (see Ephem documentation) to search
    for the body in the Small Body Database.

    Returns
    -------
     : `sora.prediction.PredictionTable`
        PredictionTable with the occultation params for each event.
    """
    from sora.observer import Observer, Spacecraft
    from sora.star.catalog import allowed_catalogues
    from .table import PredictionTable

    if reference_center != 'geocenter' and not isinstance(reference_center, (Observer, Spacecraft)):
        raise ValueError('reference_center must be "geocenter" or an observer object.')

    # generate ephemeris
    if body is None and ephem is None:
        raise ValueError('"body" and/or "ephem" must be given.')
    if body is not None:
        if not isinstance(body, (str, Body)):
            raise ValueError('"body" must be a string with the name of the object or a Body object')
        if isinstance(body, str):
            body = Body(name=body)
    if ephem is not None:
        if body is not None:
            body.ephem = ephem
            ephem = body.ephem
    else:
        ephem = body.ephem
    time_beg = Time(time_beg)
    time_end = Time(time_end)
    intervals = np.round(np.linspace(0, (time_end-time_beg).sec, divs+1))

    # define catalogue parameters
    catalog = allowed_catalogues.get_default(catalogue)
    kwds = {'columns': 'simple', 'row_limit': 10000000, 'timeout': 600}
    if mag_lim is not None:
        if isinstance(mag_lim, (int, float)):
            if len(catalog.band) == 0:
                warnings.warn(f"Catalogue '{catalog.name}' does not have any band defined.")
            else:
                mag_lim = {next(iter(catalog.band)): mag_lim}
        if isinstance(mag_lim, dict):
            kwds['column_filters'] = {catalog.band[band]: f"<{value}" for band, value in mag_lim.items()
                                      if band in catalog.band}

    # determine suitable divisions for star search
    if radius is None:
        try:
            radius = ephem.radius  # for v1.0, change to body.radius
        except AttributeError:
            radius = 0
            warnings.warn('"radius" not given or found in body or ephem. Considering it to be zero.')
        if np.isnan(radius):
            radius = 0
    radius = u.Quantity(radius, unit=u.km)

    radius_search = radius
    if reference_center == 'geocenter':
        radius_search = radius_search + const.R_earth

    if verbose:
        print('Ephemeris was split in {} parts for better search of stars'.format(divs))

    # makes predictions for each division
    occs = []
    for i in range(divs):
        dt = np.arange(intervals[i], intervals[i+1], step)*u.s
        nt = time_beg + dt
        if verbose:
            print('\nSearching occultations in part {}/{}'.format(i+1, divs))
            print("Generating Ephemeris between {} and {} ...".format(nt.min(), nt.max()))
        ncoord = ephem.get_position(time=nt, observer=reference_center)
        reg = SkyCoord([ncoord.ra.min(), ncoord.ra.max()], [ncoord.dec.min(), ncoord.dec.max()])
        center = reg.spherical.mean()
        mindist = (np.arcsin(radius_search/ncoord.distance).max() +
                   sigma*np.max([ephem.error_ra.value, ephem.error_dec.value])*u.arcsec)
        width = ncoord.ra.max() - ncoord.ra.min() + 2*mindist
        height = ncoord.dec.max() - ncoord.dec.min() + 2*mindist
        pos_search = SkyCoord(center)

        if verbose:
            print('Downloading stars ...')
        catalogue = catalog.search_region(pos_search, width=width, height=height, **kwds)
        if len(catalogue) == 0:
            print('    No star found. The region is too small or VizieR is out.')
            continue
        catalogue = catalogue[0]
        if verbose:
            print('    {} {} stars downloaded'.format(len(catalogue), catalog.name))
            print('Identifying occultations ...')
        cat_data = catalog.parse_catalogue(catalogue)
        stars = SkyCoord(ra=cat_data['ra'], dec=cat_data['dec'], distance=np.ones(len(catalogue))*u.pc,
                         pm_ra_cosdec=cat_data['pmra'], pm_dec=cat_data['pmdec'],
                         obstime=cat_data['epoch'])
        prec_stars = stars.apply_space_motion(new_obstime=((nt[-1]-nt[0])/2+nt[0]))
        idx, d2d, d3d = prec_stars.match_to_catalog_sky(ncoord)

        dist = np.arcsin(radius_search/ncoord[idx].distance) + sigma*np.max([ephem.error_ra.value,
                                                                             ephem.error_dec.value])*u.arcsec \
            + np.sqrt(stars.pm_ra_cosdec**2+stars.pm_dec**2)*(nt[-1]-nt[0])/2
        k = np.where(d2d < dist)[0]
        for ev in k:
            star = Star(code=cat_data['code'][ev], ra=cat_data['ra'][ev], dec=cat_data['dec'][ev], pmra=cat_data['pmra'][ev],
                        pmdec=cat_data['pmdec'][ev], parallax=cat_data['parallax'][ev], rad_vel=cat_data['rad_vel'][ev],
                        epoch=cat_data['epoch'][ev], local=True, nomad=False, verbose=False)
            c = star.get_position(time=nt[idx][ev], observer=reference_center)
            pars = [star.code, SkyCoord(c.ra, c.dec), {band: values[ev].value for band, values in cat_data['band'].items()}]
            try:
                pars = np.hstack((pars, occ_params(star, ephem, nt[idx][ev], reference_center=reference_center)))
                occs.append(pars)
            except:
                pass

    meta = {'name': ephem.name or getattr(body, 'shortname', ''), 'time_beg': time_beg, 'time_end': time_end,
            'maglim': mag_lim, 'max_ca': mindist, 'radius': radius.to(u.km).value,
            'error_ra': ephem.error_ra.to(u.mas).value, 'error_dec': ephem.error_dec.to(u.mas).value,
            'ephem': ephem.meta['kernels'], 'catalogue': catalog.name}
    if not occs:
        print('\nNo stellar occultation was found.')
        return PredictionTable(meta=meta)
    # create astropy table with the params
    occs2 = np.transpose(occs)
    mags = {band: [dic[band] for dic in occs2[2]] for band in occs2[2][0]}
    time = Time(occs2[3])
    obj_pos = SkyCoord([ephem.get_position(time=time, observer=reference_center)])
    t = PredictionTable(
        time=time, coord_star=occs2[1], coord_obj=obj_pos, ca=[i.value for i in occs2[4]],
        pa=[i.value for i in occs2[5]], vel=[i.value for i in occs2[6]], mag=mags,
        dist=[i.value for i in occs2[7]], source=occs2[0], meta=meta)
    if verbose:
        print('\n{} occultations found.'.format(len(t)))
    t.sort('Epoch')
    return t
