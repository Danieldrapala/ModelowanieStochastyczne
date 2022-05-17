import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
import datetime as dat

def dni(data1, day, val1):
    days = data1[data1.day_week == day].reset_index()
    wday1 = days.datetime[a].strftime('%A')
    plt.title('seasonal plot 1: ' + wday1 +'s '+val1)
    days = np.array(days.pivot('HH', 'datetime', val1))
    plt.plot(days)
    plt.savefig('seasonal plot 1- %s s %s' % (wday1, val1), dpi=300)
    plt.show()

def dni2(data3, day1, val3):
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
    plt.savefig('seasonal plot 2- %ss %s' %(wday2, val3), dpi=300)
    plt.show()

def tyg(data2, val2):
    data2 = ((df.groupby("datetime").mean()).drop(['HH'], 1)).reset_index()
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

def tyg2(data4, val4):
    data4 = ((df.groupby("datetime").mean()).drop(['HH'], 1)).reset_index()
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

data = pd.read_csv("NP2018.csv", ',', header=None, names=['YYMD', 'HH', 'Sys_p', 'Sys_Load'],
                   usecols=[0,1,2,3], dtype={'YYMD': int, 'HH': int})

ymdhw = []
d = []
for i in range(len(data.YYMD)):
    a = (int(dat.datetime.strptime(str(int(data.YYMD[i])), '%Y%m%d').strftime('%Y')))
    b = (int(dat.datetime.strptime(str(int(data.YYMD[i])), '%Y%m%d').strftime('%m')))
    c = (int(dat.datetime.strptime(str(int(data.YYMD[i])), '%Y%m%d').strftime('%d')))
    ymdhw.append(pd.Timestamp.date(dat.datetime(a, b, c)))
    d.append(int(ymdhw[i].strftime('%w'))+1)
d = pd.DataFrame({'day_week': np.array(d)})
ymdhw = np.array(ymdhw)
ymdhw = pd.DataFrame({'datetime': ymdhw})
df = pd.concat([ymdhw, data], 1)
df = pd.concat([df, d], 1)



dni(df, 2, 'Sys_p')
dni2(df, 2, 'Sys_p')
dni(df, 7, 'Sys_p')
dni2(df, 7, 'Sys_p')
dni(df, 2, 'Sys_Load')
dni2(df, 2, 'Sys_Load')
dni(df, 7, 'Sys_Load')
dni2(df, 7, 'Sys_Load')

tyg(df, 'Sys_p')
tyg2(df, 'Sys_p')
tyg(df, 'Sys_Load')
tyg2(df, 'Sys_Load')