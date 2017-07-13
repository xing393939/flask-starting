# coding: utf-8

_DBUSER = "root" # 数据库用户名
_DBPASS = "" # 数据库密码
_DBHOST = "localhost" # 数据库地址
_DBNAME = "kiblog" # 数据库名称

#config
SECRET_KEY = 'flaskblog'
BLOG_TITLE = '我的博客'
BLOG_URL = 'http://www.demo.com'
BLOG_NAME = 'Blog'

class rec: pass

rec.database = 'mysql://%s:%s@%s/%s' % (_DBUSER, _DBPASS, _DBHOST,_DBNAME)
rec.description = u"my blog"
rec.url = 'http://www.demo.com'
rec.paged = 8
rec.archive_paged = 20
rec.admin_username = 'admin'
rec.admin_email = 'admin@admin.com'
rec.admin_password = 'admin1'
rec.default_timezone = "Asia/Shanghai"
