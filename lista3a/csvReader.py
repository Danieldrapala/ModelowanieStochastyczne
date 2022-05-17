# import matplotlib.pyplot as plt
# import calendar
# import numpy as np
# import pandas as pd
#
#
# def readEPEXForSpecificDay(k):
#     epex = pd.read_csv('EPEX.csv', header=None)
#     epexOnSpecificDay = epex[epex[3] == k]
#     return epexOnSpecificDay
#
#
# def getValueForEachDay(k, column):
#     dataNotGrupped = readEPEXForSpecificDay(k)
#     price = dataNotGrupped.groupby(0, sort=False)[column].apply(list).tolist()
#     return price
#
#
# def getValueForEachHour(k, column):
#     dataNotGrupped = readEPEXForSpecificDay(k)
#     price = dataNotGrupped.groupby(1, sort=False)[column].apply(list).tolist()
#     return price
#
#
# def drawPricesPlotsForEachDay(k):
#     Os_x = [x for x in range(1, 25)]
#     thursdayList = getValueForEachDay(k, 2)
#     for day in thursdayList:
#         plt.plot(Os_x, day)
#     plt.show()
#
#
# def drawLoadPlotsForEachDay(k):
#     Os_x = [x for x in range(1, 25)]
#     thursdayList = getValueForEachDay(k, 4)
#     for day in thursdayList:
#         plt.plot(Os_x, day)
#     plt.show()
#
#
# def drawLoadPlotsForEachHour(k):
#     thursdayList = getValueForEachHour(k, 4)
#     i = 1
#     for day in thursdayList:
#         plt.plot(np.linspace(i - 0.5, i + 0.5, len(day)), day)
#         i += 1
#     plt.show()
#
#
# def drawPricePlotsForEachHour(k):
#     thursdayList = getValueForEachHour(k, 2)
#     i = 1
#     for day in thursdayList:
#         plt.plot(np.linspace(i - 0.5, i + 0.5, len(day)), day)
#         i += 1
#     plt.show()
#
#
# drawPricesPlotsForEachDay(2)
# drawPricesPlotsForEachDay(7)
# drawPricePlotsForEachHour(2)
# drawPricePlotsForEachHour(7)
#
# drawLoadPlotsForEachDay(2)
# drawLoadPlotsForEachDay(7)
# drawLoadPlotsForEachHour(2)
# drawLoadPlotsForEachHour(7)
#
#
# # Tygodniowe
# def drawPlotForEachDayOfTheWeek():
#     df = pd.read_csv('EPEX.csv', header=None)
#     df = df.groupby(0, sort=False)[[2, 3]].mean()
#     week = df.groupby(3, sort=True)[2].apply(list).tolist()
#     print(df)
#     i = 1
#     for day in week:
#         plt.plot(np.linspace(i - 0.5, i + 0.5, len(day)),
#                  day)
#         i += 1
#     plt.xticks(np.arange(1, 8), calendar.day_name)
#     plt.show()
#
#
# def drawPlotForEachWeek():
#     df = pd.read_csv('EPEX.csv', header=None)
#     df = df.groupby(0, sort=False)[[2, 3]].mean()
#     week = df.groupby(3, sort=True)[2].apply(list).tolist()
#     for day in week:
#         plt.plot(np.linspace(1, 7, len(day)),
#                  day)
#     plt.xticks(np.arange(1, 8), calendar.day_name)
#     plt.show()
#
#
# drawPlotForEachDayOfTheWeek()
# drawPlotForEachWeek()