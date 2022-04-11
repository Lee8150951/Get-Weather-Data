import pyxlUnit
import os
import monthProcess
import openpyxl
from typing import List

# 处理单一字典数据
def process(dataDic):
    storage = list()
    for key, value in dataDic.items():
        if key == "年份\\月份":
            storage.append(value)
        else:
            monthDay = monthProcess.monthProcess(key)
            current = float(value) * monthDay
            storage.append(current)
    return storage


# 封装分城市创建excel文件函数，参数列表：1.城市名称；2.数据列表
def cityDate(city: str, data: List[int]):
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
    path = f"./export/new_eva/{city}.xlsx"
    newExl.save(filename = path)


if __name__ == '__main__':
    # 读取文件夹下所有已处理文件
    fileList = os.listdir('./export/evaporation')
    
    for file in fileList:
        path = "./export/evaporation/"
        file_name = path + file
        cityName = file.split(".")[0]
        print(f"正在处理的是：{cityName}")
        # 文件处理(获取字典)
        excelFile = pyxlUnit.DoExcel(file_name)
        datas = excelFile.do_excel('Sheet1')
        currentData = list()
        for data in datas:
            treatData = process(data)
            currentData.append(treatData)
        # 存储数据
        cityDate(cityName, currentData)