from decouple import config
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
ngrok_url = "https://e093e130.ngrok.io"
# paw_url = "https://heesoo1994.pythonanywhere.com" #ngrok은 서버 항시 오픈이 아니니까 사용하는 것임
data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}') #telegram에서 지원하는 setwebhook 기능을 이용하여 가상서버(ngrok)로 data를 넘김 / 주소는 보안성을 위해 token으로 지정해줌
# data = requests.get(f'{url}{token}/setwebhook?url={paw_url}/{token}') 
# 실행하는 순간 api 와 해당가상서버와 webhook이 됨
print(data.text)