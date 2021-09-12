import sys

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

from numpy.core.shape_base import block


# function to print
def plotTimeSeries(x, y, scale_factor, title):
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=25))
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()

    ymin, ymax = plt.ylim()
    plt.ylim([ymin, ymax])
    plt.title(title)
    plt.show()


# function to print
def plotTimeSeries2(x, y, y2, scale_factor, title1, title2):
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=25))

    plt.plot(x, y * 1000, label=title1)
    plt.gcf().autofmt_xdate()

    plt.plot(x, y2, label=title2)

    plt.gcf().autofmt_xdate()

    plt.legend()
    plt.show()


def calculateCasesPerDay(finalVal):
    # calculating cases per day
    temp = []

    for i in range(len(finalVal)):
        if len(temp) == 0:
            temp = finalVal[i]

        elif temp[0] == 'cases':
            temp = finalVal[i]

        else:
            tempCases = finalVal[i][1]
            finalVal[i][1] = int(finalVal[i][1]) - int(temp[1])
            finalVal[i][1] = int(finalVal[i][1])
            temp[0] = finalVal[i][0]
            temp[1] = tempCases

    del (finalVal[1])
    return finalVal


def calculateandSort0Value(finalVal):
    # assuming 60 days data can contain minimum 0 cases
    print('\ncalculating 0 value cases')
    c = 0
    for i in range(len(finalVal)):
        if finalVal[i][1] == 0 and i > 60:
            c = c + 1
    print('zero cases =' + str(c))

    # taking avg of (current day - 1) and (current day + 1)
    print('\nsolving 0 values')
    for i in range(len(finalVal)):
        if finalVal[i][1] == 0 and i > 60:
            finalVal[i][1] = (finalVal[i - 1][1] + finalVal[i + 1][1]) / 2

    print('\ncalculating 0 value cases')
    c = 0
    for i in range(len(finalVal)):
        if finalVal[i][1] == 0 and i > 60:
            c = c + 1
    print('zero cases =' + str(c))
    return finalVal


def formatDate(finalVal, formatType):
    for i in range(len(finalVal)):
        if i != 0:
            finalVal[i][0] = datetime.datetime.strptime(finalVal[i][0], formatType).date()

    finalValTimePrint = np.array(finalVal)
    return finalValTimePrint


def formatTemp(finalVal):
    for i in range(len(finalVal)):
        finalVal[i][1] = (finalVal[i][1] - 32) * 5.0 / 9.0
    return finalVal