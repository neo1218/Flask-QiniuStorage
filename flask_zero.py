# -*- coding: utf-8 -*-

from urlparse import urljoin
import qiniu as QiniuClass


class Qiniu(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._access_key = app.config.get('QINIU_ACCESS_KEY', '')
        self._secret_key = app.config.get('QINIU_SECRET_KEY', '')
        self._bucket_name = app.config.get('QINIU_BUCKET_NAME', '')
        domain = app.config.get('QINIU_BUCKET_DOMAIN')
        if not domain:
            self._base_url = 'http://' + self._bucket_name + '.qiniudn.com'
        else:
            self._base_url = 'http://' + domain

    def save(self, data, filename=None):
        auth = QiniuClass.Auth(self._access_key, self._secret_key)
        token = auth.upload_token(self._bucket_name)
        return QiniuClass.put_data(token, filename, data)

    def delete(self, filename):
        auth = QiniuClass.Auth(self._access_key, self._secret_key)
        bucket = QiniuClass.BucketManager(auth)
        return bucket.delete(self._bucket_name, filename)

    def url(self, filename):
        return urljoin(self._base_url, filename)

    def info(self, filename):
        """获取文件信息"""
        auth = QiniuClass.Auth(self._access_key, self._secret_key)
        bucket = QiniuClass.BucketManager(auth)
        bucket_name = self._bucket_name
        ret, info = bucket.stat(bucket_name, filename)
        # return str(info)  # -a dict-: ResponseInfo object, How 2 get item!?
        if ret is not None:
            return dict(ret)
        else:
            return {}
