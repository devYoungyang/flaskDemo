'''
Author: Yang
Date: 2021-07-08 09:57:29
LastEditors: Yang
LastEditTime: 2021-07-09 14:03:33
FilePath: /flaskDemo/ZeeRay/routes/route.py
Description: 头部注释
'''
from models.user import engine
from models.user import User
from flask import Flask, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import re
app = Flask(__name__)

session = sessionmaker(bind=engine, autocommit=True)()


@app.route('/')
def index():
    return 'Hello, World !!!'


@app.route('/register', methods=['POST'])
def user_register():
    username = request.values.get('username')
    password = request.values.get('password')
    tel = request.values.get('tel')
    data = session.query(User).filter(
        User.username == username or User.tel == tel).all()
    print(len(data))
    if username and password and tel:
        if len(data) >= 1:
            return jsonify({'code': '2002', 'msg': '用户已存在'})
        else:
            if (re.match('^1[3, 5, 7]\d{9}$', tel) and len(tel) == 11):
                user = User(username=username, password=password, tel=tel)
                session.add(user)
                session.commit()
                return jsonify({'code': '2000', 'msg': '注册成功'})
            return jsonify({'code': '2003', 'msg': '手机号不正确'})
    return jsonify({'code': '2001', 'msg': '用户名为空'})


@app.route('/login', methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    tel = request.values.get('tel')
    data = session.query(User).filter(
        User.username == username, User.password == password).all()
    print(len(data))
    if username and password and tel:
        if len(data) >= 1:
            return jsonify({'code': '2000', 'msg': '登录成功'})
        return jsonify({'code': '2002', 'msg': '账号或密码不正确'})
    return jsonify({'code': '2001', 'msg': '账号为空'})
