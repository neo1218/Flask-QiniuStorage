# Flask-Zero
[七牛云存储](http://www.qiniu.com/)Flask扩展

## 安装
```python
pip install flask-zero
```

## 配置
| 配置项 | 说明 |
|:--------------------:|:---------------------------:|
| QINIU_ACCESS_KEY | 七牛 Access Key |
| QINIU_SECRET_KEY | 七牛 Secret Key |
| QINIU_BUCKET_NAME | 七牛空间名称 |
| QINIU_BUCKET_DOMAIN | 七牛空间对应域名 |

## 使用
```python
from flask import Flask
from flask_zero import Qiniu

QINIU_ACCESS_KEY = '七牛 Access Key'
QINIU_SECRET_KEY = '七牛 Secret Key'
QINIU_BUCKET_NAME = '七牛空间名称'
QINIU_BUCKET_DOMAIN = '七牛空间对应域名'

app = Flask(__name__)
app.config.from_object(__name__)
qiniu = Qiniu(app)
# 或者
# qiniue = Qiniu()
# qiniu.init_app(app)

# 保存文件到七牛
@app.route('/save')
def save():
    data = 'data to save'
    filename = 'filename'
    ret, info = qiniu.save(data, filename)
    return str(ret)

# 删除七牛空间中的文件
@app.route('/delete')
def delete():
    filename = 'filename'
    ret, info = qiniu.delete(filename)
    return str(ret)

# 根据文件名获取对应的公开URL
@app.route('/url')
def url():
    filename = 'filename'
    return qiniu.url(filename)

# 根据文件名获取文件信息字典
@app.route('/info')
def info():
    filename = 'filename'
    return qiniu.info(filename)
```

## 许可
The MIT License (MIT). 详情见 __License文件__
