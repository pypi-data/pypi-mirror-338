import urllib.request
from astropy.io import votable
import io
import pandas as pd
from astropy.time import Time

def get_asteroid_systems():
    result = urllib.request.urlopen("https://ssp.imcce.fr/webservices/miriade/api/ephemsys.php?-get=systems&-from=MiriadeDoc")
    mybytes = result.read()
    mystr = mybytes.decode("utf8")
    dados = [[l1.strip() for l1 in l.split(',')] for l in mystr.strip().split('\n')]
    df = pd.DataFrame.from_records(dados[1:], columns=dados[0])
    return df

def get_gensol_info(name):
    result = urllib.request.urlopen("https://ssp.imcce.fr/webservices/miriade/api/ephemsys.php?-get=gensol&-name={}&-from=MiriadeDoc".format(name))
    mybytes = result.read()
    mystr = mybytes.decode("utf8")
    dados = [[l1.strip() for l1 in l.split(',')] for l in mystr.strip().split('\n')]
    df = pd.DataFrame.from_records(dados[1:], columns=dados[0])
    return df

def get_ephemeris_from_miriade(name, epoch='now', ndb=5, step='1d', gensol=1):
    if ndb > 5000:
        raise ValueError('ndb must be less than 5000')
    tscale = 'TT'
    if type(epoch) is Time:
        tscale = epoch.scale.upper()
        epoch = epoch.jd
    data_sat = {"name": f"a:{name}", # The designation of the target
                "ep": "{}".format(epoch), # Requested epoch, expressed in Julian period, ISO format, or formatted as any English textual datetime
                "nbd": "{}".format(int(ndb)), # Number of dates of ephemeris to compute (default: 1) 1 ≤ nbd ≤ 5000
                "step": "{}".format(str(step)), # Step of increment (float) followed by one of (d)ays or (h)ours or (m)inutes or (s)econds (default: 1d)
                "tscale": "{}".format(tscale), # Ephemeris time scale (default: UTC)
                "gensol": "{}".format(gensol), # Id of the Genoide's orbital solution of the satellites (Default = 0)  0 | 1 | 2 | ... (4)
                "mime": "votable", # Mime type of the results (default: votable)  votable | html | text | text/csv | json
                "from": "MiriadeDoc", # Word which definite the name of the caller application, or which describes the request, Any short String
                }
    data_format_sat = "&".join([f"-{key}={item}" for key, item in data_sat.items()])
    result = urllib.request.urlopen("https://ssp.imcce.fr/webservices/miriade/api/ephemsys.php?{}".format(data_format_sat))
    mybytes = result.read()
    s = io.BytesIO(mybytes)
    v = votable.parse(s)
    tables = {t.ID: t.to_table(use_names_over_ids=True) for t in v.iter_tables()}
    return tables