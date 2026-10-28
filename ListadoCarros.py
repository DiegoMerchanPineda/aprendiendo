vehiculos = [
    {"marca": "Toyota", "precio": 45000000},
    {"marca": "Mazda", "precio": 62000000},
    {"marca": "Chevrolet", "precio": 35000000},
    {"marca": "BMW", "precio": 120000000},
    {"marca": "Kia", "precio": 55000000}
]

def filtrar_vehiculos(lista_vehiculos,presupuesto):
    vehiculos_aptos=[]
    for vehiculos in lista_vehiculos:
        if vehiculos["precio"] <=presupuesto:
            vehiculos_aptos.append(vehiculos)
        return vehiculos_aptos
    


print(filtrar_vehiculos(vehiculos,40000000))
    