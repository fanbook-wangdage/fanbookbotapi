apiurl='https://a1.fanbook.mobi/api/bot/'
apilist={
    'getme':apiurl+'getMe'
}

from .api import *

__all__ = ['getme','sendmessage','getPrivateChat']