# урок о типах данных:
#   типы данных бывают ИЗМЕНЯЕМЫМИ и НЕИЗМЕНЯЕМЫМИ
#       НЕИЗМЕНЯЕМЫЕ 
#           целые числа (int),
#           числа с плавающей точкой (float), 
#           комплексные числа (complex),    
#           логические переменные (bool), 
#           кортежи (tuple), 
#           строки (str) и 
#           неизменяемые множества (frozen set).
#       ИЗМЕНЯЕМЫЕ
#           списки (list),
#           множества (set), 
#           словари (dict).
# 

a = 3           #создается переменная "а" и объект с значением "3", к объекту ссылается переменая
print(a)        #выводим значение объекта на который ссылается переменная "а"
print(id(a))    #выводим идентификатор объекта со значением "3", через ссылку со стороны переменной а
print(type(a))  #выводим тип данных объекта

a = 2           #создаем новый объект со значением "2" и изменяем ссылку
print(a)        #выводим значение объекта на который ссылается переменная "а"
print(id(a))    #выводим идентификатор объекта, через ссылку со стороны переменной а
print(type(a))

# мы видим, что изменился идентификатор и значение, 
# т.е. создался новый объект и изменилась ссылка, а старый объект удалился 
# это означает, что тип данных "int" является ИЗМЕНЯЕМЫМ 


b = [1,2]       #создаем объект с типом данных list и переменную "b", которая ссылается на объект
print(b)        #выводим значение объекта на который ссылается переменная "а"
print(id(b))    #выводим идентификатор объекта, через ссылку со стороны переменной b
print(type(b))  #выводим тип данных объекта


b = [3,4]
print(b)
print(id(b))
print(type(b))

#Мы видим, что значение объекта изменилось, а идентификатор нет. 
#Это означает, что тип данных "list" НЕИЗМЕНЯЕМЫЙ
