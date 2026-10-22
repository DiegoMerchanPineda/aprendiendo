inventario = {
    "leche": 10,
    "pan": 20,
    "huevos": 30,
    "queso": 5,
    "arroz": 15
}

def generar_reporte(inventario):
    total_unidades=0
    productos_menos_10=set()
    producto_mayor= ""
    cantidad_mayor=-1

    for key,value in inventario.items():
        total_unidades+=value

        if value<10:
            productos_menos_10.add(key)

        if value>cantidad_mayor:
            cantidad_mayor=value
            producto_mayor=key  

        

    

    
    return f"""Total unidades: {total_unidades}
    productos con pocas unidades {productos_menos_10}
    producto con mas unidades:{producto_mayor},{inventario[producto_mayor]}"""


primero=generar_reporte(inventario)


print(primero)