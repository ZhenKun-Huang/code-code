import datetime
str2=""
enco=str2.encode('unicode_escape')
str=str(enco,'utf-8')
l1=(datetime.datetime.now().hour)%0xf
l2=(datetime.datetime.now().day)%0xf
l3=(datetime.datetime.now().month)%0xf

l5=(datetime.datetime.now().year)%0xf
str=str.replace(f"{l5}","9")

str=str.replace(f"{l3}","7")
str=str.replace(f"{l2}","6")
str=str.replace(f"{l1}","5")
by=bytes(str,encoding='utf-8')
print(by.decode('unicode_escape'))
