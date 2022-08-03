string = "pythonist"
text = [] 
dict_ = {}
for i in string:
    text.append(i)
for i in text:
    num = text.count(i)
    dict_.setdefault(i,num)
print(dict_)
