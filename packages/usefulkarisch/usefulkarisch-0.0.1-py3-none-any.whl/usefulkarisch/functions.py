import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import date as dtDate
import importlib.util
import sys
import os
import re
from typing import Union
from copy import deepcopy
from functools import reduce
from operator import mul
from sklearn.model_selection import train_test_split
from win32com import client
from xlrd import xldate_as_datetime
from blp import blp

from .classes import ArrayWithMaps

from .variables import commodityInfo, weekdays, contractMonthInfo, variablesContractSizes
#from .fastFunctions import *

def loadPricingDataframe(fileAddress):
    df = pd.read_csv(fileAddress, index_col=0)
    df.index = pd.to_datetime(df.index)
    if 'frontNotice' in df.columns:
        df['frontNotice'] = pd.to_datetime(df['frontNotice'])
    if 'lastViableDate' in df.columns:
        df['lastViableDate'] = pd.to_datetime(df['lastViableDate'])
    if 'fnd' in df.columns:
        df['fnd'] = pd.to_datetime(df['fnd'])
    if 'ltd' in df.columns:
        df['ltd'] = pd.to_datetime(df['ltd'])
    if 'lvd' in df.columns:
        df['lvd'] = pd.to_datetime(df['lvd'])
    return df

def today():
    return dt(dtDate.today())

def strContains(pattern, str):
    return re.search(pattern, str) is not None

def downwardDeviation(series):
    downwardReturns = series[series<-0.00000000001]
    if len(downwardReturns) == 0:
        return np.nan
    else:
        annualizedDD = downwardReturns.std(ddof=1) * (252 ** 0.5)
        ddVol = (2 ** 0.5) * annualizedDD
    return ddVol

def cagr(startVal, endVal, startDate, endDate):
    time = (endDate - startDate).days / 365

    return ((endVal / startVal) ** (1 / time)) - 1

def mean(lst):
    return sum(lst) / len(lst)

def parseDateToStrs(date):
    yearStr = str(date.year)
    monthStr = str(date.month) if date.month >= 10 else '0' + str(date.month)
    dayStr = str(date.day) if date.day >= 10 else '0' + str(date.day)

    return yearStr, monthStr, dayStr

def calculatePriorWeekday(date):
    if date.weekday() == 0: #if monday
        return date + timedelta(days=-3)
    elif date.weekday() == 6: #if sunday
        return date + timedelta(days=-2)
    else:
        return date + timedelta(days=-1)

def calculateNextWeekday(date):
    if date.weekday() == 4: #if friday
        return date + timedelta(days=3)
    elif date.weekday() == 5: #if saturday
        return date + timedelta(days=2)
    else:
        return date + timedelta(days=1)

def calculateClosestWeekday(date):
    if date.weekday() == 5: #if saturday
        return date + timedelta(days=-1)
    elif date.weekday() == 6: #if sunday
        return date + timedelta(days=1)
    else:
        return date

def calculatePriorWeekdayIfWeekend(date):
    if date.weekday() == 5 or date.weekday() == 6:
        return calculatePriorWeekday(date)
    else:
        return date

def dt(dateStr):
    return pd.to_datetime(dateStr)

def reverseDict(dictionary):
    return {value: key for key, value in dictionary.items()}

def importByFilepath(filepath, moduleName):
    cwd = os.getcwd()

    spec = importlib.util.spec_from_file_location(moduleName, filepath)
    outputModule = importlib.util.module_from_spec(spec)
    sys.modules[moduleName] = outputModule
    spec.loader.exec_module(outputModule)

    os.chdir(cwd)

    return outputModule

def getMonthCols(priceDf):
    monthCols = [x for x in priceDf.columns if re.search('Month', x) is not None]
    return priceDf.loc[:, monthCols]

def getPriceCols(priceDf):
    priceCols = [x for x in priceDf.columns if re.search('Price', x) is not None]
    return priceDf.loc[:, priceCols]

def pandasToNumpy(pandasObj: Union[pd.DataFrame,pd.Series]):
    """
    Generate a numpy array from pandasObj with index and col maps.
    """
    npArray = pandasObj.to_numpy()
    if type(pandasObj) == pd.Series:
        colsMap = {}
    else:
        colsMap = {col: i for col, i in zip(pandasObj.columns, range(len(pandasObj.columns)))}
    rowsMap = {ind: i for ind, i in zip(pandasObj.index, range(len(pandasObj.index)))}
    return npArray, rowsMap, colsMap

def initializeArrayFromDataframe(dataframe: pd.DataFrame):
    """Generate ArrayWithMaps object from dataframe."""
    array, rowsMap, colsMap = pandasToNumpy(dataframe)
    arrayInstance = ArrayWithMaps(array, rowsMap, colsMap)
    return arrayInstance

def initializeArrayFromFile(fileAddress: str):
    """Generate ArrayWithMaps object from csv file."""
    dataframe = loadPricingDataframe(fileAddress)
    return initializeArrayFromDataframe(dataframe)

def initializeArrayFromDict(dict: dict, indexKey: any = None, maintainOriginalDict: bool = True):
    """
    Generate ArrayWithMaps object from dict.

    Will use number indexing if none of the keys specified as index.
    maintainOriginalDict set to False will give a performance boost but will destroy the input dictionary.
    """
    if maintainOriginalDict:
        dict = deepcopy(dict)
    if indexKey is not None:
        index = dict.pop(indexKey)
    else:
        index = list(range(len(dict)))
    cols = list(dict.keys())
    data = list(dict.values())
    arrayObj = ArrayWithMaps(
        array=np.array(data).T,
        rowsMap={ind: i for ind, i in zip(index, range(len(index)))},
        colsMap={col: i for col, i in zip(cols, range(len(cols)))}
    )
    return arrayObj

def weightedAverage(values, weights):
    return np.average(values, weights=weights)

def weightedStDev(values, weights):
    wAvg = weightedAverage(values, weights)
    sumProduct = sum([((x - wAvg) ** 2) * y for x, y in zip(values, weights)])
    adjSumWeights = sum(weights)# - 1
    return (sumProduct / adjSumWeights) ** 0.5

def dayOfWeekNP(dates):
    return (dates.astype('datetime64[D]').view('int64') - 4) % 7

def product(lst):
    return reduce(mul, lst, 1)

def arrayTrainTestSplit(array: ArrayWithMaps, testSize: float, setIndexToOriginal: bool = False):
    df = array.toDataframe()
    train, test = train_test_split(df, test_size=testSize)
    train, test = train.sort_index(), test.sort_index()
    if setIndexToOriginal:
        train.index = df.index[:train.shape[0]]
        test.index = df.index[:test.shape[0]]
    trainArray = initializeArrayFromDataframe(train)
    testArray = initializeArrayFromDataframe(test)
    return trainArray, testArray

def calculateReturnsOfSeries(priceSeries: pd.Series):
    return priceSeries / priceSeries.shift(1) - 1

def writeDfToExcel(df, excelFileLocation, sheetName, writeIndex=False, useOpenPyXlAsEngine=True):
    """Use xlsxwriter only if you MUST format dates and do not care if the write deletes all other sheets."""
    if useOpenPyXlAsEngine: #!should use openpyxl if not trying to format dates
        with pd.ExcelWriter(excelFileLocation, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheetName, index=writeIndex)
    else:
        with pd.ExcelWriter(excelFileLocation, engine='xlsxwriter', datetime_format='m/d/yyyy', date_format='m/d/yyyy') as writer:
            df.to_excel(writer, sheet_name=sheetName, index=writeIndex)

def sendEmail(
    to,
    subject,
    body=None,
    attachmentAddresses=[]
):
    outlook = client.Dispatch("Outlook.Application")

    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    if body is not None:
        mail.Body = body

    if attachmentAddresses != []:
        for attachmentAddress in attachmentAddresses:
            mail.Attachments.Add(attachmentAddress)

    mail.Send()

def makeAppointment(
    subject: str,
    startDate: pd.Timestamp,
    startHour24Fmt: int,
    startMinute: int,
    reminderMinutesBefore=5,
    body: str = None,
    location: str = None
):
    outlook = client.Dispatch("Outlook.Application")

    appointment = outlook.CreateItem(1)

    startStr = f"{startDate.strftime('%m/%d/%Y')} {startHour24Fmt}:{str(startMinute) if startMinute >= 10 else '0' + str(startMinute)}:00"

    appointment.subject = subject
    appointment.start = startStr
    appointment.duration = 0
    appointment.reminderset=True
    appointment.reminderminutesbeforestart = reminderMinutesBefore

    if location is not None:
        appointment.location = location
    if body is not None:
        appointment.body = body

    appointment.save()

def calculateRsi(priceSeries, periods=14):
    priceChanges = priceSeries.diff()

    upPriceChanges = priceChanges.clip(lower=0)
    downPriceChanges = - priceChanges.clip(upper=0) #these are positive

    upPriceChangesWeightedAverages = upPriceChanges.ewm(com=periods-1, min_periods=periods).mean()
    downPriceChangesWeightedAverages = downPriceChanges.ewm(com=periods-1, min_periods=periods).mean()

    upDownRatio = upPriceChangesWeightedAverages / downPriceChangesWeightedAverages

    rsi = 100 - (100 / (1 + upDownRatio))

    return rsi

def generateCommodityInfoConverter(fromKey, toKey):
    """
    Keys: shortName, oldName, formalName, bloombergSymbol, yellowKey, systemTicker, sector, drwSymbol, currency, varName, contractSize, bloombergDollarDivisor, settlementTime
    """
    return {singleCommodityInfo[fromKey]: singleCommodityInfo[toKey] for singleCommodityInfo in commodityInfo.values()}

def generateContractMonthConverter(fromKey, toKey):
    """
    Keys: int, bloombergCode, abbreviation, fullName
    """
    return {singleContractMonthInfo[fromKey]: singleContractMonthInfo[toKey] for singleContractMonthInfo in contractMonthInfo.values()}

def calculateNWeekdaysShift(date, n):
    isWeekend = date.weekday() == 5 or date.weekday() == 6
    if isWeekend and n < 0:
        date = calculatePriorWeekday(date)
    elif isWeekend and n > 0:
        date = calculateNextWeekday(date)

    dateInd = np.where(weekdays == date)[0][0]

    return dt(weekdays[dateInd + n])

def calculateWeekdaysBetween(startDate, endDate):
    subset = weekdays[(weekdays >= startDate) & (weekdays <= endDate)]
    return len(subset)

def calculateContractSize(bloombergTicker, monthBloombergCode: str=None, year: int=None):
    if commodityInfo[bloombergTicker.lower()]['variableContractSize']:
        if monthBloombergCode is None or year is None:
            raise IndexError("Enter a month for variable contract commodity.")
        vcsDf = variablesContractSizes[bloombergTicker.lower()]
        contractSize = vcsDf.loc[(vcsDf['monthCode'] == monthBloombergCode) & (vcsDf['year'] == year), 'contSize'].values[0]
    else:
        contractSize = commodityInfo[bloombergTicker.lower()]['contractSize']

    return contractSize

def camelToSnake(camelCaseString):
   snakeCaseString = re.sub('([A-Z])', r'_\1', camelCaseString).lower()
   return snakeCaseString

def snakeToCamel(snakeCaseStr):
   camelCaseString = re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), snakeCaseStr)
   return camelCaseString

def loadExcelForCheck(excelFilePath, sheetName='Sheet1', columnNames=None, excelColumns=None, skiprows=0, dtypes=None):
    usingXlsb = re.search('\.xlsb', excelFilePath) is not None
    engine = 'pyxlsb' if usingXlsb else 'openpyxl'

    if columnNames is None:
        df = pd.read_excel(
            io=excelFilePath,
            sheet_name=sheetName,
            header=0,
            index_col=0,
            skiprows=skiprows,
            engine=engine,
        )
    else:
        df = pd.read_excel(
            io=excelFilePath,
            sheet_name=sheetName,
            header=None,
            names=columnNames,
            index_col=0,
            usecols=excelColumns,
            skiprows=skiprows,
            engine=engine,
        )
    df = df[~df.eq('0x2a').any(1)] #remove any rows with blanks
    df = df[~df.eq('0x7').any(1)] #remove any rows with blanks
    df = df[~df.eq('0x17').any(1)] #remove any rows with blanks

    if usingXlsb:
        df.index = [xldate_as_datetime(x, datemode=0) for x in df.index]
        for col in [key for key, value in dtypes.items() if re.search('date', value)]:
            df[col] = df[col].fillna(0)
            df[col] = [xldate_as_datetime(x, datemode=0) for x in df[col]]
            df[col] = df[col].replace('12/31/1899', np.nan)

    if dtypes is not None:
        df = df.astype(dtypes)

    df.index = pd.to_datetime(df.index)
    return df

def compareTwoDfs(df1, df2, threshold=0.00001):
    resDict = {}

    df1ColsSet = set(df1.columns)
    sharedColumns = [x for x in df2.columns if x in df1ColsSet]

    #sharedColumns = list(set(df1.columns).intersection(set(df2.columns)))

    df1 = df1[sharedColumns]
    df2 = df2[sharedColumns]
    df1 = df1.loc[(df1.index >= df2.index.min()) & (df1.index <= df2.index.max())]
    df2 = df2.loc[(df2.index >= df1.index.min()) & (df2.index <= df1.index.max())]

    for col in sharedColumns:
        if df1[col].dtype == 'bool':
            df1[col] = deepcopy(df1[col]).astype('int')
        if df2[col].dtype == 'bool':
            df2[col] = deepcopy(df2[col]).astype('int')
        if df1[col].dtype == 'O':
            df1[col] = [hash(x) for x in df1[col]]
        if df2[col].dtype == 'O':
            df2[col] = [hash(x) for x in df2[col]]

        diffed = abs(df1[col].fillna(999999999) - df2[col].fillna(999999999))
        diffed[diffed > threshold] = 1
        diffed[diffed <= threshold] = 0
        firstError = str(diffed.index[diffed == 1][0].date()) if diffed.sum() != 0 else 'N/A'
        resDict[col] = [diffed.sum(), firstError]

    if df1.empty or df2.empty:
        for key in resDict.keys():
            resDict[key] = [999999, dt('1/1/1900')]

    return resDict

def printCheckResults(resDict, printFile=sys.stdout):
    earliestError = dt('1/1/2100')
    earliestErrorItem = ''
    totalErrors = 0

    for key, value in resDict.items():
        totalErrors += value[0]
        print(f"{key}: {int(value[0])} ({value[1]})", file=printFile)
        if value[1] != 'N/A':
            if dt(value[1]) < dt(earliestError):
                earliestError = value[1]
                earliestErrorItem = key

    print(file=printFile)

    if earliestErrorItem != '':
        print(f"Earliest error on {earliestError} for {earliestErrorItem}", file=printFile)

    print(file=printFile)

def findActiveFile(folder, fileGeneralName, fileExtension, use_vFormat=True):
    """
    Allows finding the address of the most recent version of an evolving file with the format e.g. "filename_v01.txt" (if use_vFormat is True) or "filename1.txt" (if use_vFormat is False).

    folder: the folder where the evolving file lives
    fileGeneralName: the part of the filename before the "_v01" in the example above if using _v format, or before the "1" if not using _v format
    fileExtension: the file type excluding the period
    use_vFormat: whether to assume the filename format includes "_v" at the end

    Returns the whole file address, including the folder.
    """
    pattern = f"^{fileGeneralName}_v(\d+).{fileExtension}$" if use_vFormat else f"^{fileGeneralName}(\d+).{fileExtension}$"
    excelFilesAndVersionNums = {int(re.search(pattern, x).group(1)): x for x in os.listdir(folder) if re.search(pattern, x)}
    latestFile = excelFilesAndVersionNums[max(excelFilesAndVersionNums.keys())]

    return f"{folder}/{latestFile}"

def dataframeToListOfLists(dataframe: pd.DataFrame, includeColumns=True, includeIndex=True, colsWithDates=[], dateIndex=False):
    dataframe = deepcopy(dataframe)
    if dateIndex:
        dataframe.index = dataframe.index.strftime('%m/%d/%Y')
    for colWithDate in colsWithDates:
        dataframe[colWithDate] = dataframe[colWithDate].dt.strftime('%m/%d/%Y')
    lol = dataframe.values.tolist()
    if includeIndex:
        for i, l in zip(range(len(lol)), lol):
            l.insert(0, dataframe.index[i])
    if includeColumns:
        if includeIndex:
            lol.insert(0, ['Index'] + list(dataframe.columns))
        else:
            lol.insert(0, list(dataframe.columns))

    return lol

def listOfListsToDataframe(listOfLists, includeColumns=True, indexLabel=None, colsWithDates=[], dateIndex=False):
    dataframe = pd.DataFrame(listOfLists)
    if includeColumns:
        dataframe.columns = dataframe.loc[0]
        dataframe = dataframe.iloc[1:]
    if indexLabel is not None:
        dataframe = dataframe.set_index(indexLabel)
    if dateIndex:
        dataframe.index = dt(dataframe.index)
    for colWithDate in colsWithDates:
        dataframe[colWithDate] = dt(dataframe[colWithDate])

    return dataframe

def largestPeriodFinder(series: pd.Series, numPeriods: int, aggregatorFn, numberToReturn: int=10):
    aggregations = {
        'startIndex': [],
        'endIndex': [],
        'startInt': [],
        'endInt': [],
        'aggregation': [],
    }
    for i in range(len(series) - numPeriods):
        startInt = i
        endInt = i + numPeriods
        startIndex = series.index[i]
        endIndex = series.index[i + numPeriods]
        aggregated = aggregatorFn(series[i:i + numPeriods])

        aggregations['startIndex'].append(startIndex)
        aggregations['endIndex'].append(endIndex)
        aggregations['startInt'].append(startInt)
        aggregations['endInt'].append(endInt)
        aggregations['aggregation'].append(aggregated)

    df = pd.DataFrame(aggregations)

    bests = []
    for _ in range(numberToReturn):
        best = df.loc[df['aggregation'] == df['aggregation'].min()]
        bests.append(best)
        df = df.loc[~((df['startInt'] >= best.loc[best.index[0], 'startInt']) & (df['startInt'] <= best.loc[best.index[0], 'endInt'])) & ~((df['endInt'] >= best.loc[best.index[0], 'startInt']) & (df['endInt'] <= best.loc[best.index[0], 'endInt']))]

    bestDf = pd.concat(bests)

    return bestDf

def addNextPeriodResult(periodsDf, series, days):
    results = []
    for i in periodsDf.index:
        startDate = calculateNWeekdaysShift(periodsDf.loc[i, 'endIndex'], 1)
        endDate = calculateNWeekdaysShift(periodsDf.loc[i, 'endIndex'], days)
        #print(startDate, endDate)
        result = series.loc[(series.index >= startDate) & (series.index <= endDate)].sum()
        results.append(result)
    periodsDf[f'next{days}Result'] = results
    return periodsDf

def pullBloombergDataFrame(
    securities,
    fields,
    startDate,
    endDate,
    includeAllWeekdays=True,
    connection=None
):
    if connection is None:
        connection = blp.BlpQuery().start()

    nonTradingDayFillOption = 'NON_TRADING_WEEKDAYS' if includeAllWeekdays else 'ACTIVE_DAYS_ONLY'

    raw = connection.bdh(
        securities=securities,
        fields=fields,
        start_date=startDate.strftime('%Y%m%d'),
        end_date=endDate.strftime('%Y%m%d'),
        options=[('nonTradingDayFillOption', nonTradingDayFillOption)]
    )
    df = raw.pivot(columns=['security'], index='date')
    return df