import xlrd
import openpyxl
import addressFactory

# 处理地级市分类
data = xlrd.open_workbook('./export/position/PositionTidy.xls')
table = data.sheets()[0]
# 获取数据
positions = table.col_values(0)[1:]
# 地级市集合
cities = set()
for position in positions:
    # 使用工厂处理
    currentSplit = addressFactory.factory(position)
    cities.add(currentSplit[1])

longitude = table.col_values(1)[1:]
latitude = table.col_values(2)[1:]
storeHouse = list()
for city in cities:
    # 临时存储
    storage = list()
    # 存入城市
    storage.append(city)
    for i in range(len(positions)):
        if city in positions[i]:
            lola = str(longitude[i]) + "," + str(latitude[i])
            storage.append(lola)
    # 存储至仓库
    storeHouse.append(storage)

# 导出
newExl = openpyxl.Workbook()
sheet = newExl.create_sheet()
for storeData in storeHouse:
    sheet.append(storeData)
# 储存
newExl.save(filename = './export/position/long&lati.xlsx')

print("Success!")