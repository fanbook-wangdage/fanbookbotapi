# 开始使用

这里使用getme做示例

```python
import fanbookbotapi

print(fanbookbotapi.getme('123').text)
```

# 支持的api

- getme(token='bot token')
- sendmessage(token='bot token',chatid=0,biaoti="标题",ik=[[{"text":"下一页","callback_data":"{\"type\":\"next\",\"index\":2,\"msg\":\"114514\"}"}]],text='文本',type="card")

```
发送消息
Args:
    chatid (int): 频道id
    biaoti (str): 标题(type为card时的卡片标题)
    ik (list): 键盘列表
    text (str): 正文文本
    type (str): 类型，card(内置md消息卡片\\\\n是换行)或text(文本)或fanbook(自定义特殊消息)
    
Returns:
    str: 返回requests请求对象
```