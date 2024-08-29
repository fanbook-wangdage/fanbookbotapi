apiurl='https://a1.fanbook.mobi/api/bot/'
apilist={
    'getme':apiurl+'getMe'
}

from .api import *
from .userapi import *
from .get_signature import *

__all__ = ['getme','sendmessage','getPrivateChat','send_user_message','get_signature']