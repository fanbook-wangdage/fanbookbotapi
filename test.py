import fanbookbotapi

token=''
print(fanbookbotapi.getme(token).text)
print(fanbookbotapi.sendmessage(token,chatid=433212507046281216).text)
print(fanbookbotapi.getPrivateChat(token,userid=389320179948986368).text)