from flask import Flask,request,render_template,session,redirect,url_for

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []
users.append(User(username="test", password="test"))

app=Flask(__name__,static_folder="templates",static_url_path="/")
app.secret_key = "Amber's secret key"

@app.route("/")
def home():
    if "username" in session:
        session["logged_in"] = True
        return redirect(url_for("member"))
    else:
        session.pop("username", None)
        return render_template("home.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if (username == "test") and (password == "test"):
            session["username"] = username
            session["password"] = password
            session["logged_in"] = True
            return redirect(url_for("member"))           
        else:
            session["username"] = username
            session["password"] = password
            return redirect(url_for("error"))
            session.pop("username", None)   
    return render_template("home.html")

@app.route("/member/")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        session.pop("username", None)
        return redirect(url_for("home"))

@app.route("/error/")
def error():
    if "username" in session:
        session.pop("username", None)
        return render_template("error.html")
    else:
        return redirect(url_for("home"))


@app.route("/signout", methods=["GET"])
def signout():
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(port=3000,debug=True)