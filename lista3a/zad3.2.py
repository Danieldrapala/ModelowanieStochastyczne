import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dat

def pdk(data, k):
    points = []
    for n in range(len(data.Sys_p) - k):
        points.append([data.Sys_p[n + k], data.Sys_p[n]])
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1],s=[1 for n in range(len(points[:, 0]))])
    plt.title('Pd,h vs P(d-%i),h' %k)
    plt.xlabel('Pd,h')
    plt.ylabel('P(d-%i),h' %k)
    plt.show()


data = pd.read_csv("NP2018.csv", ',', header=None, names=['YYMMDD', 'HH', 'Sys_p', 'Sys_load'],
                   usecols=[0,1,2,3], dtype={'YYMMDD': int, 'HH': int})

ymdhw = []
d = []
for i in range(len(data.YYMMDD)):
    a = (int(dat.datetime.strptime(str(int(data.YYMMDD[i])), '%Y%m%d').strftime('%Y')))
    b = (int(dat.datetime.strptime(str(int(data.YYMMDD[i])), '%Y%m%d').strftime('%m')))
    c = (int(dat.datetime.strptime(str(int(data.YYMMDD[i])), '%Y%m%d').strftime('%d')))
    ymdhw.append(pd.Timestamp.date(dat.datetime(a, b, c)))
    print(int(ymdhw[i].strftime('%w'))+1)
    d.append(int(ymdhw[i].strftime('%w'))+1)
d = pd.DataFrame({'day_week': np.array(d)})
ymdhw = np.array(ymdhw)
ymdhw = pd.DataFrame({'datetime': ymdhw})
df = pd.concat([ymdhw, data], 1)
df = pd.concat([df, d], 1)


plt.scatter(df.Sys_p, df.Sys_load, s=[1 for n in range(len(df.Sys_p))])
plt.title('Pd,h vs Zd,h')
plt.xlabel('zonal price')
plt.ylabel('system load')
plt.show()


#indeks godzinowy w pliku NP2018 jest 1,2,3,4,...,23,0
dx = df[df['HH'].isin(np.array([6,9,18,22]))].reset_index()
pdk(dx, 1)
pdk(dx, 2)
pdk(dx, 7)