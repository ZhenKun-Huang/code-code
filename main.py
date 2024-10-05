import datetime
str2="请输入加密内容"
enco=str2.encode('unicode_escape')
print(enco)
str=str(enco,'utf-8')
l1=(datetime.datetime.now().hour)%0x18
l2=(datetime.datetime.now().day)%0x1f
l3=(datetime.datetime.now().month)%0xc
print(type(enco))
print(str)
str=str.replace("5",f"{l1}")
str=str.replace("6",f"{l2}")
str=str.replace("7",f"{l3}")
by=bytes(str,encoding='utf-8')
print(str)
print(by.decode('unicode_escape'))
