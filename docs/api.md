
## 1. 获取拍卖列表

### 请求方式

```HTTP
GET /auctions [200]
```

### 请求参数

| 参数名称    | 是否必须 | 类型   | 描述     | 默认值 | 取值范围                                                  |
| ----------- | -------- | ------ | -------- | ------ | --------------------------------------------------------- |
| productName | false    | String | 商品名    | 无     |                                                           |
| quality     | false    | String | 商品成色   | 无     | ["9成新", "7成新", "9.5成新", "8成新", "9.9成新", "95新"] |
| status      | false    | Int    | 商品状态 | 1      | 1未结束, 2 已结束                                         |
| pages       | false    | Int    | 当前页   | 1      |                                      |
| per_page    | false    | Int    | 分页数   | 30      |                                          |

**响应示例**:

```javascript
{
  "data": [
    {
      "auction_id": 114127384,
      "currentPrice": 1.0,
      "endTime": 1553561460000,
      "productName": "【备件库99新】小米（MI）小米AI音箱 白色 小爱智能音箱 听音乐语音遥控家电 人工智能音箱",
      "quality": "9.9成新",
      "status": 1
    },
    {
      "auction_id": 114127385,
      "currentPrice": 1.0,
      "endTime": 1553565540000,
      "productName": "【备件库99新】小米（MI）小米AI音箱 白色 小爱智能音箱 听音乐语音遥控家电 人工智能音箱",
      "quality": "9.9成新",
      "status": 1
    }
  ],
  "page": {
    "current": 1,
    "pages": 1,
    "per_page": 30
  },
  "total": 4
}
```