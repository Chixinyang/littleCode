#coding:utf-8

from flask import Flask,render_template,redirect

app = Flask(__name__)

#定义路由

#登录
@app.route("/login/",methods=["GET","POST"])
def login():
    return render_template("login.html") #渲染模板

#注册
@app.route("/register/",methods=["GET","POST"])
def register():
    return render_template("register.html") #渲染模板

#退出(302跳转到登录界面)
@app.route("/logout/",methods=["GET"])
def logout():
    return redirect("/login/") #渲染模板

#文章列表
@app.route("/art/list/",methods=["GET"])
def art_list():
    return render_template("art_list.html") #渲染模板

#编辑文章
@app.route("/art/edit/<int:id>",methods=["GET","POST"])
def art_edit(id):
    return render_template("art_edit.html") #渲染模板

#发布文章
@app.route("/art/add/",methods=["GET","POST"])
def art_add():
    return render_template("art_add.html") #渲染模板

#删除文章
@app.route("/art/del/<int:id>",methods=["GET"])
def art_del(id):
    return render_template("art_delete.html") #渲染模板

if __name__ == "__main__":
    #debug=True 调试模式自动运行修改后的文件
    app.run(debug=True,host="127.0.0.1",port=8080)