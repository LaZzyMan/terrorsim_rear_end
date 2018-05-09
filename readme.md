# GTD-Backend

> 全球恐怖袭击可视化系统后端数据Restful API及数据管理

## API Description

API root: http://47.94.208.122/gtd/api

### 点位数据：tdgeneral

调用参数：

参数 | 描述 | 示例
-|:-:|-
year | 年份 | 1970
countryid|国家编号|100
regionid|地区编号|12
format|格式|api/json

返回数据格式为geojson：
```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "coordinates": [
                    -118.027606,
                    34.06857
                ],
                "type": "Point"
            },
            "properties": {
                "year": 1970,
                "month": 12,
                "day": 31,
                "city": "El Monte ",
                "country_id": {
                    "country_id": 217,
                    "country_name": "United States"
                }
            }
        }
    ]
}
```

### 事件详细数据：tfinfo

#### retrieve调用：
pk=eventid

eg: http://47.94.208.122/gtd/api/tdinfo/201701270001

#### list调用参数（速度慢，不推荐）：

参数 | 描述 | 示例
-|:-:|-
year | 年份 | 1970
countryid|国家编号|100
regionid|地区编号|12
format|格式|api/json

返回数据格式为geojson：
```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "coordinates": [
                    -118.027606,
                    34.06857
                ],
                "type": "Point"
            },
            "properties": {
                "year": 1970,
                "month": 12,
                "day": 31,
                "city": "El Monte ",
                "country_id": {
                    "country_id": 217,
                    "country_name": "United States"
                }
            }
        }
    ]
}
```

### 国家数据：country

### 地区数据：region

### 词频数据：keyword


## 后台数据管理

URL: http://47.94.208.122/gtd/admin