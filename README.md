# 基于flask和mysql的博客

# 运行

1. pip install -r requirements.txt
1. 关于提示“No module named MySQLdb”，解决方案如下：
 * easy_install mysql-python (mix os)
 * pip install mysql-python (mix os)
 * apt-get install python-mysqldb (Linux Ubuntu, ...)
 * cd /usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)
 * yum install MySQL-python (Linux Fedora, CentOS ...)
 * For Windows, see this answer: [Install mysql-python (Windows)](https://stackoverflow.com/questions/21440230/install-mysql-python-windows)
1. python app.py
1. 访问 http://path/intsall 导数据库
