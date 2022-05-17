import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dat
import calendar

def plotsForEachDay(data1, day, val1):
    days = data1[data1.day_week == day].reset_index()
    wday1 = days.datetime[a].strftime('%A')
    plt.title('seasonal plot 1: ' + wday1 +'s '+val1)
    days = np.array(days.pivot('HH', 'datetime', val1))
    plt.plot(days)
    plt.show()

def plotMeanForEachDay(data3, day1, val3):
    days = data3[data3.day_week == day1].reset_index()
    wday2 = days.datetime[a].strftime('%A')
    plt.title('seasonal plot 2: ' + wday2 + 's '+val3)
    days = days.pivot('HH', 'datetime', val3)
    days = (days.transpose())
    for i in days.columns:
        session = days[i]
        term = np.linspace(i, i + 1, len(session))
        plt.plot(term, session)
        plt.plot(term, np.full_like(term, session.mean()))
    plt.show()

def weekPlots(data2, val2):
    data2 = ((data2.groupby("datetime").mean()).drop(['HH'], 1)).reset_index()
    wek = 0
    week = []
    for r in range(len(data2.datetime)):
        if data2.day_week[r] == 1:
            wek += 1
        week.append(wek)
    week = pd.DataFrame({'week_no': (np.array(week))})
    data2 = pd.concat([data2, week], 1)
    data2 = np.array(data2.pivot('day_week', 'week_no', val2))
    plt.title('seasonal plot 1, weeks ' + val2)
    plt.plot(list(calendar.day_name), data2)
    plt.savefig('seasonal plot 1, weeks %s.png' % val2, dpi=300)
    plt.show()

def plotMeanWeek(data4, val4):
    data4 = ((data4.groupby("datetime").mean()).drop(['HH'], 1)).reset_index()
    wek = 0
    week = []
    for r in range(len(data4.datetime)):
        if data4.day_week[r] == 1:
            wek += 1
        week.append(wek)
    week = pd.DataFrame({'week_no': (np.array(week))})
    data4 = pd.concat([data4, week], 1)
    data4 = (data4.pivot('day_week', 'week_no', val4))
    data4 = (data4.transpose())
    for i in data4.columns:
        session = data4[i]
        term = np.linspace(i-1, i, len(session))
        plt.plot(term, session)
        plt.plot(term, np.full_like(term, session.mean()))
    plt.title('seasonal plot 2, weeks ' + val4)
    plt.savefig('seasonal plot 2, weeks %s.png' %val4, dpi=300)
    plt.show()

data = pd.read_csv("EPEX.csv", ',', header=None, names=['YYYYMMDD', 'HH', 'zonal_price', 'day_week', 'load_forecast'], usecols=[0,1,2,3,4])

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


plotsForEachDay(df, 2, 'zonal_price')
plotMeanForEachDay(df, 2, 'zonal_price')
plotsForEachDay(df, 7, 'zonal_price')
plotMeanForEachDay(df, 7, 'zonal_price')
plotsForEachDay(df, 2, 'load_forecast')
plotMeanForEachDay(df, 2, 'load_forecast')
plotsForEachDay(df, 7, 'load_forecast')
plotMeanForEachDay(df, 7, 'load_forecast')

weekPlots(df, 'zonal_price')
plotMeanWeek(df, 'zonal_price')
weekPlots(df, 'load_forecast')
plotMeanWeek(df, 'load_forecast')