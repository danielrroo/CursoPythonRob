#Sucesión que converge al num 'e'

#e = lim cuando n tiende a infinito de (1+1/n)elevadoa la n
e=0
for i in range(1,1000):
    e=pow((1+1/i),i)
    print(e)

