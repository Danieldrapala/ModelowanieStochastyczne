import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime as dat


data = pd.read_csv("EPEX.csv", ',', header=None, names=['YYYYMMDD', 'HH', 'zon_p', 'day_week','load_forecast'], usecols=[0,1,2,3,4])

def pdk(data, k):
    points = []
    for n in range(len(data.zon_p) - k):
        points.append([data.zon_p[n + k], data.zon_p[n]])
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1], s=[1 for n in range(len(points[:, 0]))])
    plt.title('Pd,h vs P(d-%i),h' %k)
    plt.xlabel('Pd,h')
    plt.ylabel('P(d-%i),h' %k)
    plt.show()

ymdhw = []
for i in range(len(data.YYYYMMDD)):
    a = (int(dat.datetime.strptime(str(int(data.YYYYMMDD[i])), '%Y%m%d').strftime('%Y')))
    b = (int(dat.datetime.strptime(str(int(data.YYYYMMDD[i])), '%Y%m%d').strftime('%m')))
    c = (int(dat.datetime.strptime(str(int(data.YYYYMMDD[i])), '%Y%m%d').strftime('%d')))
    d = (int(data.HH[i]))
    e = (int(data.day_week[i]) - 1)
    ymdhw.append(pd.Timestamp.date(dat.datetime(a, b, c)))
ymdhw = np.array(ymdhw)
ymdhw = pd.DataFrame({'datetime': ymdhw})
df = pd.concat([ymdhw, data], 1)

plt.scatter(df.zon_p, df.load_forecast, s=[1 for n in range(len(df.zon_p))])
plt.title('Pd,h vs Zd,h')
plt.xlabel('zonal price')
plt.ylabel('system load')
plt.show()


dx = df[df['HH'].isin(np.array([6,9,18,22]))].reset_index()
pdk(dx, 1)
pdk(dx, 2)
pdk(dx, 7)
