import xlrd
import os
from framework.logger import Logger

logger = Logger("logger=Lianxi").getlog()

class Lianxi(object):
    @classmethod
    def read_excel(self, excelPath, sheetName = 'DNF'):
        workbook = xlrd.open_workbook(excelPath)
        sheet = workbook.sheet_by_name(sheetName)

        keys = sheet.row_values(0)

        rowNum = sheet.nrows
        cloNum = sheet.ncols

        if rowNum<=1:
            logger.error("excel表中数据行数小于一")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data = {  }
                values = sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]] = values[j]
                    r.append(sheet_data)
        return r

if __name__=='__main__':
    filepath = "dnf.xlsx"
    sheetName="DNF"
    print(Lianxi().read_excel("../pageobjects/dnf.xlsx","DNF"))
