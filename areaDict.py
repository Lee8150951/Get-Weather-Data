# 区域面积处理
import pyxlUnit

def areaDict():
    file_name = "./resources/area.xlsx"
    excelFile = pyxlUnit.DoExcel(file_name)
    area = excelFile.do_excel('2020年区域面积')
    areaDict = dict()
    for current in area:
        if current['City'] != None:
            cityName = current['City']
            cityArea = current[2020] * 10000
            cityArea = '%.4f' % cityArea
            areaDict[cityName] = cityArea
    return areaDict