1. 创建 `Python` 虚拟环境并生效

```shell
python3 -m venv myvenv
source myvenv/bin/activate
```

2. 安装必要库

```shell
python3 -m pip install django djangorestframework channels channels_redis
```

3. 启用通道层

通道层是一种通信系统。它允许多个消费者实例相互交谈.

每个消费者实例都有一个自动生成的唯一通道名称，所以可以通过通道层进行通信。

```shell
docker run -p 6379:6379 -d redis:5
```

4. 自动化测试

安装 `Chrome`

安装 `chromedriver`
```shell
curl https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip -O
unzip chromedriver_linux64.zip
mv chromedriver ../myvenv/bin/
sourece ../myvenv/bin/activate
```

安装 `Selenium`

```shell
python3 -m pip install selenium
```
