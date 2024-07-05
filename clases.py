class ProductoDat:
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

    def consultar_producto(self, codigo):         #funcion consulta de prod. con COD
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
            print(f"codigo.....: {producto['codigo']}")
            print(f"descripción: {producto['descripcion']}")
            print(f"tamano.....: {producto['tamano']}")
            print(f"cantidad...: {producto['cantidad']}")
            print(f"precio.....: {producto['precio']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")
catalogo = ProductoDat()
catalogo.agregar_producto(1,'vino tintillo',100,20,2000)
catalogo.agregar_producto(2,'gaseosa cola',100,20,2000)
catalogo.agregar_producto(3,'gaseosa pepsi',100,20,2000)
catalogo.agregar_producto(4,'gaseosa sprite',100,20,2000)
catalogo.agregar_producto(5,'jugo vaggio',100,20,2000)
catalogo.agregar_producto(6,'vino blanquillo',100,20,2000)

catalogo.listar_producto()

class ClienteDat:
    clientes=[]
    
    def agregar_cliente (self,id ,apellido,nombre,cuit_cuil,telefono,mail,direccion):  #Funcion agregar prod 
        if self.consultar_cliente(id):    # si cod de prod
            return False                  # no esta
        nuevo_cliente = {                # tonces nuevo prod es igual al sig dicc
            'id': id,             #cargo cod  
            'apellido': apellido,   #cargo desc
            'nombre': nombre,              #cargo tam
            'cuit_cuil': cuit_cuil,       #cargo cant
            'telefono': telefono,
            'mail': mail,
            'direccion': direccion      #cargo precio
        }
        self.clientes.append(nuevo_cliente)  #sumo nuevo prod a la lista
        return True       # y confirmo
    
    def consultar_cliente (self, id):         #funcion consulta de prod. con COD
        for cliente in self.clientes:             # itero prod en lista
            if cliente ['id']== id:     #si COD prod es = a cod 
               return cliente                  # retorno producto
        return False                            # si no devuelvo falso
    
    def modificar_cliente(self,id ,nuevo_apellido,nuevo_nombre,nuevo_cuit_cuil,nuevo_telefono,nuevo_mail,nueva_direccion):  # modifico prod por cod
        for cliente in self.clientes:         #itero la lista 
            if cliente['id']== id:   # si esta el cod
               cliente['apellido'] = nuevo_apellido #cambio cada elemento por el nuevo
               cliente['nombre'] = nuevo_nombre
               cliente['cuit_cuil'] = nuevo_cuit_cuil
               cliente['telefono'] = nuevo_telefono
               cliente['mail'] = nuevo_mail
               cliente['direccion'] = nueva_direccion
               return True   #confirmo
        return False  # si no, no puedo modificar 
    
    def listar_cliente(self): #funcion mostrar prod
        print("_"*50)     #imprimo linea de sep 
        for cliente in self.clientes:       # itero cada prod
            print(f"Id..: {cliente['id']}")     # imp item
            print(f"Apellido.....: {cliente['apellido']}")  #imp item
            print(f"Nombre.......: {cliente['nombre']}")       # item
            print(f"Cuit_Cuil....: {cliente['cuit_cuil']}")    #item
            print(f"Telefono.....: {cliente['telefono']}")
            print(f"Mail.........: {cliente['mail']}")#imp item
            print(f"Direccion....: {cliente['direccion']}")
            print("-"*50)               #impr sep entre prod
            
    def eliminar_cliente(self, id):      #funcion eliminar prod por cod
        for cliente in self.clientes:          # itero la lista
            if cliente['id']== id:  # si cod esta en cod
                self.clientes.remove(id)#elimino prod
                return True   # confirmo 
        return False        # si no esta, no elimino
    
    def mostrar_cliente(self,id):          
        cliente = self.consultar_cliente(id)
        if cliente:
            print("-" * 50)
            print(f"Id: {cliente['id']}")
            print(f"Apellido...: {cliente['apellido']}")
            print(f"Nombre.....: {cliente['nombre']}")
            print(f"Cuit_Cuil..: {cliente['cuit_cuil']}")
            print(f"Telefono...: {cliente['telefono']}")
            print(f"Mail.......: {cliente['mail']}")
            print(f"Direccion..: {cliente['direccion']}")
            print("-" * 50)
        else:
            print("Cliente no encontrado.")

clientes = ClienteDat()

clientes.agregar_cliente(1,'de Cousandier','Fernando Sebastian', 20248475723, 1135680406, 'decousandierfs@gmail.com', 'Don Segundo Sombra 5897')
clientes.agregar_cliente(2,'Gomez','Sergio Esteban', 21228472522, 1124324875, 'gomezsergio@gmail.com', 'Av. San Martin 1532')

clientes.listar_cliente()

        
  
    
     
    
    