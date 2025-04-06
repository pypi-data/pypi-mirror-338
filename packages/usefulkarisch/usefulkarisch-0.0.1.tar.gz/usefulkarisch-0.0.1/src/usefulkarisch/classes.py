import pandas as pd
import numpy as np
from typing import Any, Dict, List, Callable
from copy import deepcopy

class ArrayWithMaps:
    """
    Array with maps corresponding to index and column locations.

    Keyword arguments
    -----------------
    array :
        data array
    rowsMap :
        dict of row indices from name -> int index
    colsMap :
        dict of column indices from name -> int index

    Attributes
    ----------
    array :
        data array
    rowsMap :
        dict of row indices from name -> int index
    colsMap :
        dict of column indices from name -> int index
    rowsMapReversed :
        dict of row indices from int -> name index
    colsMapReversed :
        dict of column indices from int -> name index

    Methods
    -------
    loc :
        Get value for provided named row and column.
    iloc :
        Get value for provided numbered row and column.
    ilocRow :
        Get value for provided numbered row and named column.
    getInd :
        Get the row index name from provided row number.
    getCol :
        Get the column name from provided column number.
    getRowNum :
        Get the row number from provided row name.
    getColNum :
        Get the column number from provided column name.
    getFullIndex :
        Get list of all row names.
    getFullCols :
        Get list of all column names.
    getFullRowNums :
        Get list of all row numbers.
    getFullColNums :
        Get list of all column numbers.
    """
    def __init__(self, array: np.ndarray, rowsMap: Dict, colsMap: Dict):
        self.array = array
        self.rowsMap = rowsMap
        self.colsMap = colsMap

        self.rowsMapReversed = {val: key for key, val in self.rowsMap.items()}
        self.colsMapReversed = {val: key for key, val in self.colsMap.items()}

    def loc(self, rows: Any, cols: str = None):
        rows = self.rowsMap.keys() if rows is None else rows
        cols = self.colsMap.keys() if cols is None else cols
        rows = [rows] if not hasattr(rows, '__iter__') or type(rows) == str else rows
        cols = [cols] if not hasattr(cols, '__iter__') or type(cols) == str else cols
        inds = [self.rowsMap[x] for x in rows]
        colVals = [self.colsMap[x] for x in cols]
        return np.take(np.take(self.array, inds, axis=0), colVals, axis=1)

    def getVal(self, row: Any, col: Any):
        return self.array[self.rowsMap[row], self.colsMap[col]]

    def getRow(self, row: Any):
        return self.array[self.rowsMap[row], :]

    def iloc(self, rowNums: int, colNums: int):
        rowNums = [rowNums] if not hasattr(rowNums, '__iter__') else rowNums
        colNums = [colNums] if not hasattr(colNums, '__iter__') else colNums
        return np.take(np.take(self.array, rowNums, axis=0), colNums, axis=1)

    def ilocRow(self, rowNum: int, col: str):
        return self.array[rowNum, self.colsMap[col]]

    def getInd(self, rowNum: int):
        return self.rowsMapReversed[rowNum]

    def getCol(self, colNum: int):
        return self.colsMapReversed[colNum]

    def getRowNum(self, row: Any):
        return self.rowsMap[row]

    def getColNum(self, col: str):
        return self.colsMap[col]

    def getFullIndex(self):
        return list(self.rowsMap.keys())

    def getFullCols(self):
        return list(self.colsMap.keys())

    def getFullRowNums(self):
        return list(self.rowsMap.values())

    def getFullColNums(self):
        return list(self.colsMap.values())

    def getFullColData(self, col: str):
        return self.array[:, self.colsMap[col]]

    def indexOnColLoc(self, colToIndexOn, indexVal, colToReturnFrom):
        return self.loc(row=list(self.getFullColData(colToIndexOn)).index(indexVal), col=colToReturnFrom)

    def filterIndex(self, val: Any, comparisonFn: Callable):
        filteredIndex = {x: self.rowsMap[x] for x in self.rowsMap.keys() if comparisonFn(x, val)}
        newArray = np.take(self.array, list(filteredIndex.values()), axis=0)
        newRowsMap = {newInd: newI for newInd, newI in zip(filteredIndex.keys(), range(len(filteredIndex.keys())))}
        newColsMap = dict(self.colsMap)
        newArrayMap = ArrayWithMaps(array=newArray, rowsMap=newRowsMap, colsMap=newColsMap)
        return newArrayMap

    def filterColumns(self, val: Any, comparisonFn: Callable):
        filteredColumns = {x: self.colsMap[x] for x in self.colsMap.keys() if comparisonFn(x, val)}
        newArray = np.take(self.array, list(filteredColumns.values()), axis=1)
        newColsMap = {newInd: newI for newInd, newI in zip(filteredColumns.keys(), range(len(filteredColumns.keys())))}
        newRowsMap = dict(self.rowsMap)
        newArrayMap = ArrayWithMaps(array=newArray, rowsMap=newRowsMap, colsMap=newColsMap)
        return newArrayMap

    def toDataframe(self):
        return pd.DataFrame(data=self.array, index=self.rowsMap.keys(), columns=self.colsMap.keys())

    def toSeries(self):
        return pd.Series(data=self.array[:, 0], index=self.rowsMap.keys())