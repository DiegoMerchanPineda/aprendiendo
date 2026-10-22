#List Comprenhensions

# Dada palabras = ["Hola", "MUNDO", "Python"], crea una lista con todas en minúsculas.
palabras = ["Hola", "MUNDO", "Python"]
new_list=[]
for i in palabras:
    
    new_list.append(i.lower())

print(new_list)

new_list2=[i.lower() for i in palabras]
gen = (i.lower() for i in palabras)



# Dada numeros = [5, 12, 3, 20, 8], crea una lista solo con los mayores que 7.
numeros = [5, 12, 3, 20, 8]
numeros_list=[]
for i in numeros:
    if i>7:
        numeros_list.append(i)

numeros_list2=[i for i in numeros if i>7]

print(numeros_list2)


# Dada palabras = ["sol", "computador", "mar", "teclado"], crea una lista con las palabras de más de 3 letras. Pista: len().
palabras = ["sol", "computador", "mar", "teclado"]
new_palabras=[]

for i in palabras:
    if len(i)>3:
        new_palabras.append(i)

new_palabras2=[i for i in palabras if len(i)>3]

print(new_palabras2)

# Aplícalo a tu proyecto: en tu contador de palabras, usa una comprensión para pasar lista_palabras a minúsculas. Así resuelves de paso el cambio 1 (Hola hola HOLA
