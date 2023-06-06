def saludo():
    print("Menu Comida FadFood.")

saludo()     

def menu():
    opcion_valida = False
    while not opcion_valida:
        print("""1 Primera opcion.\t 2 Primera opcion.\t 3 Primera opcion.\t 4 Primera opcion.""")
        opcion = input("Seleccione una opcion: ")
        if opcion != "1" and opcion != "2" and opcion !="3" and opcion !="4":
          print("Opcion no valida")
        else:
          opcion_valida = True

    return opcion

opcion_seleccionada = menu()
print(f"opcion seleccionada: {opcion_seleccionada}")