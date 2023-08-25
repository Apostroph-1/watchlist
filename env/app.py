from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy #数据库
import os
import sys
#
# WIN = sys.platform.startswith('win')
# if WIN:  # 如果是 Windows 系统，使用三个斜线
#     prefix = 'sqlite:///'
# else:  # 否则使用四个斜线
#     prefix = 'sqlite:////'

app = Flask(__name__)#用flask中的 Flask类 通过实例化这个类，创建一个程序对象app
#Flask.config 字典。配置变量的名称必须使用大写，写入配置的语句一般会放到扩展类实例化语句之前。
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# #添加数据库文件的绝对路径
# #
# # 在扩展类实例化前加载配置
# db = SQLAlchemy(app)#初始化拓展,传入程序实例 app
# #模型类要声明继承 db.Model
# class User(db.Model):#表名user自动生成，并小写
#     id = db.Column(db.Integer,primary_key = True)#主键
#     name = db.Column(db.String(20)) #名字
#
# class Movie(db.Model):#表名 Movie
#     id = db.Column(db.Integer,primary_key = True)#主键
#     title = db.Column(db.String(60))
#     year = db.Column(db.String(4))


#
# @app.route('/')
# def hello():
#     return 'Welcome to My Watchlist!'

# @app.route('/')
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'

# @app.route('/test')
# def test_url_for():
#     # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
#     print(url_for('hello'))
#     # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
#     print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
#     print(url_for('user_page', name='peter'))  # 输出：/user/peter
#     print(url_for('test_url_for'))  # 输出：/test
#     # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
#     print(url_for('test_url_for', num=2))  # 输出：/test?num=2
#     return 'Test page'


name = 'Shelton'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
def index():
    return render_template("index.html", name=name, movies=movies)



if __name__ == '__main__':
    app.run(port=5001,debug=True)