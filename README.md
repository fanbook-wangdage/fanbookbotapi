# 开始使用

这里使用getme做示例

```python
import fanbookbotapi

print(fanbookbotapi.getme('123').text)
```  

**1.2.2更改：发送消息函数添加参数add_Key，为了防止不添加键盘时消息出现边框，如果你需要添加键盘，请将其设置为True，否则不用管**  

# 支持的api

## bot api

- getme(token)

```
获取bot的信息
```

- sendmessage()

```
发送消息
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
    token (str): botToken
sendmessage(token='',chatid=0,biaoti="标题",ik=[[{"text":"下一页","callback_data":"{\"type\":\"next\",\"index\":2,\"msg\":\"114514\"}"}]],text='文本',biaoticolor='ffe4e4',type="card",shade=['ff764a','ffb39aff'],backgroundColor='ddeeff00',getjson=False) -> requests.models.Response|str:
```

- getPrivateChat(token,userid)  

```
创建私聊频道
Args:
    token (str): botToken
    userid (int): 用户长id
Returns:
    requests.models.Response: requests请求对象
    {"ok":true,"result":{"id":510639729457618944,"guild_id":0,"type":"private","channel_type":3}}
    返回中，id代表频道id
```

- bot_websocket()

```
fanbook bot websocket接口
Args:
    token (str): bot token
    onOpen (function): ws连接成功回调
    onMessage (function): ws收到消息回调
    onError (function): ws错误回调
    onClose (function): ws关闭回调
    log_level (str, optional): 日志等级. Defaults to "DEBUG".
```

## 用户api

> 用户api仅供学习研究使用，使用造成的后果与作者无关，严禁违法、违规使用

- send_user_message()

```
请求代码由WrunDorry提供
使用userapi发送消息

    Args:
        user_token (str, optional): 用户token和bot token二选一
        bot_token (str, optional): bot token和user token二选一
        text (str, optional): 消息体. Defaults to '{\"type\":\"text\",\"text\":\"test\",\"contentType\":0}'.
        decs (str, optional): 消息预览文本. Defaults to 'test'.
        channel_id (str, optional): 频道id. Defaults to '123456'.
        guild_id (str, optional): 服务器id. Defaults to '123456'.
        key (str, optional): api_key，默认留空. Defaults to ''.
        secret (str, optional): api_secret，默认留空. Defaults to ''.
        transaction (str, optional): 请求的唯一id，一般调试使用. Defaults to '73460be6-e295-4828-8750-01022533b9f0'.
        log_level (str, optional): 日志等级. Defaults to 'DEBUG'.

    Returns:
        requests.models.Response: 返回响应
```