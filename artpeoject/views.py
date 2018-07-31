# coding:utf-8

from flask import Flask, render_template, redirect, flash, Response, session
from forms import LoginForm, RegisterForm, ArtAddForm
from models import User, db
from werkzeug.security import generate_password_hash
from datetime import datetime
from verification_code import Verify_Code
import os

app = Flask(__name__)
# 添加CSRF secret
app.config["SECRET_KEY"] = "123456"


# 定义路由

# 登录
@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("登录成功！", "login ok")
        return redirect('/art/list/')
    return render_template("login.html", title="登录", form=form)  # 渲染模板


# 注册
@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data  # data是一个字典类型
        # 保存数据
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(user)
        db.session.commit()
        # 定义一个会话闪现
        flash("注册成功,请登录", "register ok")
        return redirect("/login/")
    else:
        flash("哎呦，貌似注册还没成功", "register err")
    return render_template("register.html", title="注册", form=form)  # 渲染模板


# 退出(302跳转到登录界面)
@app.route("/logout/", methods=["GET"])
def logout():
    return redirect("/login/")  # 渲染模板


# 文章列表
@app.route("/art/list/", methods=["GET"])
def art_list():
    return render_template("art_list.html", title="文章列表")  # 渲染模板


# 编辑文章
@app.route("/art/edit/<int:id>", methods=["GET", "POST"])
def art_edit(id):
    return render_template("art_edit.html")  # 渲染模板


# 发布文章
@app.route("/art/add/", methods=["GET", "POST"])
def art_add():
    form = ArtAddForm()
    return render_template("art_add.html", title="文章发布", form=form)  # 渲染模板


# 删除文章
@app.route("/art/del/<int:id>", methods=["GET"])
def art_del(id):
    return render_template("art_delete.html")  # 渲染模板


# 验证码
@app.route("/verifycode/", methods=["GET"])
def verifycode():
    # 创建验证码
    verifycode = Verify_Code()
    verifycode.create_verification_code()
    # 读取图片的二进制编码
    with open(verifycode.image_path, mode='rb') as f:
        image = f.read()
    session.__setitem__("verifycode",verifycode.chars)
    print(session.__getitem__("verifycode"))
    # 以图片的格式返回
    return Response(image, mimetype='jpeg')


if __name__ == "__main__":
    # debug=True 调试模式自动运行修改后的文件
    app.run(debug=True, host="127.0.0.1", port=8080)
