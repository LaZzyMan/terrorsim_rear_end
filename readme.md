# GTD-Backend

> 全球恐怖袭击可视化系统后端数据Restful API及数据管理

## API Description

API root: http://47.94.208.122/gtd/api

API schema: http://47.94.208.122/gtd/api/schema

### 点位数据：tdgeneral

调用参数：

参数 | 描述 | 示例
-|:-:|-
year | 年份 | 1970
countryid|国家编号|100
regionid|地区编号|12
keyword|关键词|10
start|开始时间|19700101
end|结束时间|19701231
poly|多边形边界|[(0,0),(0,1),(1,1),(0,0)]
format|格式|api/json

返回数据格式为geojson：
```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "id": "197012310002",
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -118.027606,
                    34.06857
                ]
            },
            "properties": {
                "year": 1970,
                "month": 12,
                "day": 31,
                "city": "El Monte ",
                "country": {
                    "countryId": 165,
                    "countryName": "United States",
                    "region": 1
                },
                "dayInYear": 365
            }
        },
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
keyword|关键词|10
start|开始时间|19700101
end|结束时间|19701231
poly|多边形边界|[(0,0),(0,1),(1,1),(0,0)]
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

#### 统计数据：/statistics

返回格式数据格式：
```json

```

### 国家数据：country

#### retrieve调用：
pk=countryId

eg: http://47.94.208.122/gtd/api/country/1

#### list调用:
返回所有国家边界多边形数据。

### 地区数据：region

### 词频数据：keyword


## 后台数据管理

URL: http://47.94.208.122/gtd/admin
