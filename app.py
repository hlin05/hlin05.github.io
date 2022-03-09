# Implements a registration form, confirming registration via email


from django.shortcuts import render
from flask import Flask, render_template
from flask_frozen import Freezer
#from flask_mail import Mail, Message
# from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#session=Session(app)

# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"

# Requires that "Less secure app access" be on
# https://support.google.com/accounts/answer/6010255
# app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
# app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
# mail = Mail(app)

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fail")
def fail():
    return render_template("failure.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/gallary")
def gallary():
    return render_template("gallary.html")

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/liion-batteries")
def lion():
    return render_template("liion-batteries.html")

@app.route("/multi")
def multi():
    return render_template("multivalent.html")

@app.route("/redox")
def redox():
    return render_template("redox.html")

@app.route("/water")
def water():
    return render_template("water.html")

@app.route("/fluid")
def fluid():
    return render_template("fluid.html")

@app.route("/prin_inv")
def prin_inv():
    return render_template("prin_inv.html")

@app.route("/alumni")
def alumni():
    return render_template("alumni.html")

@app.route("/pub")
def pub():
    return render_template("pub.html")

@app.route("/teach")
def teach():
    return render_template("teach.html")

@app.route("/univ")
def univ():
    return render_template("univ.html")

@app.route("/slc")
def slc():
    return render_template("slc.html")

@app.route("/equip")
def equip():
    return render_template("equip.html")

@app.route("/open")
def open():
    return render_template("open.html")

@app.route("/member")
def member():
    return render_template("member.html")
# freezer = Freezer(app)

# if __name__ == '__main__':
#     freezer.freeze()