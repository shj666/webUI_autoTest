
import xlrd
from framework.logger import Logger

logger = Logger("logger=Lianxi").getlog()

class Lianxi(object):

    @classmethod
    def read_excel(self, excelPath, sheetName = "DNF"):


        workbook = xlrd.open_workbook(excelPath)
        sheet = workbook.sheet_by_name(sheetName)
        # 获取第一行作为key值
        keys = sheet.row_values(0)
        # 获取总行数
        rowNum = sheet.nrows
        # 获取总列数
        cloNum = sheet.ncols


        if rowNum <=1:
            logger.error("excel表中数据总行数小于1")
        else:
            r = []
            for i in range(1, rowNum):
                sheet_data = { }
                values = sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]] = values[j]
                r.append(sheet_data)
        return r

if __name__ == "__main__":

    print(Lianxi.read_excel("D:/data/dnf.xlsx", "DNF"))

