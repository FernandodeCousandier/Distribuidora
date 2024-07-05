
productos=[]                             #lista de productos

def agregar_producto (codigo,descripcion,tamano,cantidad,precio):  #Funcion agregar prod 
    if consultar_producto (codigo):    # si cod de prod
        return False                  # no esta
    nuevo_producto = {                # tonces nuevo prod es igual al sig dicc
        'codigo': codigo,             #cargo cod  
        'descripcion': descripcion,   #cargo desc
        'tamano': tamano,              #cargo tam
        'cantidad': cantidad,       #cargo cant
        'precio': precio            #cargo precio
    }
    productos.append(nuevo_producto)  #sumo nuevo prod a la lista
    return True       # y confirmo

def consultar_producto (codigo):         #funcion consulta de prod. con COD
    for producto in productos:             # itero prod en lista
        if producto['codigo']==codigo:     #si COD prod es = a cod 
            return producto                  # retorno producto
    return False                            # si no devuelvo falso

def modificar_producto(codigo,nueva_descripcion,nuevo_tamano,nueva_cantidad,nuevo_precio):  # modifico prod por cod
    for producto in productos:         #itero la lista 
        if producto['codigo']==codigo:   # si esta el cod
            producto['descripcion'] = nueva_descripcion #cambio cada elemento por el nuevo
            producto['tamano'] = nuevo_tamano
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            return True   #confirmo
    return False  # si no, no puedo modificar 

def listar_producto(): #funcion mostrar prod
    print("_"*50)     #imprimo linea de sep 
    for producto in productos:       # itero cada prod
        print(f"codigo.....: {producto['codigo']}")     # imp item
        print(f"descripcion: {producto['descripcion']}")  #imp item
        print(f"tamaño.....: {producto['tamano']}")       # item
        print(f"cantidad...: {producto['cantidad']}")    #item
        print(f"precio.....: {producto['precio']}")     #imp item
        print("-"*50)               #impr sep entre prod

def eliminar_producto(codigo):      #funcion eliminar prod por cod
    for producto in productos:          # itero la lista
        if producto['codigo']==codigo:  # si cod esta en cod
            productos.remove(producto)#elimino prod
            return True   # confirmo 
    return False        # si no esta, no elimino

# agregamos productos

agregar_producto(1, 'Teclado USB 101 teclas', 100, 10, 4500)
agregar_producto(2, 'Mouse USB 3 botones', 100, 5, 2500)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 100, 15, 52500)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 100, 25, 78500)
agregar_producto(5, 'Pad mouse', 100, 5, 500)
agregar_producto(6, 'Parlantes USB', 100, 4, 2500)

# consultamos productos por codigo

cod_prod=int(input("Digite Cod de prod: "))
producto= consultar_producto(cod_prod)
if producto:
    print(f"producto encontrado: {producto ['codigo'] }-{producto ['descripcion'] }")
else: 
    print(f"producto {cod_prod} no encontrado")

#TRANSF A CLASES

class Catalogo:
    productos=[]
    def agregar_producto (self,codigo,descripcion,tamano,cantidad,precio):  #Funcion agregar prod 
        if self.consultar_producto(codigo):    # si cod de prod
            return False                  # no esta
        nuevo_producto = {                # tonces nuevo prod es igual al sig dicc
            'codigo': codigo,             #cargo cod  
            'descripcion': descripcion,   #cargo desc
            'tamano': tamano,              #cargo tam
            'cantidad': cantidad,       #cargo cant
            'precio': precio            #cargo precio
        }
        self.productos.append(nuevo_producto)  #sumo nuevo prod a la lista
        return True       # y confirmo

def consultar_producto (self, codigo):         #funcion consulta de prod. con COD
    for producto in self.productos:             # itero prod en lista
        if producto['codigo']==codigo:     #si COD prod es = a cod 
            return producto                  # retorno producto
    return False                            # si no devuelvo falso

def modificar_producto(self,codigo,nueva_descripcion,nuevo_tamano,nueva_cantidad,nuevo_precio):  # modifico prod por cod
    for producto in self.productos:         #itero la lista 
        if producto['codigo']==codigo:   # si esta el cod
            producto['descripcion'] = nueva_descripcion #cambio cada elemento por el nuevo
            producto['tamano'] = nuevo_tamano
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            return True   #confirmo
    return False  # si no, no puedo modificar    

def listar_producto(self): #funcion mostrar prod
    print("_"*50)     #imprimo linea de sep 
    for producto in self.productos:       # itero cada prod
        print(f"codigo.....: {producto['codigo']}")     # imp item
        print(f"descripcion: {producto['descripcion']}")  #imp item
        print(f"tamaño.....: {producto['tamano']}")       # item
        print(f"cantidad...: {producto['cantidad']}")    #item
        print(f"precio.....: {producto['precio']}")     #imp item
        print("-"*50)               #impr sep entre prod

def eliminar_producto(self, codigo):      #funcion eliminar prod por cod
    for producto in self.productos:          # itero la lista
        if producto['codigo']==codigo:  # si cod esta en cod
            self.productos.remove(producto)#elimino prod
            return True   # confirmo 
    return False        # si no esta, no elimino

def mostrar_producto(self, codigo):
    producto = self.consultar_producto(codigo)
    if producto:
        print("-" * 50)
        print(f"Código.....: {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Tamano.....: {producto['tamano']}")
        print(f"Cantidad...: {producto['cantidad']}")
        print(f"Precio.....: {producto['precio']}")
        print("-" * 50)
    else:
        print("Producto no encontrado.")