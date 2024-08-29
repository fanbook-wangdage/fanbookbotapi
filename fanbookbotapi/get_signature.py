import hashlib
import urllib.parse
from collections import OrderedDict

#排序
def fixed_encodeURIComponent(value: str) -> str:
    return urllib.parse.quote(value, safe='~()*!.\'')

def get_signature(signature_map: dict, app_secret='dJcPo1dQHeMgDn1s8MQr',app_key='ww0qqc0UHMsFtDUhGbh0',platform='web') -> str:
    """生成签名

    Args:
        signature_map (dict): 待签名的请求体
        app_secret (str, optional): 失效后修改. Defaults to 'dJcPo1dQHeMgDn1s8MQr'.
        app_key (str, optional): 失效后修改. Defaults to 'ww0qqc0UHMsFtDUhGbh0'.
        platform (str, optional): 失效后修改. Defaults to 'web'.

    Returns:
        str: 签名字符串
    """
    # 对字段按键进行排序
    sorted_fields = OrderedDict(sorted(signature_map.items()))
    # 将键值对转换为字符串并连接
    chain = '&'.join(f"{key}={value}" for key, value in sorted_fields.items())
    # 在末尾添加appSecret
    chain = chain + '&' + app_secret
    # 对结果进行URL编码
    encoded_chain = fixed_encodeURIComponent(chain)
    # 生成md5签名
    signature = hashlib.md5(encoded_chain.encode('utf-8')).hexdigest()
    return signature

def get_key() -> str:
    """默认的key

    Returns:
        str: 返回默认的app_key
    """
    return 'ww0qqc0UHMsFtDUhGbh0'

def get_secret() -> str:
    """默认的secret

    Returns:
        str: 返回默认的app_secret
    """
    return 'dJcPo1dQHeMgDn1s8MQr'
