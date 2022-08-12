list_ = ['--X', 'X--', 'X++', '++X']
X = 0
for i in list_:
    if i.count('-') == 2:
        X-=1
    elif i.count('+') == 2:
        X+=1
print(X)