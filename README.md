# MQTTHandler

A Python logging handler using MQTT protocol.

## Installation

```sh
pip install mqtthandler
```

## Example usage

```py
import mqtthandler
import logging

mqtthdlr = mqtthandler.MQTTHandler('server.mqtt.com', 'topic/test')
mqtthdlr.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(mqtthdlr)
logger.setLevel(logging.INFO)

logging.info('test')  # Automatically connect to the MQTT server and send log message to MQTT topic
```

MQTTHandler will not wait for connected, you have to do it yourself.
E.g.

```py
mqtthdlr.initiate()   # Manually connect to the MQTT server
import time; time.sleep(3)   # A dirty way to wait for MQTT connected
logging.info('test')  # send log message to MQTT topic
```

MQTTHandler will create a thread to maintain the connection (automatically reconnecting if disconnected) itself. This will make your program never exit. You have to terminate MQTTHandler yourself to destroy the MQTTHandler thread.

```py
mqtthdlr.terminate()  # Destroy the MQTT connection
```

## API

### MQTTHandler

#### Constructor

```
MQTTHandler(host, topic, port=1883, keepalive=60, bind_address='', client_id='', clean_session=True, userdata=None, protocol=mqttc.MQTTv311, qos=0, retain=False)
```

Reference to [paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python/blob/master/README.rst).

#### Methods

```
initiate()
```
```
terminate()
```

Start/stop the handler.

```
max_inflight_messages_set(inflight)
```
```
message_retry_set(retry)
```
```
tls_set(ca_certs, certfile=None, keyfile=None, cert_reqs=ss.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
```
```
tls_insecure_set(value)
```
```
username_pw_set(username, password)
```
```
user_data_set(userdata)
```
```
will_set(topic, payload=None, qos=0, retain=False)
```

Reference to [paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python/blob/master/README.rst).
