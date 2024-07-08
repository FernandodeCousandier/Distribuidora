import mysql.connector 
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector.errorcode
from werkzeug.utils import secure_filename
from mysql.connector import Error
app=Flask(__name__)
CORS(app)

class Clientes:
    def __init__(self, host, user, password, database):
        self.connection=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor=self.connection.cursor()
        try:
            self.cursor.execute(f'USE {database}')
        except mysql.connector.Error as error:
            if error.errno==mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f'CREATE DATABASE {database}')
                self.connection.database=database
            else:
                raise error
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            apellido VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            cuit_cuil BIGINT(11) NOT NULL,
            telefono INT(10) NOT NULL,
            domicilio VARCHAR (255) NOT NULL)''')
        self.connection.commit()
        
        self.cursor.close()
        self.cursor = self.connection.cursor(dictionary=True)
    
    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes=self.cursor.fetchall()
        return clientes
    
    def consultar_clientes(self,id):
        self.cursor.execute(f"SELECT * FROM clientes WHERE id={id}")
        return self.cursor.fetchone()
    
    def mostrar_clientes(self,id):
        cliente=self.consultar_clientes(id)
        if cliente:
            print("-" * 40)
            print(f"Id........: {cliente['id']}")
            print(f"Apellido..: {cliente['apellido']}")
            print(f"Nombre....: {cliente['nombre']}")
            print(f"Cuit_Cuil.: {cliente['cuit_cuil']}")
            print(f"Telefono..: {cliente['telefono']}")
            print(f"Mail......: {cliente['mail']}")
            print(f"Direccion......: {cliente['direccion']}")
            print("-" * 40)
        else:
            print("cliente no encontrado.")
    
    def agregar_cliente(self, apellido, nombre, cuit_cuil, telefono, mail, direccion): 
        sql="INSERT INTO clientes (apellido, nombre, cuit_cuil, telefono, mail, direccion) VALUES(%s,%s,%s,%s,%s,%s)"
        valores= (apellido, nombre, cuit_cuil, telefono, mail, direccion)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def eliminar_clientes(self, id):
        self.cursor.execute(f"DELETE FROM clientes WHERE id={id}")
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def modificar_cliente(self, id, nuevo_apellido, nuevo_nombre, nuevo_cuit_cuil, nuevo_telefono, nuevo_mail, nueva_direccion):
        sql = "UPDATE clientes SET apellido = %s, nombre = %s, cuit_cuil = %s, telefono = %s, mail = %s, direccion = %s WHERE id = %s"
        valores = (nuevo_apellido, nuevo_nombre, nuevo_cuit_cuil, nuevo_telefono, nuevo_mail, nueva_direccion, id)

        self.cursor.execute(sql, valores)
        self.connection.commit()
        return self.cursor.rowcount > 0

clientedat=Clientes(host='Fernando75.mysql.pythonanywhere-services.com', user='Fernando75', password='sebastian1975',database='distribuidora')

@app.route("/clientes", methods=['GET'])
def listar_clientes():
    clientes=clientedat.listar_clientes()
    return jsonify(clientes)

@app.route("/clientes/<int:id>", methods=['GET'])
def mostrar_clientes(id):
    clientes=clientedat.consultar_clientes(id)
    if clientes:
        return jsonify(clientes)
    else:
        return "Cliente no encontrado", 404
@app.route("/clientes", methods=['POST'])
def agregar_clientes():
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    cuit_cuil = request.form['cuit_cuil']
    telefono = request.form['telefono']
    mail = request.form['mail']
    direccion = request.form['direccion']

    nuevo_cliente=clientedat.agregar_cliente(apellido,nombre,cuit_cuil,telefono,mail,direccion)
    if nuevo_cliente:
        return jsonify({"Mensaje":"Cliente agregado","id": nuevo_cliente})
    else:
        return jsonify({"Mensaje":"Error al agregar el cliente"}), 500
@app.route("/clientes/<int:id>", methods=['PUT'])
def modificar_cliente(id):
    nuevo_apellido=request.form.get('apellido')
    nuevo_nombre=request.form.get('nombre')
    nuevo_cuit_cuil=request.form.get('cuit_cuil')
    nuevo_telefono=request.form.get('telefono')
    nuevo_mail=request.form.get('mail')
    nuevo_direccion=request.form.get('direccion')
    
    if clientedat.modificar_cliente(id, nuevo_apellido,nuevo_nombre,nuevo_cuit_cuil,nuevo_telefono,nuevo_mail,nuevo_direccion):
        return jsonify({"Mensaje":"Cliente modificado"}), 200
    else:
        return jsonify({"Mensaje":"Cliente no encontrado"}), 403

@app.route("/clientes/<int:id>", methods=['DELETE'])
def eliminar_cliente(id):
    clientedat.consultar_clientes(id)
    if clientedat.eliminar_clientes(id):
        return jsonify({"Mensaje":"Cliente borrado"}), 200
    else:
        return jsonify({"Mensaje":"Error al borrar el cliente"}), 404

if __name__=="__main__":
    app.run(debug=True)



