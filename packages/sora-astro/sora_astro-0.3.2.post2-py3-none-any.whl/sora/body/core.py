import warnings

import astropy.constants as const
import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord, Longitude, Latitude
from astropy.time import Time

from sora.config import input_tests
from .frame import get_archinal_frame
from .meta import BaseBody, PhysicalData
from .utils import search_sbdb, search_satdb, apparent_magnitude

__all__ = ['Body']


class Body(BaseBody):
    """Class that contains and manages the information of the body.

    Attributes
    ----------
    name : `str`, required
        The name of the object. It can be the used `spkid` or `designation
        number` to query the SBDB (Small-Body DataBase). In this case, the name
        is case insensitive.

    database : `str`, optional, default='auto'
        The database to query the object. It can be ``satdb`` for our temporary
        hardcoded satellite database, or ``'sbdb'`` to query on the SBDB. If
        database is set as ``auto`` it will try first with ``satdb``,
        then ``sbdb``. If the user wants to use their own information,
        database must be given as ``None``. In this case, `spkid` parameter
        must be given.

    ephem : `sora.EphemKernel`, `sora.EphemHorizons`, `sora.EphemJPL`, `sora.EphemPlanete`
        An Ephem Class that contains information about the ephemeris. It can be
        "horizons" to automatically defined an EphemHorizons object or a list of
        kernels to automatically define an EphemKernel object.

    orbit_class : `str`
        It defines the Orbital class of the body. It can be ``TNO``,
        ``Satellite``, ``Centaur``, ``comet``, ``asteroid``, ``trojan``, ``neo``,
        and ``planet``. It is important for a better characterization of the
        object. If a different value is given, it will be defined as
        ``unclassified``.

    spkid : `str`, `int`, `float`
        If ``database=None``, the user must give a `spkid` or an `ephem`
        which has the `spkid` parameter.

    shape : `str`, `sora.body.shape.Shape3D`
        It defines the input shape of the body. It can be a body.shape object
        or the path to OBJ file.

    albedo : `float`, `int`
        The albedo of the object.

    H : `float`, `int`
        The absolute magnitude.

    G : `float`, `int`
        The phase slope.

    diameter : `float`, `int`, `astropy.quantity.Quantity`
        The diameter of the object, in km.

    density : `float`, `int`, `astropy.quantity.Quantity`
        The density of the object, in g/cm³.

    GM : `float`, `int`, `astropy.quantity.Quantity`
        The Standard Gravitational Parameter, in km³/s².

    rotation : `float`, `int`, `astropy.quantity.Quantity`
        The Rotation of the object, in hours.

    pole : `str`, `astropy.coordinates.SkyCoord`
        The Pole coordinates of the object. It can be a `SkyCoord object` or a
        string in the format ``'hh mm ss.ss +dd mm ss.ss'``.

    BV : `float`, `int`
        The B-V color.

    UB : `float`, `int`
        The U-B color.

    smass : `str`
        The spectral type in SMASS classification.

    tholen : `str`
        The spectral type in Tholen classification.

    Note
    ----
    The following attributes are are returned from the Small-Body DataBase when
    ``database='sbdb'`` or from our temporary hardcoded Satellite DataBase when
    ``database='satdb'``:

    `orbit_class`, `spkid`, `albedo`, `H`, `G`, `diameter`, `density`, `GM`,
    `rotation`, `pole`, `BV`, `UB`, `smass`, and `tholen`.

    These are physical parameters the user can give to the object. If a query is
    made and user gives a parameter, the parameter given by the user is defined
    in the *Body* object.

    """

    def __init__(self, name, database='auto', **kwargs):

        allowed_kwargs = ["albedo", "H", "G", "diameter", "density", "GM", "rotation", "pole", "BV", "UB", "smass",
                          "orbit_class", "spkid", "tholen", "ephem", "frame", "shape"]
        input_tests.check_kwargs(kwargs, allowed_kwargs=allowed_kwargs)
        self._shared_with = {'ephem': {}, 'occultation': {}}
        if database not in ['auto', 'satdb', 'sbdb', None]:
            raise ValueError(f'{database} is not a valid database argument.')
        if database is None:
            self.__from_local(name=name, spkid=kwargs.get('spkid'))
        if database in ['auto', 'satdb']:
            try:
                self.__from_satdb(name=name)
            except ValueError:
                pass
            else:
                database = 'satdb'
        if database in ['auto', 'sbdb']:
            try:
                self.__from_sbdb(name=name)
            except ValueError:
                pass
            else:
                database = 'sbdb'
        if database == 'auto':
            raise ValueError('Object was not located on satdb or sbdb.')
        # set the physical parameters based on the kwarg name.
        if 'smass' in kwargs:
            self.spectral_type['SMASS']['value'] = kwargs.pop('smass')
        if 'tholen' in kwargs:
            self.spectral_type['Tholen']['value'] = kwargs.pop('tholen')
        for key in kwargs:
            setattr(self, key, kwargs[key])
        try:
            shape = self.shape
        except AttributeError:
            self.shape = self.radius.value
        self._shared_with['ephem']['search_name'] = self._search_name
        self._shared_with['ephem']['id_type'] = self._id_type
        if getattr(self, "frame", None) is None:
            try:
                self.frame = get_archinal_frame(self.spkid)
            except ValueError:
                if not np.isnan(self.pole.ra) and not np.isnan(self.rotation):
                    from .frame import PlanetocentricFrame
                    self.frame = PlanetocentricFrame(epoch='J2000', pole=self.pole, alphap=0, deltap=0, prime_angle=0,
                                                     rotation_velocity=360*u.deg / self.rotation, right_hand=True,
                                                     reference="")
        if 'ephem' not in kwargs:
            self.ephem = 'horizons'

    def __from_sbdb(self, name):
        """Searches the object in the SBDB and defines its physical parameters.

        Parameters
        ----------
        name : `str`
            The `name`, `spkid` or `designation number` of the Small Body.

        """
        sbdb = search_sbdb(name)
        self.meta_sbdb = sbdb
        self.name = sbdb['object']['fullname']
        self.shortname = sbdb['object'].get('shortname', self.name)
        self.orbit_class = sbdb['object']['orbit_class']['name']

        pp = sbdb['phys_par']  # get the physical parameters (pp) of the sbdb

        if 'extent' in pp:
            extent = np.array(pp['extent'].split('x'), dtype=float)/2
            self.shape = extent
        self.albedo = PhysicalData('Albedo', pp.get('albedo'), pp.get('albedo_sig'), pp.get('albedo_ref'), pp.get('albedo_note'))
        self.H = PhysicalData('Absolute Magnitude', pp.get('H'), pp.get('H_sig'), pp.get('H_ref'), pp.get('H_note'), unit=u.mag)
        self.G = PhysicalData('Phase Slope', pp.get('G'), pp.get('G_sig'), pp.get('G_ref'), pp.get('G_note'))
        self.diameter = PhysicalData('Diameter', pp.get('diameter'), pp.get('diameter_sig'), pp.get('diameter_ref'),
                                     pp.get('diameter_note'), unit=u.km)
        self.density = PhysicalData('Density', pp.get('density'), pp.get('density_sig'), pp.get('density_ref'),
                                    pp.get('density_note'), unit=u.g/u.cm**3)
        self.GM = PhysicalData('Standard Gravitational Parameter', pp.get('GM'), pp.get('GM_sig'), pp.get('GM_ref'),
                               pp.get('GM_note'), unit=u.km**3/u.s**2)
        self.rotation = PhysicalData('Rotation', pp.get('rot_per'), pp.get('rot_per_sig'), pp.get('rot_per_ref'),
                                     pp.get('rot_per_note'), unit=u.h)
        self.BV = PhysicalData('B-V color', pp.get('BV'), pp.get('BV_sig'), pp.get('BV_ref'), pp.get('BV_note'))
        self.UB = PhysicalData('U-B color', pp.get('UB'), pp.get('UB_sig'), pp.get('UB_ref'), pp.get('UB_note'))
        if 'pole' in pp:
            delimiters = [",", "|", ";", "/"]
            pole = pp['pole']
            for delimiter in delimiters:
                pole = pole.replace(delimiter, " ")
            if len(pole.split()) == 2:
                self.pole = SkyCoord(pole, unit=('deg', 'deg'))
                # Removed uncertainty due to different SBDB formats.
                # pole_err = pp['pole_sig'].split('/')
                # self.pole.ra.uncertainty = Longitude(pole_err[0], unit=u.deg)
                # self.pole.dec.uncertainty = Latitude(pole_err[0] if len(pole_err) == 1 else pole_err[1], unit=u.deg)
                self.pole.reference = pp['pole_ref'] or ""
                self.pole.notes = pp['pole_note'] or ""
            else:
                self.pole = None
        else:
            self.pole = None
        self.spectral_type = {
            "SMASS": {"value": pp.get('spec_B'), "reference": pp.get('spec_B_ref'), "notes": pp.get('spec_B_note')},
            "Tholen": {"value": pp.get('spec_T'), "reference": pp.get('spec_T_ref'), "notes": pp.get('spec_T_note')}}
        self.spkid = sbdb['object']['spkid']
        self._des_name = sbdb['object']['des']
        self.discovery = "Discovered {} by {} at {}".format(sbdb['discovery'].get('date'), sbdb['discovery'].get('who'),
                                                            sbdb['discovery'].get('location'))

    def __from_satdb(self, name):
        satdb = search_satdb(name)
        self.name = name.capitalize()
        self.shortname = name.capitalize()
        self.orbit_class = satdb['class']

        self.albedo = PhysicalData('Albedo', *satdb.get('albedo', [None, None, None]))
        self.H = PhysicalData('Absolute Magnitude', *satdb.get('H', [None, None, None]), unit=u.mag)
        self.G = PhysicalData('Phase Slope', *satdb.get('G', [None, None, None]))
        self.diameter = PhysicalData('Diameter', *satdb.get('diameter', [None, None, None]), unit=u.km)
        self.density = PhysicalData('Density', *satdb.get('density', [None, None, None]), unit=u.g / u.cm ** 3)
        self.GM = PhysicalData('Standard Gravitational Parameter', *satdb.get('GM', [None, None, None]),
                               unit=u.km ** 3 / u.s ** 2)
        self.rotation = PhysicalData('Rotation', *satdb.get('rotation', [None, None, None]), unit=u.h)
        if 'pole' in satdb:
            self.pole = SkyCoord(satdb['pole'][0].replace('/', ' '), unit=('deg', 'deg'))
            self.pole.ra.uncertainty = Longitude(satdb['pole'][1].split('/')[0], unit=u.deg)
            self.pole.dec.uncertainty = Latitude(satdb['pole'][1].split('/')[1], unit=u.deg)
            self.pole.reference = satdb['pole'][2] or ""
            self.pole.notes = ""
        else:
            self.pole = None
        self.BV = None
        self.UB = None
        self.spectral_type = {
            "SMASS": {"value": None, "reference": "", "notes": ""},
            "Tholen": {"value": None, "reference": "", "notes": ""}}
        self.spkid = satdb['spkid']
        self._des_name = name
        self.discovery = ""

    def __from_local(self, name, spkid):
        """Defines Body object with default values for mode='local'.
        """
        self.name = name
        self.shortname = name
        self.orbit_class = None
        if not spkid:
            raise ValueError("'spkid' must be given.")
        self.spkid = spkid
        self.albedo = None
        self.H = None
        self.G = None
        self.diameter = None
        self.density = None
        self.GM = None
        self.rotation = None
        self.pole = None
        self.BV = None
        self.UB = None
        self.spectral_type = {"SMASS": {"value": None, "reference": None, "notes": None},
                              "Tholen": {"value": None, "reference": None, "notes": None}}
        self.discovery = ""

    def get_position(self, time, observer='geocenter'):
        """Returns the object position as seen by an observer

        Parameters
        ----------
        time : `str`, `astropy.time.Time`
            Reference time to calculate the object position. It can be a string
            in the ISO format (yyyy-mm-dd hh:mm:ss.s) or an astropy Time object.

        observer : `str`, `sora.Observer`, `sora.Spacecraft`
            IAU code of the observer (must be present in given list of kernels),
            a SORA observer object or a string: ['geocenter', 'barycenter']

        Returns
        -------
        coord : `astropy.coordinates.SkyCoord`
            Astropy SkyCoord object with the object coordinates at the given time.
        """
        return self.ephem.get_position(time=time, observer=observer)

    def get_pole_position_angle(self, time, observer='geocenter'):
        """Returns the pole position angle and the aperture angle relative to
        the geocenter.

        Parameters
        ----------
        time : `str`, `astropy.time.Time`
            Time from which to calculate the position.
            It can be a string in the ISO format (yyyy-mm-dd hh:mm:ss.s) or an astropy Time object.

        observer : `str`, `sora.Observer`, `sora.Spacecraft`
            IAU code of the observer (must be present in given list of kernels),
            a SORA observer object or a string: ['geocenter', 'barycenter']

        Returns
        -------
        position_angle, aperture_angle : `float` array
            Position angle and aperture angle of the object's pole, in degrees.
        """
        time = Time(time)
        pole = self.pole
        if np.isnan(pole.ra):
            raise ValueError("Pole coordinates are not defined")
        obj = self.ephem.get_position(time, observer=observer)
        position_angle = obj.position_angle(pole).rad*u.rad
        aperture_angle = np.arcsin(
            -(np.sin(pole.dec)*np.sin(obj.dec) +
              np.cos(pole.dec)*np.cos(obj.dec)*np.cos(pole.ra-obj.ra))
            )
        return position_angle.to('deg'), aperture_angle.to('deg')

    def apparent_magnitude(self, time, observer='geocenter'):
        """Calculates the object's apparent magnitude.

        Parameters
        ----------
        time :  `str`, `astropy.time.Time`
            Reference time to calculate the object's apparent magnitude.
            It can be a string in the ISO format (yyyy-mm-dd hh:mm:ss.s) or an astropy Time object.

        observer : `str`, `sora.Observer`, `sora.Spacecraft`
            IAU code of the observer (must be present in given list of kernels),
            a SORA observer object or a string: ['geocenter', 'barycenter']

        Returns
        -------
        ap_mag : `float`
            Object apparent magnitude.
        """
        from astroquery.jplhorizons import Horizons

        time = Time(time)

        if np.isnan(self.H) or np.isnan(self.G):
            from sora.observer import Observer, Spacecraft
            warnings.warn('H and/or G is not defined for {}. Searching into JPL Horizons service'.format(self.shortname))
            origins = {'geocenter': '@399', 'barycenter': '@0'}
            location = origins.get(observer)
            if not location and isinstance(observer, str):
                location = observer
            if isinstance(observer, (Observer, Spacecraft)):
                location = f'{getattr(observer, "code", "")}@{getattr(observer, "spkid", "")}'
            if not location:
                raise ValueError("observer must be 'geocenter', 'barycenter' or an observer object.")
            obj = Horizons(id=self._search_name, id_type=self._id_type, location=location, epochs=time.jd)
            eph = obj.ephemerides(extra_precision=True)
            if 'H' in eph.keys():
                self.H = eph['H'][0]
                self.H.reference = "JPL Horizons"
                self.G = eph['G'][0]
                self.G.reference = "JPL Horizons"
            if len(eph['V']) == 1:
                return eph['V'][0]
            else:
                return eph['V'].tolist()

        else:
            obs_obj = self.ephem.get_position(time, observer=observer)
            sun_obj = self.ephem.get_position(time, observer='10')

            # Calculates the phase angle between the 2-vectors
            unit_vector_1 = -obs_obj.cartesian.xyz / np.linalg.norm(obs_obj.cartesian.xyz)
            unit_vector_2 = -sun_obj.cartesian.xyz / np.linalg.norm(sun_obj.cartesian.xyz)
            dot_product = np.dot(unit_vector_1, unit_vector_2)
            phase = np.arccos(dot_product).to(u.deg).value
            return apparent_magnitude(self.H.value, self.G.value, obs_obj.distance.to(u.AU).value,
                                      sun_obj.distance.to(u.AU).value, phase)

    def to_log(self, namefile):
        """Saves the body log to a file.

        Parameters
        ----------
        namefile : `str`
            Filename to save the log.
        """
        f = open(namefile, 'w')
        f.write(self.__str__())
        f.close()

    def get_orientation(self, time, observer='geocenter'):
        """Returns the object orientation as seen by an observer.

        Parameters
        ----------
        time : `str`, `astropy.time.Time`
            Epoch of observation to calculate the object orientation. It can be a string
            in the ISO format (yyyy-mm-dd hh:mm:ss.s) or an astropy Time object.

        observer : `str`, `sora.Observer`, `sora.Spacecraft`
            IAU code of the observer (must be present in given list of kernels),
            a SORA observer object or a string: ['geocenter', 'barycenter']
            to compute ephemeris.

        Returns
        -------
        orientation : `dict`
            A dictionary with the following orientation parameters:
            - `sub_observer`: `str`
                the longitude and latitude of the body in the direction of the observer.
            - `sub_solar` : `str`
                The sub-solar coordinate.
            - `pole_position_angle` : `astropy.coordinates.Angle`
                Apparent position angle of the pole.
            - `pole_aperture_angle` : `astropy.coordinates.Angle`
                Apparent aperture angle of the pole.
        """
        time = Time(time)
        pos = self.ephem.get_position(time=time, observer=observer)
        orientation = {}
        try:
            epoch = time - pos.spherical.distance / const.c
            frame = self.frame.frame_at(epoch=epoch)
            pole = frame.pole
            subobs = SkyCoord(-pos.cartesian).transform_to(frame=frame)
            orientation['sub_observer'] = subobs.to_string('decimal')
            # TODO(subsun is technically wrong. We must correct to an observer on the body.)
            pos_sun = self.ephem.get_position(time=time, observer='10')
            subsun = SkyCoord(-pos_sun.cartesian).transform_to(frame=frame)
            orientation['sub_solar'] = subsun.to_string('decimal')
        except AttributeError:
            warnings.warn('Frame attribute is not defined')
            pole = self.pole
        if not np.isnan(pole.ra):
            position_angle = pos.position_angle(pole).rad * u.rad
            aperture_angle = np.arcsin(
                -(np.sin(pole.dec) * np.sin(pos.dec) +
                  np.cos(pole.dec) * np.cos(pos.dec) * np.cos(pole.ra - pos.ra))
            )
            orientation['pole_position_angle'] = position_angle.to('deg')
            orientation['pole_aperture_angle'] = aperture_angle.to('deg')
        else:
            warnings.warn("Pole coordinates are not defined")
        return orientation

    def plot(self, time=None, observer='geocenter', center_f=0, center_g=0, contour=False, ax=None, plot_pole=True, **kwargs):
        """Plots the body shape as viewed by observer at some time given the body orientation.
        If the user wants to dictate the orientation, please use `shape.plot()` instead.

        Parameters
        ----------
        time :  `str`, `astropy.time.Time`
            Reference time to calculate the object's apparent magnitude.
            It can be a string in the ISO format (yyyy-mm-dd hh:mm:ss.s) or an astropy Time object.
            It must be only one value.

        observer : `str`, `sora.Observer`, `sora.Spacecraft`
            IAU code of the observer (must be present in given list of kernels),
            a SORA observer object or a string: ['geocenter', 'barycenter']

        center_f : `int`, `float`
            Offset of the center of the body in the East direction, in km

        center_g  : `int`, `float`
            Offset of the center of the body in the North direction, in km

        radial_offset : `int`, `float`
            Offset of the center of the body in the direction of observation, in km

        ax : `matplotlib.pyplot.Axes`
            The axes where to make the plot. If None, it will use the default axes.

        contour : `bool`
            If True, it plots the limb of the projected shape.
            If False, it plots the 3D shape. Default: False.

        plot_pole : `bool`
            If True, the direction of the pole is plotted.
            Ignored if `contour=True`
        """
        if not hasattr(self, 'shape'):
            raise ValueError('{} does not have a shape or size to be plotted'.format(self.__class__.__name__))
        if time is None or getattr(self, 'frame', None) is None:
            warnings.warn('No time is giving or frame is not defined. Plotting without computing orientation. '
                          'To provide orientation, please plot from shape directly.')
            orientation = {}
        else:
            time = Time(time)
            if not time.isscalar and len(time) > 1:
                raise ValueError('time keyword must refer to only one instant')
            orientation = self.get_orientation(time=time, observer=observer)
            orientation.pop('pole_aperture_angle')
        if 'pole_aperture_angle' in kwargs:
            kwargs.pop('pole_aperture_angle')
        if contour:
            orientation.pop('sub_solar')
            self.shape.get_limb(**orientation).plot(center_f=center_f, center_g=center_g, ax=ax, **kwargs)
        else:
            self.shape.plot(**orientation, center_f=center_f, center_g=center_g, ax=ax, plot_pole=plot_pole, **kwargs)

    def __str__(self):
        from .values import smass, tholen
        out = ['#' * 79 + '\n{:^79s}\n'.format(self.name) + '#' * 79 + '\n',
               'Object Orbital Class: {}\n'.format(self.orbit_class)]
        if self.spectral_type['Tholen']['value'] or self.spectral_type['SMASS']['value']:
            out += 'Spectral Type:\n'
            value = self.spectral_type['SMASS']['value']
            if value:
                out.append('    SMASS: {}  [Reference: {}]\n'.format(value, self.spectral_type['SMASS']['reference']))
            value = self.spectral_type['Tholen']['value']
            if value:
                out.append('    Tholen: {} [Reference: {}]\n'.format(value, self.spectral_type['Tholen']['reference']))
            out += " "*7 + (smass.get(self.spectral_type['SMASS']['value']) or
                            tholen.get(self.spectral_type['Tholen']['value']) or '') + "\n"
        out.append(self.discovery)

        out.append('\n\nPhysical parameters:\n')
        out.append(self.diameter.__str__())
        out.append(self.mass.__str__())
        out.append(self.density.__str__())
        out.append(self.rotation.__str__())
        if not np.isnan(self.pole.ra):
            out.append('Pole\n    RA:{} +/- {}\n    DEC:{} +/- {}\n    Reference: {}, {}\n'.format(
                       self.pole.ra.__str__(), self.pole.ra.uncertainty.__str__(), self.pole.dec.__str__(),
                       self.pole.dec.uncertainty.__str__(), self.pole.reference, self.pole.notes))
        out.append(self.H.__str__())
        out.append(self.G.__str__())
        out.append(self.albedo.__str__())
        out.append(self.BV.__str__())
        out.append(self.UB.__str__())
        if hasattr(self, 'frame'):
            out.append('\n' + self.frame.__str__() + '\n')
        if hasattr(self, 'shape'):
            out.append('\n' + self.shape.__str__() + '\n')
        if hasattr(self, 'ephem'):
            out.append('\n' + self.ephem.__str__() + '\n')
        return ''.join(out)
