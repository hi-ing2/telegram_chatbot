from flask import Flask,render_template, request
from decouple import config
import requests

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID') #.env에서 들고 오는 정보
url = "https://api.telegram.org/bot"


@app.route('/')
def hello():
    return "Hello world!"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}') # {}안 변수들은 여기서 정의한 변수들
    return render_template('send.html')


if __name__ == ("__main__"):
    app.run(debug=True)
