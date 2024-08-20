import requests,json
from .apilist import *

def getme(token:str) ->requests.models.Response:
    """获取bot信息

    Args:
        token (str): bot的token

    Returns:
        requests.models.Response: requests请求对象
    """
    r=requests.get(apiurl+token+apilist['getme'])
    return r

def sendmessage(token='',chatid=0,biaoti="标题",add_Key=False,ik=[[{"text":"下一页","callback_data":"{\"type\":\"next\",\"index\":2,\"msg\":\"114514\"}"}]],text='文本',biaoticolor='ffe4e4',type="card",shade=['ff764a','ffb39aff'],backgroundColor='ddeeff00',getjson=False) -> requests.models.Response|str:
    """发送消息

    Args:
        token (str, optional): botToken. Defaults to ''.
        chatid (int, optional): 频道id. Defaults to 0.
        biaoti (str, optional): 卡片标题. Defaults to "标题".
        ik (list, optional): 自定义键盘. Defaults to [[{"text":"下一页","callback_data":"{\"type\":\"next\",\"index\":2,\"msg\":\"114514\"}"}]].
        text (str, optional): 正文内容，如果是card模式，换行符为  4个反斜线n. Defaults to '文本'.
        biaoticolor (str, optional): 弃用，默认即可. Defaults to 'ffe4e4'.
        type (str, optional): card(内置卡片)/fanbook(特殊消息解析模式)/text(纯文本). Defaults to "card".
        shade (list, optional): 标题背景颜色，如果配置两项就是渐变色. Defaults to ['ff764a','ffb39aff'].
        backgroundColor (str, optional): 标题文本颜色. Defaults to 'ddeeff'.
        getjson (bool, optional): 设置为True就是只返回编码完成的json，不请求. Defaults to False.
        add_Key (bool, optional): 是否添加键盘. Defaults to False.

    Returns:
        requests.models.Response|str: requests请求对象|编码完成的json
    """
    if len(shade)==1:
        color1,color2=shade[0],shade[0]
    else:
        color1,color2=shade[0],shade[1]
        
    url = apiurl+token+apilist['sendmessage']
    if type=="card":
        text1="{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\""+str(color1)+"\\\",\\\""+str(color2)+"\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\""+str(biaoti)+"\\\",\\\"style\\\":{\\\"color\\\":\\\"#"+str(biaoticolor)+"\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\""+backgroundColor+"\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\""+str(text)+"\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}"
        pm="Fanbook"
    elif type=='fanbook':
        pm='Fanbook'
        text1=text
    else:
        text1=text
        pm=None
    #print(text1)
    d={
    "chat_id": int(chatid),
    "text": text1,
    "parse_mode": pm
    }
    if add_Key:
        #添加"reply_markup": {
        #"inline_keyboard": ik
    #}  
        d['reply_markup']={
            "inline_keyboard": ik
        }
    payload=json.dumps(d)
    if getjson==False:
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    else:
        return payload

def getPrivateChat(token:str,userid:int) ->requests.models.Response:
    """创建私聊频道

    Args:
        token (str): botToken
        userid (int): 用户长id

    Returns:
        requests.models.Response: requests请求对象
    """
    url=apiurl+token+apilist['getPrivateChat']
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({
        "user_id":int(userid)
        })
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    return postreturn