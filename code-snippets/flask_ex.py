from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greet():
    return "Hello!"

@app.route("/profile")
def profile():
    return render_template("home.html")

@app.route("/profile/<float:name>")   # For taking variables
def profile_name(name):
    print(type(name))
    return f"This is the profile page for {name}"

app.run(debug=True)