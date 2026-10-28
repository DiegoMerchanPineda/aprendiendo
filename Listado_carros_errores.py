vehiculos = [
    {"marca": "Toyota", "precio": 45000000},
    {"marca": "Mazda", "precio": 62000000},
    {"marca": "Chevrolet", "precio": 35000000},
    {"marca": "BMW", "precio": "Consultar"},
    {"marca": "Kia"},
    {"marca": "Renault", "precio": None},
    {"marca": "Nissan", "precio": -5000000},
    {"marca": "Hyundai", "precio": 0}
]
def filtrar_vehiculos(lista_vehiculos,presupuesto):
    vehiculos_aptos=[]
    

    for vehiculo in lista_vehiculos:
        precio=vehiculo.get("precio")
        if precio is None or not isinstance(precio, (int, float)) or precio<=0:
            continue
        elif vehiculo["precio"] <=presupuesto:
            vehiculos_aptos.append(vehiculo)
    return vehiculos_aptos
    


assert(len(filtrar_vehiculos(vehiculos,50000000)))==2
assert(filtrar_vehiculos(vehiculos,30000000))==[]
assert(filtrar_vehiculos(vehiculos,35000000)[0]["marca"])=="Chevrolet"
    