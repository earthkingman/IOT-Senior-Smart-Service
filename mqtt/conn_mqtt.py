import paho.mqtt.client as mqtt
from db_conn import Database

# 클라이언트가 서버에게서 CONNACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("fire")
    client.subscribe("dht")
    client.subscribe("heart_rate")


# 서버에게서 PUBLISH 메시지를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):

    get_topic = str(msg.topic)
    get_msg = str(msg.payload)

    #print(type(get_topic))
    #print(get_topic)

    db_connect = Database()
    #print("conn ok")

    if get_topic == 'dht':
        temp = get_msg[2:6]
        humi = get_msg[6:10]
        db_connect.insert_dht("dht", 1, 1, temp, humi)
        print("insert data : " + temp, humi)

    elif get_topic == 'fire' and len(get_msg) > 4:
        text = "화재감지!!"
        db_connect.insert_fire("fireDetect", 1, 1, text)
        print(text)
        print("insert data")

    elif get_topic == 'heart_rate' and len(get_msg) > 4:
        rate = get_msg[2:-1]
        db_connect.insert_heartRate("heartRate", 1, 1, str(rate))
        print("insert heart rate : " + str(rate))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)   # MQTT 서버에 연결 # - 서버 IP '테스트를 위해 test.mosquitto.org'로 지정
client.loop_forever()