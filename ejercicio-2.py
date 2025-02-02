listas = [1,2,3,4,5]
print (listas)
print (listas[0])
print(listas[1:4])
print(listas[:3])
print(listas[2:])
print(listas[0:4:2])
print(listas[-1])
print(listas[-3])
print(listas[::-1])
print(listas[-1-4])
print(listas[-4-1])
print(listas[-1:-4])
print(listas[-4:-1])

listas[1:3]=[7,8]
print(listas)
listas.insert(-1,9)
print(listas)
listas.insert(20,3)
print(listas)
listas.append(6)
print(listas)

listas.remove(9) # Elimina el numero 9
print(listas)
listas.pop(1) # Elimina el numero
listas.pop(0) # se usa para eliminar y devolver un elemento de una lista en una posición específica.
print(listas)

listas.clear()
print(listas)

'''
Listas.
    insert
    append
    remove
    pop
    clear
    extend
    reverse
    sort
    index
    
    del listas
    print(listas)
'''


listas1=[1,2,3]
listas2=[4,5,6]
print(listas1)
print(listas2)
listas1.extend(listas2)
print(listas1)
a = ""

for i in listas1:
    a += str (i)+ " "

print(a)


listas3=[2,7,10,1,5]
listas3.sort()
print(listas3)
listas3.sort(reverse=True)
print(listas3)
print(listas3.index(10))

'''
Hacer un programa que nos muestre el arreglo de texto y el menu nos muestre las opciones 
de métodos de la clase lista 

al principio el arreglo vacio
validar si la opcion es posible
'''