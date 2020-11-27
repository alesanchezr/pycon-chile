from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

app.run(host='0.0.0.0', port=3000, debug=True)