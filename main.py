from operaciones import opera
import json
from pprint import pprint
db=opera()



def menu():
    while (True):
        print("****************************************")
        print("             MENU PRINCIPAL             ")
        print("Opciones:                               ")
        print("[1] - Listado de todos los tiquet       ")
        print("[2] - Agregar Tiquet                    ")
        print("[3] - Tiquet por sector                 ")
        print("[4] - Sumar Tarifa de los tiquets       ")
        print("[5] - Salir                             ")
        print("****************************************")
        opcion = input("[SISTEMA] - Ingrese una opcion: ")
        try:
            opcion = str(opcion)
            if opcion == "1":
                print("[SISTEMA] - LISTA DE TODOS LOS TIQUET:")
                Lista=db.lista()
                Lista=json.loads(Lista.decode('utf-8'))
                for x in Lista:
                    print("ID: {}".format(x["id"]))
                    print("Sector: {}".format(x["Sector"]))
                    print("Asiento: {}".format(x["Asiento"]))
                    print("Tarifa: {}".format(x["Tarifa"]))
                    print("****************************************")
            elif opcion == "2":
                print("[SISTEMA] - AGREGAR TIQUET:")
                id=input("Ingrese el ID: ")
                sector=input("Ingrese el sector: ")
                asiento=input("Ingrese el asiento: ")
                tarifa=input("Ingrese la tarifa: ")
                db.agregar(id,sector,asiento,tarifa)
                print("[SISTEMA] - TIQUET AGREGADO")
            elif opcion == "3":
                print("[SISTEMA] - FILTRO DE TIQUET POR SECTOR:")
                sector=input("Ingrese el sector: ") 
                Filtro=db.filtro(sector) #Filtro es una variable que contiene el resultado de la funcion filtro
                if(Filtro.decode() == 'error') :
                    print("[SISTEMA] - NO HAY TIQUETES PARA EL SECTOR")
                else:
                    Filtro=json.loads(Filtro.decode('utf-8')) #decodifica el json
                    for x in Filtro:
                        print("ID: {}".format(x["id"]))
                        print("Sector: {}".format(x["Sector"]))
                        print("Asiento: {}".format(x["Asiento"]))
                        print("Tarifa: {}".format(x["Tarifa"]))
                        print("****************************************")
            elif opcion == "4":
                print("[SISTEMA] - SUMAR TARIFA DE LOS TIQUET:")
                Suma=db.sumar()
                print(Suma.decode())
            elif opcion == "5":
                break
            else:
                print("[ERROR] - OPCION NO VALIDA")
        except ValueError:
            print("Opcion Invalida")
menu()            


