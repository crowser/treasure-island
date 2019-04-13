    # treasure-island

## 功能
* 纪录京东夺宝岛拍卖商品历史成交价格
* 待拍商品查询

## 构建/安装方法
1. 安装docker

    参照docker官方文档

2. 创建`.env`文件，内容为

    ```bash
    MONGO_INITDB_ROOT_USERNAME=root
    MONGO_INITDB_ROOT_PASSWORD=`配置密码密码`
    ```
3. 启动应用

    ```bash
    docker-compose up -d
    ```


## [API](docs/api.md) 



