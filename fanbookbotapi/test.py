import botWs
token = "YOUR_TOKEN"
def onMessage(ws,message):
    pass
def onError(ws):
    pass
def onClose(ws):
    pass
def onOpen(ws):
    pass
botWs.bot_websocket(token,onOpen=onOpen,onMessage=onMessage,onError=onError,onClose=onClose)