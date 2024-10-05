import datetime
str2=""
enco=str2.encode('unicode_escape')
str=str(enco,'utf-8')
l1=(datetime.datetime.now().hour)%0xff
l2=(datetime.datetime.now().day)%0xff
l3=(datetime.datetime.now().month)%0xff

l5=(datetime.datetime.now().year)%0xff
str=str.replace(f"{l5}","9")

str=str.replace(f"{l3}","7")
str=str.replace(f"{l2}","6")
str=str.replace(f"{l1}","5")
by=bytes(str,encoding='utf-8')
print(by.decode('unicode_escape'))
