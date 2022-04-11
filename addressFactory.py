from typing import List

# 处理函数（将地址按行政单位划分）
def factory(address: str) -> List[str]:
    split = list()
    # 特殊城市
    if address[2] == "市":
        province = address[:3]
        split.append(province)
        city = address[3:]
        split.append(city)
        return split
    elif "特别行政区" in address:
        province = address[:7]
        split.append(province)
        city = address[7:]
        split.append(city)
        return split
    # 省级行政单位
    if "省" in address:
        # 定位长度
        p = address.find("省")
        province = address[:p + 1]
        split.append(province)
        remain = address[p + 1:]
        split.append(remain)
    elif "自治区" in address:
        # 定位长度
        p = address.find("自治区")
        province = address[:p + 3]
        split.append(province)
        remain = address[p + 3:]
        split.append(remain)
    # 市级行政单位
    if "自治州" in split[1]:
        p = split[1].find("自治州")
        split[1] = split[1][:p + 3]
    elif "地区" in split[1]:
        p = split[1].find("地区")
        split[1] = split[1][:p + 2]
    elif "盟" in split[1]:
        p = split[1].find("盟")
        split[1] = split[1][:p + 1]
    elif "市" in split[1]:
        p = split[1].find("市")
        split[1] = split[1][:p + 1]
    return split