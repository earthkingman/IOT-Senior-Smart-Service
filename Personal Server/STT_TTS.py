
import time
import pygame
import base64
import requests
import os
import sys
import urllib.request

class ST:
    #생성자
    def __init__(self):
        print("객체가 생성되었습니다.")
        

    #Text to Speech
    def TTS(self,text):
        
        # Api setup
        client_id = ""
        client_secret = ""
        encText = urllib.parse.quote(text)
        data = "speaker=mijin&speed=0&text=" + encText
        url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
        request.add_header("X-NCP-APIGW-API-KEY", client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if (rescode == 200):
            print("TTS mp3 저장")
            response_body = response.read()
            with open('1111.mp3', 'wb') as f:
                f.write(response_body)
        else:
            print("Error Code:" + rescode)



    def STT(self,audioFilePath):
        # 오디오 파일 열기
        print("SPEECH TO TEXT API 작동")
        audio_file = open(audioFilePath, "rb")
        audio_src = base64.b64encode(audio_file.read()).decode("utf8")
        audio_file.close()
        # Api setup
        client_id = ""
        client_secret = ""
        lang = "Kor"  # 언어 코드 ( Kor, Jpn, Eng, Chn )
        url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
        data = open(audioFilePath, 'rb')
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(url, data=data, headers=headers)
        rescode = response.status_code
        if (rescode == 200):
            print("SPEECH TO TEXT API 정상종료")
        else:
            print("SPEECH TO TEXT API ERROR 발생:" + response.text)
        return response.text


        # 노래재생
    def Play_Sound(self,music):
            music_file = music
            freq = 16000  # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
            bitsize = -16  # signed 16 bit. support 8,-8,16,-16
            channels = 1  # 1 is mono, 2 is stereo
            buffer = 2048  # number of samples (experiment to get right sound)

            # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
            pygame.mixer.init(freq, bitsize, channels, buffer)
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()

            clock = pygame.time.Clock()
            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
