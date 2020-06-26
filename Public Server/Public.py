#-*-coding: utf-8 -*-

import json
import requests
import model #DB
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template,jsonify
from flask_cors import CORS #크로스오리진 허용 매우중요
import time

app = Flask(__name__, static_folder='./static')

db = model.Database() #디비 
app.config['JSON_AS_ASCII'] = False  # 서버로 데이터 던져줄때 한글깨져서 추가함 
cors = CORS(app) #크로스오리진 허용 매우중요

url = "http://110.46.100.33:5000/test"

@app.route('/') #공공서버 개인서버 STT TTS 통신 테스트
def index():
    lists = db.select("silver")    
    ## 총노인 위험 노인 
    ## 노인정보 
    return render_template('main.html',show=lists)

@app.route('/test', methods=['GET','POST']) #공공서버 개인서버 STT TTS 통신 테스트
def test():
    
    if request.method == 'GET':
        return "성공"
         
    if request.method == 'POST':
        value = request.form['messsage']      
        
        db.insert("msg",1,1,value,1)
        row=db.select("msg")
        print(row)
        return render_template('chat.html',show=row)


@app.route('/detail', methods=['GET','POST']) # 노인 상세 페이지
def detail():
    return render_template('detail.html')



@app.route('/dht', methods=['GET','POST']) # 온습도 정보 상세페이지
def dht():
      time.sleep(1.5)
      if request.method == 'POST':
        value = request.form['s_id']
        row=db.select_s_id("dht",value)
        return jsonify(row)


@app.route('/fire', methods=['GET','POST']) # 화재 정보 메인페이지
def fire():
      db = model.Database()
      time.sleep(0.5)
      if request.method == 'POST':
        row=db.distinctselect("fireDetect")
        return jsonify(row)




@app.route('/fireremove', methods=['GET','POST']) # 화재 정보 삭제 
def fireremove():
      time.sleep(3.5)
      if request.method == 'POST':
        s_id = request.form['s_id']
        db.delete_fire("fireDetect",s_id)
        row=db.distinctselect("fireDetect")
        return jsonify(row)



@app.route('/info', methods=['GET','POST']) # 노인 정보 상세페이지
def info(): 
      time.sleep(0.5)
      if request.method == 'POST':
        s_id = request.form['s_id']
        row=db.select_s_id("silver",s_id)
        return jsonify(row)


@app.route('/danger') # 위험 노인 페이지 
def danger():
    return render_template('danger.html')


@app.route('/form') #명주가 만든 노인 입력 페이지 
def form():
    return render_template('form.html')



@app.route('/silverdata', methods=['post']) #노인 정보 입력 다 하고 디비 저장
def silverData():
    time.sleep(1)
    s_name = request.form.get('s_name')
    s_birth = request.form.get('s_birth')
    s_sex = request.form.get('inline-radios')
    s_phone = request.form.get('s_phone')
    s_postcode = request.form.get('postcode')
    s_address = request.form.get('address')
    s_detailAddress = request.form.get('detailAddress')
    s_extraAddress = request.form.get('extraAddress')
    s_image = request.files['file']
    s_image = "c://image/image.jpg"
    s_info = request.form.get('s_info')
    s_address = s_address + s_detailAddress + s_extraAddress

    db.insert_register(s_name, s_birth, s_address, s_image, s_info, s_phone)
    lists = db.select("silver")
    return render_template("/main.html",show=lists)


    
@app.route('/calendar')  #동원이가 만든 달력 페이지
def calendar():
    return render_template('calendar.html')


@app.route('/chat2') # ajax로 만든거 이게 진짜 채팅 페이지임 페이지만 열어주고 채팅에서 바로 ajax_chat으로 ajax요청함
def chat2():
    return render_template('chat2.html')



@app.route('/ajax_chat2', methods=['GET','POST'])  # ajax 채팅
def ajax_chat2():
       time.sleep(5)
       if request.method == 'POST': # chat2 페이지에서 채팅 보내기 버튼누르면 갱신    
            s_id  =  request.form['s_id']                                                   
            row=db.select_s_id("msg",s_id)
            return jsonify(row) # 무조건 jsonifiy로 응답해줘야함 그래야 type오류안남




@app.route('/ajax_chat', methods=['GET','POST'])  # ajax 채팅
def ajax_chat():
       time.sleep(2.5)
       if request.method == 'POST': # chat2 페이지에서 채팅 보내기 버튼누르면 갱신 
            if request.form['message']!='':         #채팅데이터가없으면 DB에 저장안함 
                value = request.form['message']   #메세지 받아오기
                s_id  =  request.form['s_id']       # 노인 구분하는 id   main.html 참고하면댐
                print("부분 메세지 확인 "+str(s_id))  
                db.insert("msg",1,int(s_id),value,2)  #복지사id, 노인id, 채팅내용 ,m_type ->2이면 복지사가보낸거 1이면 노인이말한거
                                                        # 그리고 s_id int로 형변환 안하면 오류난다이~
            row=db.select_s_id("msg",s_id)
            return jsonify(row) # 무조건 jsonifiy로 응답해줘야함 그래야 type오류안남

       if request.method == 'GET':  # chat2 페이지 열리자 말자 바로 채팅 갱신
            time.sleep(3)
            s_id =request.args.get('s_id')   #노인 구분하는 id
            print("전체 메세지 확인 "+str(s_id))
            row=db.select_s_id("msg",s_id)
            return jsonify(row) # 무조건 jsonifiy로 응답해줘야함 그래야 type오류안남

 
@app.route('/speech', methods=['GET','POST']) #http 통신구현
def speech():
       if request.method == 'POST': 
            time.sleep(4)
            if request.form['message']!='':                  
                value = request.form['message']   
                s_id  =  request.form['s_id']               
                data = {'message': value } 
                res = requests.post(url, data=data)
                print(res.text)
                if res.text!='':
                    db.insert("msg",1,int(s_id),res.text,1)
                return jsonify("텍스트 개인서버로  보내기 성공") # 무조건 jsonifiy로 응답해줘야함 그래야 type오류안남

 
@app.route('/graph', methods=['GET','POST'])  # 그래프 그려주는 사이트
def graph():       
       time.sleep(2)
       if request.method == 'POST':
           db = model.Database()
           s_id  =  request.form['s_id']  
           row=db.select_s_id("heartRate",s_id)
           return jsonify(row) 
  

if __name__ == '__main__':
      app.run(host=' 0.0.0.0', port=5000, debug=True)
    #   app.run(host=' 127.0.0.1', port=5000, debug=True)
