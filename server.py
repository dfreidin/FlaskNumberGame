from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "swordfish"
@app.route("/")
def index():
    if not (session.get("secret_num") and session.get("guess")):
        session["secret_num"] = random.randint(1,101)
        return render_template("index.html", check="new", message="")
    n = int(session["secret_num"])
    g = int(session["guess"])
    if g == n:
        return render_template("index.html", check="yes", message=str(n)+" was the number!")
    if g < n:
        return render_template("index.html", check="low", message="Too low!")
    if g > n:
        return render_template("index.html", check="high", message="Too high!")
@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = request.form["guess"]
    return redirect("/")
@app.route("/reset", methods=["POST"])
def reset():
    session.pop("secret_num")
    session.pop("guess")
    return redirect("/")

app.run(debug=True)