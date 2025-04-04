import urllib.request
import re
import pandas as pd

def read_nima():
    fp = urllib.request.urlopen("http://lesia.obspm.fr/lucky-star/astrom.php")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    finder = re.findall(r'Mtable = .*;', mystr)
    text = finder[0][:-1].replace('null', 'None')
    Mtable = [t.replace('"', '').split(',') for t in text[11:-2].split('],[')]
    labels = ['number', 'name', 'full_name', 'NIMA_version', 'n1', 'n2', 'n3', 'n4', 'n5','n6', 'abs_mag', 'a', 'e', 'I',
              'lon_node', 'arg_per', 'mean_ano', 'epoch', 'err_a', 'err_d', 'n17', 'size']
    df = pd.DataFrame.from_records(Mtable, columns=labels)

    df['link'] = ''
    df['kernel'] = ''
    df['first_obs'] = ''
    df['last_obs'] = ''
    df['abs_mag'] = ''
    df['G_slop'] = ''
    for index, row in df.iterrows():
        df.loc[index, "link"] = 'http://lesia.obspm.fr/lucky-star/obj.php?p={}'.format(row['number'])
        df1 = pd.read_html('http://lesia.obspm.fr/lucky-star/obj.php?p={}'.format(row['number']))
        df.loc[index, 'kernel'] = df1[2][1][2]
        df.loc[index, 'first_obs'] = df1[2][1][3]
        df.loc[index, 'last_obs'] = df1[2][1][4]
        df.loc[index, 'abs_mag'] = df1[0][1][3]
        df.loc[index, 'G_slop'] = df1[0][1][4]

    df = df.drop_duplicates(subset='name')

    return df