import json
import time
import requests
import record_voice
from flask import Flask, request, render_template,jsonify
from flask_cors import CORS #크로스오리진 허용 매우중요
from STT_TTS import ST

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 서버로 데이터 던져줄때 한글깨져서 추가함 
cors = CORS(app) #크로스오리진 허용 매우중요



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET','POST'])
def test():
    
    if request.method == 'GET':
        return "성공"

    if request.method == 'POST':
        print("--------------------------------------------")
        value = request.form['message']
        print("----------------------------------------------")
        p.TTS(value)
        print("----------------------------------------------")
        p.Play_Sound("1111.mp3") # TTS
        time.sleep(1.0)
        p.Play_Sound("2.mp3") # 2초뒤에 말해주세요 음성 실행
        print("--------------------------------------")
        time.sleep(0.5)
        record_voice.record() #노인 음성녹음
        text = p.STT("get_voice.wav")  # 노인음성 STT
        print("---------------------------------------")
        return text ##여기에 음성을 텍스트로 바꿔서 리턴값 넣어주면댄다


if __name__ == '__main__':
      p=ST()
      app.run(host='192.168.1.50', port=5000, debug=True)