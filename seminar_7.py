c = []
a = (input('введите сопелку  ')).split()

for i in range(len(a)):
    c.append(len(list(filter(lambda x: x in 'аоеиёыуэюя', a[i]))))
   
print((lambda x: 'Парам пам-пам' if len(set(x)) == 1 else 'Пам парам')(c))

