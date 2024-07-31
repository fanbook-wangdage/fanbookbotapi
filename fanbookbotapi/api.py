import requests,json
from .apilist import *

def getme(token:str) ->object:
    """获取bot信息

    Args:
        token (str): bot的token

    Returns:
        object: requests请求对象
    """
    r=requests.get(apiurl+token+apilist['getme'])
    return r

def sendmessage(token='',chatid=0,biaoti="标题",ik=[[{"text":"下一页","callback_data":"{\"type\":\"next\",\"index\":2,\"msg\":\"114514\"}"}]],text='文本',type="card") -> object:#发送数据
    r"""
    发送消息
    Args:
        chatid (int): 频道id
        biaoti (str): 标题
        ik (list): 键盘列表
        text (str): 正文文本
        type (str): 类型，card(内置md消息卡片\\\\n是换行)或text(文本)或fanbook(自定义特殊消息)
        
    Returns:
        obj: 返回requests请求对象
    """
    if biaoti=='获取成功':
        color='#11A675'
    else:
        color='FF6100'
    url = apiurl+token+apilist['sendmessage']
    if type=="card":
        text1="{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\""+biaoti+"\\\",\\\"style\\\":{\\\"color\\\":\\\""+color+"\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,8,0,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\""+text+"\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}"
        pm="Fanbook"
    elif type=='fanbook':
        pm='Fanbook'
        text1=text
    else:
        text1=text
        pm=None
    payload = json.dumps({
    "chat_id": int(chatid),
    "text": text1,
    "parse_mode": pm,
    "reply_markup": {
        "inline_keyboard": ik
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response