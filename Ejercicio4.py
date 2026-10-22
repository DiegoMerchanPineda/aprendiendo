def contar_palabras(palabras):
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


# 1. Leer el archivo
try:
    with open("texto2.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("No encontre el archivo")
else:
        # 2. Convertir el texto en lista de palabras
    lista_palabras = contenido.split()

    # 3. Contar
    resultado = contar_palabras(lista_palabras)

    # 4. Escribir el resultado en otro archivo
    with open("resultado.txt", "w") as f:
        f.write(str(resultado))

    print(resultado)
