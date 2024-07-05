import mysql.connector
from flask import Flask, Request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os 
import time
app=Flask(__name__)
CORS(app)
class ProductoDat:
    def __init__(self, host, user, password, database):
        self.conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        self.cursor=self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (codigo INT AUTO_INCREMENT PRIMARY KEY,
                            descripcion VARCHAR(255) NOT NULL,
                            tamano FLOAT (10,2) NOT NULL,
                            cantidad INT NOT NULL,
                            precio FLOAT (10,2) NOT NULL)''')
        self.conn.commit()
       # return self.cursor.rowcount > 0

catalogo = ProductoDat (host='localhost',user='root',password='',database='distribuidora')

@app.route("/productos", methods=["GET"])
def listar_productos():
    productos=catalogo.
class ClienteDat:
    def __init__(self, host, user, password, database):
        self.conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        self.cursor=self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY,
                            apellido VARCHAR(255) NOT NULL,
                            nombre VARCHAR(255) NOT NULL,
                            cuit_cuil INT (11) NOT NULL,
                            telefono INT (10) NOT NULL,
                            mail VARCHAR(255) NOT NULL,
                            direccion VARCHAR(255) NOT NULL)''')
        self.conn.commit()
clientes = ClienteDat (host='localhost', user='root', password='', database='distribuidora')