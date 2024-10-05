import datetime
str2=""
enco=str2.encode('unicode_escape')
str=str(enco,'utf-8')
l1=(datetime.datetime.now().hour)%0x5
l2=(datetime.datetime.now().day)%0x6
l3=(datetime.datetime.now().month)%0x7

l5=(datetime.datetime.now().year)%0x9
str=str.replace("5",f"{l1}")
str=str.replace("6",f"{l2}")
str=str.replace("7",f"{l3}")

str=str.replace("9",f"{l5}")
by=bytes(str,encoding='utf-8')
print(by.decode('unicode_escape'))
