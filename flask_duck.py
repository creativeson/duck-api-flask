from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def index():
    # 從 session 或其他存儲中獲取當前主題
    theme = request.cookies.get('theme', 'light')

    if request.method == "POST":
        # 切換主題
        theme = 'dark' if theme == 'light' else 'light'
        response = redirect(url_for('index'))
        response.set_cookie('theme', theme, max_age=30*24*60*60)  # 保存30天
        return response

    # 獲取隨機鴨子圖片
    url = "https://random-d.uk/api/v2/quack"
    response = json.loads(requests.get(url).text)
    duck_jpg = response['url']

    return render_template("index.html", theme=theme, pic=duck_jpg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
