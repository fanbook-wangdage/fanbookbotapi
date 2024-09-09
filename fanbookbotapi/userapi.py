import json
import time
import uuid
import requests
import logging
import coloredlogs
# 创建日志记录器
logger = logging.getLogger(__name__)
from .get_signature import get_signature, get_key, get_secret
from .api import getme

def send_user_message(user_token='',bot_token='',text='{\"type\":\"text\",\"text\":\"test\",\"contentType\":0}',decs='test',channel_id='123456',guild_id='123456',key='',secret='',transaction='73460be6-e295-4828-8750-01022533b9f0',log_level='DEBUG') ->requests.models.Response:
    """使用userapi发送消息

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
    """
    # 配置 coloredlogs
    coloredlogs.install(level=log_level, logger=logger)
    url = f"https://web.fanbook.cn/api/a1/api/message/clientSend/{guild_id}/{channel_id}" # 社区ID/频道ID
    auth=user_token
    
    t=int(time.time() * 1000)
    nonce=str(uuid.uuid4())
    
    if key=='':app_key=get_key()
    else:app_key=key
    
    if secret=='':app_secret=get_secret()
    else:app_secret=secret
    
    #如果是bot token，则获取用户token
    if bot_token!='':
        try:
            auth=json.loads(getme(bot_token).text)
            logger.debug(str(auth))
            auth=auth['result']['user_token']
        except:
            try:
                logger.error(getme(bot_token).text)
            except:
                pass
            logger.critical('bot_token获取用户token失败')
            #引发token error
            raise Exception('bot_token error')
    else:
        auth=user_token
    
    '''
    WrunDorry 2024-08-29
    '''
    r=json.dumps({
        "channel_id":channel_id,
        "guild_id":guild_id,
        "content":text,
        "desc":decs,
        "nonce":nonce,
        "token":auth,
        "transaction":transaction
    })
    common_fields = {
        "Nonce": nonce,
        "Timestamp": t,
        "Authorization": auth,
        "AppKey": app_key,
        "RequestBody": r,
        "Platform": 'web'
    }

    signature = get_signature(common_fields, app_secret, app_key) # 生成签名
    logger.info(f"Generated Signature: {signature}")

    headers = {
    "Nonce": nonce,
    'appkey': app_key,
    'authorization': auth,
    'language': 'zh-CN',
    'platform': 'web',
    'priority': 'u=1, i',
    'signature': signature,
    'timestamp': str(t),
    'content-type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=r) # 发送请求

    logger.debug(str(response.text))
    data=json.loads(response.text)
    if data['action']=='error':
        logger.warning('发送消息失败')
    else:
        logger.info('发送消息成功')
    return response
