#Progrma control de stock mercaderia electrica
#------------------------------------------------------------------
# Programa de control de stock
#------------------------------------------------------------------
#------------------------------------------------------------------
# Importar las Librerías:
#------------------------------------------------------------------
from colorama import init, Fore, Style #Librería para dar color
init( autoreset = True )
from os import system 
import json # Librería para usar archivos JSON
from getpass_asterisk.getpass_asterisk  import  getpass_asterisk # Librería utilizada para ocultar usuando "*"
import sys # Librería utilizada para salir del proceso con el metodo exit
import time # Libreria para retrasar unos segundos la ejecucución
#-----------------------------------------------
# Función limpiar
#-----------------------------------------------
def limpiar():# Limpieza de pantalla
    system("cls")
#-----------------------------------------------
# Función de ingreso
#-----------------------------------------------
def login():
    intentos = 3  # Número de intentos permitidos de ingreso

    while intentos > 0 :
# Solicitar nombre de usuario y contraseña
        usuario_i = getpass_asterisk(Fore.BLUE + Style.BRIGHT + "Ingrese nombre de usuario: ")
        password_i = getpass_asterisk(Fore.BLUE + Style.BRIGHT + "Ingrese contraseña: ")
        
# Buscar el usuario en el archivo JSON
        
        usuario_correcto = False
        for user in listaUsuarios:
            if user["usuario"] == usuario_i  and user["password"] == password_i:
                nivel = int(user["nivel"])
                print(Fore.CYAN + Style.BRIGHT + "Credenciales correctas. ¡Bienvenido!")
                usuario_correcto = True
                return nivel
            
        if usuario_correcto:
            break
        else:
            intentos = intentos - 1
            if intentos > 0:
                print(Fore.RED + f"Usuario o contraseña incorrectos. Le quedan {intentos} intentos.")
            else:
                print(Fore.RED + "Usuario o contraseña incorrectos. No le quedan más intentos.")
                sys.exit()

#-----------------------------------------------
# Función de registro de usuario
#-----------------------------------------------
def usuario():
    limpiar()
    
    user = {}
    usuario = input(Fore.YELLOW + Style.BRIGHT + "Ingrese nombre de usuario: ")
    contraseña = input(Fore.YELLOW + Style.BRIGHT + "Ingrese contraseña: ")
    flag = True
    while flag:
        try:
            nivel = int(input(Fore.YELLOW + Style.BRIGHT + "Ingrese nivel de acceso: " ))
            if nivel == 1 or nivel == 2 or nivel == 3:
                print(Fore.CYAN + Style.BRIGHT + "Usuario creado exitosamente!!!!!!.")
                nivel = str(nivel)
                flag = False
                break
            else:
                print(Fore.RED + "El nivel de usuario debe ser un número entre 1 y 3")
                print(Fore.RED + "Ingrese el nivel correcto")
                    
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero entre 1 y 3...")
            print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        
# Creo el diccionario de los usuarios:

    user = {
        "usuario"   : usuario,
        "password"  : contraseña,
        "nivel"     : nivel
    }

# Guardo los usuarios en una lista:

    listaUsuarios.append(user)

# Guardo los datos en un archivo:

    lista = open("user.json", "w") 
    json.dump(listaUsuarios, lista, indent=4)  
    lista.close()     

#-----------------------------------------------
# Chequeo si el código se repite 
#-----------------------------------------------
def validar_codigo(codigo):# Verifica si el código ingresado se repite
    respuesta = False
    for articulo in lista_articulos:
        if articulo["codigo"]==codigo:
            respuesta = True
            break
    return respuesta

#-----------------------------------------------
# Función para crear articulos
#-----------------------------------------------
def altas():
    limpiar()
    while True:
        auxiliar = True
        while auxiliar:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código de producto: "))
                auxiliar = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
        validar = validar_codigo(codigo)
        if validar == False:
            break
        else:
            print(Fore.YELLOW + "Ese código ya esta registrado. Ingrese el correcto....")

    nombre   = input(Fore.CYAN + Style.BRIGHT + "Nombre del Articulo: ")
    desc     = input(Fore.CYAN + Style.BRIGHT + "Descripción breve: ")
    auxiliar_2 = True
    while auxiliar_2:
        try:
            valor    = int(input(Fore.CYAN + Style.BRIGHT + "Valor del articulo: "))
            auxiliar_2 = False
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
            print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
    auxiliar_3 = True
    while auxiliar_3:
        try:
            cantidad = int(input(Fore.CYAN + Style.BRIGHT + "Cantidad del articulo: "))
            auxiliar_3 = False
        except:
            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
            print(Fore.RED + Style.BRIGHT + "Intente nuevamente!!!!!!!!!!")
        

# Creo el diccionario de los productos:

    articulo = {
        "codigo"      : codigo,
        "nombre"      : nombre,
        "descripcion" : desc,
        "valor"       : valor,
        "cantidad"    : cantidad
        }

# Guardo los productos en una lista:

    lista_articulos.append(articulo)

# Guardo los datos en un archivo:

    archivo = open("articulo.json", "w") 
    json.dump(lista_articulos, archivo, indent=4)  
    archivo.close()
    limpiar()
#-----------------------------------------------
# Función editar articulos
#-----------------------------------------------
def editar():
    # 1) Chequeamos si el código ingresado existe
    limpiar()
    while True:
        bandera = True
        while bandera:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del articulo: "))
                bandera = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")

        if validar_codigo(codigo):
# Buscar los datos del producto
            for articulo in lista_articulos:
                if articulo["codigo"] == codigo:
# 2) Mostramos los datos 
                    limpiar()
                    print("Nombre...........", articulo["nombre"])
                    print("Valor............", articulo["valor"])
                    print("Descripción......", articulo["descripcion"])
                    print("Cantidad.........", articulo["cantidad"])
# 3) Guardamos los datos en nuevas variables
                    a_nombre = articulo["nombre"]
                    a_valor = articulo["valor"]
                    a_desc  = articulo["descripcion"]
                    a_cantidad = articulo["cantidad"]
# 4) Pedimos ingresar los nuevos datos
                    
                    print(Fore.CYAN + "Datos editados ( Presinar Enter si no se realizan cambios)")
                    nombre     = input("Nombre:............ ")
                    valor      = input("Valor:............. ")
                    desc       = input("Descripción:....... ")
                    cantidad   = input("Cantidad:.......... ")
# 5) Armamos un nuevo diccionario con los datos editados
                                
                    if len(nombre) == 0:
                        n_nombre = a_nombre
                    else:
                        n_nombre = nombre

                    if len(valor) == 0:
                        n_valor = a_valor
                    else:
                        n_valor = int(valor)

                    if len(desc) == 0:
                        n_desc = a_desc 
                    else:
                        n_desc = desc

                    if len(cantidad) == 0:
                        n_cantidad = a_cantidad
                    else:
                        n_cantidad = int(cantidad)

# Creamos el diccionario con los datos del prducto editado:
                    articulo = {
                        "codigo"      : codigo,
                        "nombre"      : n_nombre,
                        "descripcion" : n_desc,
                        "valor"       : n_valor,
                        "cantidad"    : n_cantidad
                        }

                    for id, editado in enumerate(lista_articulos):  
                        if editado["codigo"] == codigo:
                            del lista_articulos[id]
                                    
# Agregar el diccionario con cambios editados
                    lista_articulos.append(articulo)

# Actualizamos el archivo JSON
                    archivo = open("articulo.json", "w") 
                    json.dump(lista_articulos, archivo, indent=4) 
                    archivo.close()                     

                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            opción = input(Fore.RED + "¿Desea probar con otro código? [s/n]")
            if opción.lower() == "n":
                limpiar()
                return
#-----------------------------------------------
# Función de venta de articulos
#-----------------------------------------------
def vender():
    limpiar()
    while True:
        aux = True
        while aux:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del articulo que vendió: "))
                aux = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        if validar_codigo(codigo):
            for articulo in lista_articulos:
                if articulo["codigo"] == codigo:
                    print()
                    print("Nombre:        ", articulo["nombre"])
                    print("Valor:         ", articulo["valor"])
                    print("Descripción:   ", articulo["descripcion"])
                    print("Cantidad:      ", articulo["cantidad"])
                    print()
                    aux_1 = True
                    while aux_1:
                        try:
                            cantidad_v = int(input(Fore.CYAN + Style.BRIGHT + "Cantidad del Articulo vendido: "))
                            if cantidad_v > articulo["cantidad"]:
                                print(Fore.RED + "La cantidad a entregar es mayor que la cantidad disponible.")
                            else:
                                cantidad_t = articulo["cantidad"] - cantidad_v
                                aux_1 = False
                        except:
                            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                            print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
                            break
                        

# Crear el registro de compra
                    articulo = {
                        "codigo"      : codigo,
                        "nombre"      : articulo["nombre"],
                        "descripcion" :articulo["descripcion"],
                        "valor"       : articulo["valor"],
                        "cantidad"    : cantidad_t
                        }
                    

                    for id, articulos in enumerate(lista_articulos):  
                        if articulos["codigo"] == codigo:
                            del lista_articulos[id]

# Guardar el registro de entrega en la lista de empleados
                    lista_articulos.append(articulo)

# Actualizar el archivo JSON de productos con la nueva cantidad
                    archivo = open("articulo.json", "w") 
                    json.dump(lista_articulos, archivo, indent=4)

                    print(Fore.GREEN + "Articulo vendido exitosamente.")
                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            eleccion = input(Fore.RED + "¿Desea intentar con otro código? [s/n]: ")
            if eleccion.lower() == "n":
                limpiar()
                return
#-----------------------------------------------
# Función de compra de articulos incrementando stock
#-----------------------------------------------
def comprar():
    limpiar()
    while True:
        aux = True
        while aux:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del articulo que compró: "))
                aux = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        if validar_codigo(codigo):
            for articulo in lista_articulos:
                if articulo["codigo"] == codigo:
                    print()
                    print("Nombre:        ", articulo["nombre"])
                    print("Descripción:   ", articulo["descripcion"])
                    print("Valor:         ", articulo["valor"])
                    print("Cantidad:      ", articulo["cantidad"])
                    print()
                    aux_1 = True
                    while aux_1:
                        try:
                            cantidad_e = int(input(Fore.CYAN + Style.BRIGHT + "Cantidad del Articulo comprado: "))
                            cantidad_f = articulo["cantidad"] + cantidad_e
                            print(cantidad_f)
                            aux_1 = False
                        except:
                            print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                            print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
                        continue
                    

                    
# Crear el registro de compra
                    articulo = {
                        "codigo"     : codigo,
                        "nombre"     : articulo["nombre"],
                        "descripcion": articulo["descripcion"],
                        "valor"      : articulo["valor"],
                        "cantidad"   : cantidad_f
                        }
                    
                    for id, articulos in enumerate(lista_articulos):  
                        if articulos["codigo"] == codigo:
                            del lista_articulos[id]

# Guardar el registro de entrega en la lista de empleados
                    lista_articulos.append(articulo)

# Actualizar el archivo JSON de productos con la nueva cantidad
                    archivo = open("articulo.json", "w") 
                    json.dump(lista_articulos, archivo, indent=4)

                    print(Fore.GREEN + "Articulo actualizado exitosamente.")
                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            eleccion = input(Fore.RED + "¿Desea intentar con otro código? [s/n]: ")
            if eleccion.lower() == "n":
                limpiar()
                return
#-----------------------------------------------
# Función de eliminacion de articulos
#-----------------------------------------------
def borrar():
    # 1) Chequeamos si el código ingresado existe
    limpiar()
    while True:
        flag = True
        while flag:
            try:
                codigo = int(input(Fore.CYAN + Style.BRIGHT + "Ingrese el código del producto: "))
                flag = False
            except:
                print(Fore.RED + Style.BRIGHT + "Debe ser un número entero...")
                print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        if validar_codigo(codigo):
# Buscar los datos del producto
            for articulo in lista_articulos:
                if articulo["codigo"] == codigo:
# 2) Mostramos los datos 
                    limpiar()
                    print("Nombre............", articulo["nombre"])
                    print("Descripción.......", articulo["descripcion"])
                    print("Valor.............", articulo["valor"])
                    print("Cantidad..........", articulo["cantidad"])
                    
                    opción = input(Fore.RED + "¿Estas seguro de eliminar el registro? [s/n]: ")
                    if opción.lower() == "s":
                        for id, editado in enumerate(lista_articulos):  
                            if editado["codigo"] == codigo:
                                del lista_articulos[id]
# Actualizamos el archivo JSON
                    archivo = open("articulo.json", "w") 
                    json.dump(lista_articulos, archivo, indent=4) 
                    archivo.close()                     
                    return
        else:
            print(Fore.RED + "El código ingresado no existe.")
            opcion = input(Fore.RED + "¿Desea probar con otro código? [s/n]")
            if opcion.lower() == "n":
                limpiar()
                return
#-----------------------------------------------
# Función listado de articulos existentes
#-----------------------------------------------   
def listar():
    limpiar()
    print(Fore.GREEN + Style.BRIGHT + "Lista de Articulos.")
    print(Fore.GREEN + "="*77)
    print(Fore.GREEN + "| Código | Nombre del Producto  |    Descripción     |  Valor   | Cantidad  |")
    print(Fore.GREEN + "="*77)
    for articulo in lista_articulos:
        print(f"| {articulo ['codigo']:6} ", end="")       
        print(f"| {articulo ['nombre'][:20]:20} ", end="")
        print(f"| {articulo ['descripcion'][:18]:18} ", end="")  
        print(f"|${articulo ['valor']:8} ", end="")
        print(f"| {articulo ['cantidad']:9} |")
    print(Fore.GREEN + "="*77)

#-----------------------------------------------
# Función Eliminar Usuario existente
#-----------------------------------------------
def eliminar_usuario():# Elimina del registro al usuario completo
# 1) Chequeamos si el usuario ingresado existe
    limpiar()
    while True:
        cambio_password = input(Fore.CYAN + Style.BRIGHT + "Usuario a eliminar: ")
# Buscar los datos del producto
        for usuarios in listaUsuarios:
            if usuarios["usuario"] == cambio_password:
# 2) Mostramos los datos 
                limpiar()
                print("Usuario................", usuarios["usuario"])
                print("Contraseña.............", usuarios["password"])
                print("Nivel..................", usuarios["nivel"])
                opción = input(Fore.RED + Style.BRIGHT + "¿Estas seguro de eliminar el usuario? [s/n]: ")
                limpiar()
                if opción.lower() == "s":
                    for ident, editados in enumerate(listaUsuarios):  
                        if editados["usuario"] == cambio_password:
                            del listaUsuarios[ident]
                            
# Actualizamos el archivo JSON
                a = open("user.json", "w") 
                json.dump(listaUsuarios, a, indent=4) 
                a.close()                     
                return
        else:
            print(Fore.RED + "El usuario ingresado no existe.")
            seleccion = input(Fore.RED + "¿Desea probar con otro usuario? [s/n]")
            if seleccion.lower() == "n":
                return
            
#-----------------------------------------------
# Función para editar usuarios 
#-----------------------------------------------
def editar_usuario():# Se pueden realizar cambios a los datos del usuario, clave y nivel de acceso
# 1) Chequeamos si el usuario ingresado existe
    limpiar()
    while True:
        cambio_password = input(Fore.YELLOW + Style.BRIGHT + "Ingrese el usuario a editar: ")
# Buscar los datos del usuario
        for user in listaUsuarios:
            if user["usuario"] == cambio_password:
# 2) Mostramos los datos 
                limpiar()
                print("Usuario:................", user["usuario"])
                print("Contraseña:.............", user["password"])
                print("Nivel:..................", user["nivel"])
# 3) Guardamos los datos en nuevas variables
                a_user  = user["usuario"]
                a_password = user["password"]
                a_nivel    = user["nivel"]
# 4) Pedimos ingresar los nuevos datos
                limpiar()
                print(Fore.CYAN + "Datos editados ( Presinar Enter si no se realizan cambios)")
                user   = input("Usuario:............ ")
                password  = input("Contraseña:......... ")
                
                flags = True
                while flags:
                    try:
                        nivel = int(input("Nivel:.............. "))
                        if nivel == 1 or nivel == 2 or nivel == 3:
                            print(Fore.CYAN + Style.BRIGHT + "Usuario editado exitosamente.")
                            nivel = str(nivel)
                            flags = False
                            break
                        else:
                            print(Fore.RED + "El nivel de usuario debe ser entre 1 y 3")
                            print(Fore.RED + "Ingrese el nivel correcto")
                                
                    except:
                        print(Fore.RED + Style.BRIGHT + "Debe ser un número entero entre 1 y 3...")
                        print(Fore.RED + Style.BRIGHT + "Intenta nuevamente!!!!!!!!!!")
        
# 5) Armamos un nuevo diccionario con los datos editados
                    
                if len(usuario) == 0:
                    n_user = a_user
                else:
                    n_user = user

                if len(password) == 0:
                    n_password = a_password
                else:
                    n_password = password

                if len(nivel) == 0:
                    n_nivel = a_nivel
                else:
                    n_nivel = nivel

# Creamos el diccionario con los datos del prducto editado:
                user = {
                    "usuario"  : n_user,
                    "password" : n_password,
                    "nivel"    : n_nivel
                    }

                for ident, editados in enumerate(listaUsuarios):  
                    if editados["usuario"] == cambio_password:
                        del listaUsuarios[ident]
                                
# Agregar el diccionario con cambios editados
                listaUsuarios.append(user)

# Actualizamos el archivo JSON
                a = open("user.json", "w") 
                json.dump(listaUsuarios, a, indent=4) 
                a.close()                     
                return
        else:
            print(Fore.RED + "El usuario ingresado no existe.")
            seleccion = input(Fore.RED + "¿Desea probar con otro usuario? [s/n]")
            if seleccion.lower() == "n":
                limpiar()
                return

#-----------------------------------------------
# Función para detectar el nivel de usuario 
#-----------------------------------------------
def nivel_acceso_usuario():# Realiza una comparación para determinar el nivel de control del usuario
    nivel_i = login()# Compara con la devolución del usuario y contraseña correctos ingresados
    for elemento in listaUsuarios:
        if int(elemento["nivel"] == "1") and nivel_i == 1 :
            nivel_usuario = 1
        elif int(elemento["nivel"] == "2") and nivel_i == 2 :
            nivel_usuario = 2
        elif int(elemento["nivel"] == "3") and nivel_i == 3 :
            nivel_usuario = 3
    return nivel_usuario

#------------------------------------------------------------
# Función para seleccionar el menu de acuerdo al nivel de usuario
#------------------------------------------------------------

def seleccion_menu():# Dependiendo del nivel de usuario muestra el menu correspondiente
    nivel_usuario = nivel_acceso_usuario()
    if nivel_usuario == 3:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 3")
        time.sleep(2) # espera 2 segundos antes de ejecutar
        menu3()
    elif nivel_usuario == 2:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 2")
        time.sleep(2) # espera 2 segundos antes de ejecutar
        menu2()
    elif nivel_usuario == 1:
        print(Fore.CYAN + Style.BRIGHT + "Ud. posee nivel de acceso 1")
        time.sleep(2) # espera 2 segundos antes de ejecutar
        menu1()
#-----------------------------------------------
# Función encabezado
#-----------------------------------------------
def titulo():
    print(Fore.GREEN + Style.BRIGHT + "*" *30)
    print(Fore.GREEN + Style.BRIGHT + "Programa de Control de Stock")
    print(Fore.GREEN + Style.BRIGHT + "*" *30)

#-----------------------------------------------
# Función menu de ingreso
#-----------------------------------------------
def menu():
    titulo()
    while True:
        print(Style.BRIGHT + "[I]NGRESO")
        print(Style.BRIGHT + "[N]UEVO USUARIO")
        print(Style.BRIGHT + "[S]ALIR")
        opcion = input ("Elija una opción:  ").upper()
        match opcion:
            case "I":
                seleccion_menu()
            case "N":
                usuario()
            case "S":
                sys.exit()

#-----------------------------------------------
# Función menu nivel 2 opciones
#-----------------------------------------------       
def menu1():
    limpiar()
    titulo()
    print("Usuario Nivel 1 Usuario inicial!!!!!")
    while True:
        print(Style.BRIGHT + "[A]LTAS")
        print(Style.BRIGHT + "[V]ENDER")
        print(Style.BRIGHT + "[L]ISTAR")
        print(Style.BRIGHT + "[S]ALIR")
        opcion2 = input ("Ingrese una opción:  ").upper()
        limpiar()
        match opcion2:
            case "A":
                altas()
            case "V":
                vender()
            case "L":
                listar()
            case "S":
                sys.exit()
#-----------------------------------------------
# Función menu nivel 2 opciones
#-----------------------------------------------       
def menu2():
    limpiar()
    titulo()
    print("Usuario Nivel 2 Usuario completo!!!!!")
    while True:
        print(Style.BRIGHT + "[A]LTAS")
        print(Style.BRIGHT + "[E]DITAR")
        print(Style.BRIGHT + "[V]ENDER")
        print(Style.BRIGHT + "[C]OMPRAR")
        print(Style.BRIGHT + "[B]ORRAR")
        print(Style.BRIGHT + "[L]ISTAR")
        print(Style.BRIGHT + "[S]ALIR")
        opcion2 = input ("Ingrese una opción:  ").upper()
        limpiar()
        match opcion2:
            case "A":
                altas()
            case "E":
                editar()
            case "V":
                vender()
            case "C":
                comprar()
            case "B":
                borrar()
            case "L":
                listar()
            case "S":
                sys.exit()

#-----------------------------------------------
# Función menu nivel 3 opciones
#-----------------------------------------------       
def menu3():
    limpiar()
    titulo()
    print("Usuario Nivel 3 Administrador!!!!!")
    while True:
        print(Style.BRIGHT + "[A]LTAS")
        print(Style.BRIGHT + "[E]DITAR")
        print(Style.BRIGHT + "[V]ENDER")
        print(Style.BRIGHT + "[C]OMPRAR")
        print(Style.BRIGHT + "[B]ORRAR")
        print(Style.BRIGHT + "[L]ISTAR")
        print(Style.BRIGHT + "[U]SUARIOS EDITAR")
        print(Style.BRIGHT + "[D]AR DE BAJA USUARIO")
        print(Style.BRIGHT + "[S]ALIR")
        opcion3 = input ("Ingrese una opción:  ").upper()
        limpiar()
        match opcion3:
            case "A":
                altas()
            case "E":
                editar()
            case "V":
                vender()
            case "C":
                comprar()
            case "B":
                borrar()
            case "L":
                listar()
            case "U":
                editar_usuario()
            case "D":
                eliminar_usuario()
            case "S":
                sys.exit()       
#--------------------------------------------------------------------
#Programa principal
#--------------------------------------------------------------------
try: 
    lista = open("user.json", "r") 
    listaUsuarios = json.load(lista)  
    lista.close()
    lista = open("articulo.json", "r") 
    lista_articulos = json.load(lista)  
    lista.close()
except:
    listaUsuarios  = []
    lista_articulos = []

menu()
limpiar()
