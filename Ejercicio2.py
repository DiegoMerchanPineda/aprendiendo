def list_palabras(palabras):
    diccionario1={}

    for palabra in palabras:
        if palabra in diccionario1:
            diccionario1[palabra]+=1
        else:
            diccionario1[palabra]=1

    return diccionario1
        
palabras1=["hola","como", "hola", "estas"]
print(list_palabras(palabras1))

