from flask import Flask, render_template, request
from decouple import config
import requests
import random
import re
import time

app = Flask(__name__)

token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')  # .env에서 들고 오는 정보
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
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')# {}안 변수들은 여기서 정의한 변수들
    return render_template('send.html') #입력정보는 해당 url로 넘겨줘서, 메세지를 받을 수 있지만 로컬 상에서 돌아가기 때문에 표시할 영역이 없어 에러가 발생한다!


@app.route(f'/{token}', methods=["POST"]) #token 값을 사용한 이유는 접근성을 제한하기 위함 / post method를 사용하여 무조건적인 접근방지 (복잡하게 하여 토큰노출을 막는다)
def telegram(): #어떻게 응답과 데이터를 보내는지 궁금함
    KAKAO_KEY = '3d28d42b5f4d318cfe6bee77bb929850'
    headers = {'Authorization': 'KakaoAK {}'.format('KAKAO_KEY')}
    data = request.get_json()
    text = data['message']['text']
    who_id = data['message']['chat']['id']
    print(text)
    print(who_id)
    print(request.get_json()) #내가 봇에게 메세지보내면 제이슨의 형태로 출력됨
    if text == "안녕" :
        return_text = "안녕하세요"
    elif re.search("로또" , text) : #text안에 '로또'라는 문자열을 탐색 한다면~
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6)) #sroted: 오름차순 정렬
    elif re.search("번역" , text) :
        return_text = "번역 문장을 타이핑하세요"
        requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}')
        
        # time.sleep(1)
        # if return text ==  "번역 문장을 타이핑하세요"
        # input_text = text
        # requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={input_text}')
        # #GO
        # return_text = "언어(키값)종류를 선택하세요"
        # requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}')
        # time.sleep(60)
        # Input_key = 
        # #GO
        # Input_key에 대한 input_text를 번역
        # requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={번역본}')

    else :
        return_text = "현재 지원하지 않는 문장입니다."
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}') #return_text로 봇이 나에게 응답함

        
        
        
     
    return "ok", 200  # 한 번의 요청에 대한 한 번의 응답을 하기 위함 (무조건적인 응답 방지)


if __name__ == ("__main__"):
    app.run(debug=True)
