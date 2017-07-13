# 基于flask和mysql的博客

# 运行

一. pip install -r requirements.txt

二. 关于提示“No module named MySQLdb”，解决方案如下：

1. easy_install mysql-python (mix os)
1. pip install mysql-python (mix os)
1. apt-get install python-mysqldb (Linux Ubuntu, ...)
1. cd /usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)
1. yum install MySQL-python (Linux Fedora, CentOS ...)
1. For Windows, see this answer：[Install mysql-python (Windows)](https://stackoverflow.com/questions/21440230/install-mysql-python-windows)

三. python app.py

四. 访问 http://path/intsall 导数据库
