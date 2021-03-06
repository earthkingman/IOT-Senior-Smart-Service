import paho.mqtt.client as mqtt

ab=0
# 클라이언트가 서버에게서 CONNACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("hello/world") # Topic /seoul/yuokok을 구독한다.


# 서버에게서 PUBLISH 메시지를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # ab=str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)   # MQTT 서버에 연결 # - 서버 IP '테스트를 위해 test.mosquitto.org'로 지정

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()