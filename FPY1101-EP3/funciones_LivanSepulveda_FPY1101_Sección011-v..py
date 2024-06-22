
nombrelibros = ["alas de hierro", "la sombra de la sirena",]
autorlibro = ["rebeca yarros", "camilla lackberg"]
añopublicacion = [2024, 2003]
SKU = ["ALASDE-REB-2024","LASOMB-CAM-2003" ]
libros = []
usuarios= []
prestamo= []
def registrar(libros) :
    libro = input("Ingrese el nombre del libro que desea registrar: ")
    while libro in nombrelibros:
        print("Libro ya registrado: ")
        libro = input("Ingrese el nombre del libro que desea registrar: ")
        nombrelibros.append(libro)
    autor = input("Ingrese el autor del libro:")
    while autor in autorlibro:
        de= input("autor registrado anteriormente, ¿desea registrar otra vez?si/no: ").lower
        if de == "si":
            autorlibro.append(autor)
        if de == "no":
            return
    año = ("Ingrese el año de publicacion: ") 
    while año in añopublicacion:
        de= input("año registrado anteriormente, ¿desea registrar otra vez?si/no: ").lower
        if de == "si":
            añopublicacion.append(año)
        if de == "no":
            return
    sk = ("Ingrese el sku del libro: ")
    while sk in SKU:
        print("SKU ya registrado antreriormente: ")
        sk = ("Ingrese el sku del libro: ")
    libros.append({
        "nombre_libro" : libro,
        "nombre_autor" : autor,
        "año_publicacion": año,
        "sku_libro" : sk
    })

def prestar(libros):
    user = input("Ingrese su usuario:")
    while user not in usuarios:
        eleccion =("Usuario no registrado, ¿Desea registrarse? si/no: ").lower
        if eleccion == "si":
            user = input("Ingrese el nmbre de usuario para registrar: ")
            usuarios.append ({
                "usuario": user
            })
        elif eleccion == "no":
            return
    s = input("Ingrese sku del libro :")
    while s not in SKU:
        print("ingrese sku valido:")
        s = input("Ingrese sku del libro :")
    prestamo.append ({
        "sku libro prestado": s,
        "fecha de prestamo": "22-06-2024"
    })

def listar(libros):
    print("Libros de la biblioteca:")
    for libro in libros:
        print(libro)

def imprimir(prestamo):
    imprimir_prestamos = "prestamos.txt"
    if prestamo == []:
        print("no hay libros prestados en este momento")
        with open (imprimir_prestamos, "w") as archivo :
            for libro in libros:
                 archivo.write

menu = ("1.Registrar libro \n2.Prestar libro \n3.Listar todos los libros \n4.Imprimir reporte de prestamos \n5.Salir del programa.")

while True:
    try:
        print(menu)
        opcion =int(input( "Bienvenido a la biblioteca, elija una de las opciones: "))
        if opcion== 1:
            registrar(libros)
        elif opcion == 2:
            prestar(libros)
        elif opcion== 3:
            listar(libros)
        elif opcion == 4:
            imprimir(libros)
        elif opcion== 5:
            break
        else :
            print("Ingrese un numero valido")
    except ValueError:
        print ("ingrese un numero del 1 al 5")