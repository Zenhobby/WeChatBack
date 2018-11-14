# coding=utf-8
from flask import Flask,request
from time import time

import hashlib
import xml.etree.cElementTree as ET

application = Flask(__name__)

wechat_token="zenhobbystoken"
def check_signature(signature, timestamp, nonce):
    token = wechat_token
    tmp_arr = [token, timestamp, nonce]
    tmp_arr.sort()
    tmp_str = tmp_arr[0] + tmp_arr[1] + tmp_arr[2]
    sha1_tmp_str = hashlib.sha1(tmp_str).hexdigest()
    if (sha1_tmp_str == signature):
        return True
    else :
        return False

@application.route('/wechat/',methods = ['GET','POST'])
def respond():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')

    if request.method == 'GET':
        if check_signature(signature, timestamp, nonce)
            return echostr
        else :
            return 'Not Valid!'
    else :
        xml_recv = ET.fromstring(request.data)
        MsgType = xml_recv.find("MsgType").text
        ToUserName = xml_recv.find("ToUserName").text
        FromUserName = xml_recv.find("FromUserName").text
        replyContent = ""
        if (MsgType == "text"):
            replyContent = xml_recv.find("Content").text + " hello"
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime><![CDATA[%s]]></CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
        re_msg = (reply % (FromUserName, ToUserName, str(int(time.time())), replyContent))
        return re_msg

if __name__ == "__main__":
    application.run(host="0.0.0.0")
