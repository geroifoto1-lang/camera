import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/owner")
def owner():
    return """
    <h2>Страница владельца</h2>
    <p>Удалённая передача видео пока не подключена.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
