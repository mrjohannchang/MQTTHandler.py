# -*- coding: utf-8 -*-

import logging
import paho.mqtt.client as mqttc
import ssl

class MQTTHandler(logging.Handler):
  def __init__(
      self,
      host,
      topic,
      port=1883,
      keepalive=60,
      bind_address='',
      client_id='',
      clean_session=True,
      userdata=None,
      protocol=mqttc.MQTTv311,
      qos=0,
      retain=False):

    logging.Handler.__init__(self)

    self._topic = topic
    self._qos = qos
    self._retain = retain
    self._started = False
    self._host = host
    self._port = port
    self._keepalive = keepalive
    self._bind_address = bind_address

    self._mqttc = mqttc.Client(
        client_id=client_id,
        clean_session=clean_session,
        userdata=userdata,
        protocol=protocol)
    self._mqttc.connect_async(
        self._host,
        port=self._port,
        keepalive=self._keepalive,
        bind_address=self._bind_address)

  def __del__(self):
    try:
      self._mqttc.loop_stop()
    except:
      pass
    try:
      self._mqttc = None
    except:
      pass

  def emit(self, record):
    if not self._started:
      self._mqttc.loop_start()
      self._started = True
    try:
      msg = self.format(record)
      self._mqttc.publish(
          topic=self._topic,
          payload=msg,
          qos=self._qos,
          retain=self._retain)
      self.flush()
    except Exception:
      self.handleError(record)

  def loop_start(self):
    if not self._started:
      self._mqttc.loop_start()
      self._started = True

  def loop_stop(self):
    try:
      self._mqttc.loop_stop()
    except:
      pass
    finally:
      self._started = False

  def max_inflight_messages_set(self, inflight):
    self._mqttc.max_inflight_messages_set(inflight)

  def message_retry_set(self, retry):
    self._mqttc.message_retry_set(retry)

  def tls_set(
      self,
      ca_certs,
      certfile=None,
      keyfile=None,
      cert_reqs=ssl.CERT_REQUIRED,
      tls_version=ssl.PROTOCOL_TLSv1,
      ciphers=None):
    self._mqttc.tls_set(
        ca_certs,
        certfile=certfile,
        keyfile=keyfile,
        cert_reqs=cert_reqs,
        tls_version=tls_version,
        ciphers=ciphers)

  def tls_insecure_set(self, value):
    self._mqttc.tls_insecure_set(value)

  def username_pw_set(self, username, password=None):
    self._mqttc.username_pw_set(username=username, password=password)

  def user_data_set(self, userdata):
    self._mqttc.user_data_set(userdata)

  def will_set(self, topic, payload=None, qos=0, retain=False):
    self._mqttc.will_set(topic, payload=payload, qos=qos, retain=retain)
