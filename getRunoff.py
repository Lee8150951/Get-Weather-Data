import os
import areaDict
import pyxlUnit
import openpyxl
from typing import List

# 处理单一字典数据
def process(dataDic):
    storage = list()
    for key, value in dataDic.items():
        if key == "年份\\月份":
            storage.append(value)
        else:
            storage.append(value)
    return storage

# 封装分城市创建excel文件函数，参数列表：1.城市名称；2.数据列表
def cityData(city: str, data: List[int]):
    newExl = openpyxl.Workbook()
    sheet = newExl.active
    # 创建表头
    months = ["年份\月份", "一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    data.insert(0, months)
    # 循环数据
    for row_index, row_item in enumerate(data):
        for col_index, col_item in enumerate(row_item):
            sheet.cell(row=row_index+1,column= col_index+1,value = col_item)
    # 储存
    path = f"./export/runoff/{city}.xlsx"
    newExl.save(filename = path)
    

if __name__ == '__main__':
    # 获取面积字典
    dict = areaDict.areaDict()
    # 获取城市蒸发量数据
    fileList = os.listdir('./export/new_eva')
    for city in fileList:
        # 读取城市名称
        cityName = city.split('.')[0]
        # 没有城市面积数据
        if cityName not in dict.keys():
            # 生成txt数据提示错误
            with open('./export/runoff/没有处理城市.txt', 'a', encoding='utf-8') as notion:
                notion.write(f'{cityName};')
        else:
            # 面积
            area = dict[cityName]
            # 获取降水量precipitation
            preFilePath = './export/new_pre/' + city
            preFile = pyxlUnit.DoExcel(preFilePath)
            preDatas = preFile.do_excel('Sheet')
            # 获取蒸发量evaporation
            evaFilePath = './export/new_eva/' + city
            evaFile = pyxlUnit.DoExcel(evaFilePath)
            evaDatas = evaFile.do_excel('Sheet')
            # 循环年份(21年)
            years = len(preDatas)
            store = list()
            for year in range(years):
                thisYear = list()
                # 年数据
                yearPre = preDatas[year]
                preDataList = list(yearPre.values())[1:]
                yearEva = evaDatas[year]
                evaDataList = list(yearEva.values())[1:]
                # 年份值
                yearNum = 2000 + year
                thisYear.append(yearNum)
                # 循环月份(12个月)
                for month in range(12):
                    # 单位(亿立方米/s)
                    runoff = (float(area) * (float(preDataList[month]) + float(evaDataList[month]))) / 100000
                    runoff = '%.5f' % runoff
                    thisYear.append(runoff)
                store.append(thisYear)
            # 存储数据
            cityData(cityName, store)
    print("处理完成。。。")