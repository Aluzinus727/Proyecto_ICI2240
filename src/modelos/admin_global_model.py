import os
import random
import string
import csv
import shutil
from tempfile import NamedTemporaryFile
from src.cupon import Cupon


class AdminGlobalModel:
    """
        Clase que contiene la parte lógica del menú de un administrador global.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_info_cine, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cines: dict, cupones: dict):
        self.empleado = empleado
        self.cines = cines
        self.cupones = cupones

    def generar_cupones(self, cantidad, porcentaje):
        new_cupones = {}

        for _ in range(cantidad):
            codigo = ''.join((random.choice(string.ascii_uppercase) for x in range(6)))

            if self.cupones.get(codigo) is None:
                new_cupon = Cupon(codigo, porcentaje, False)
                self.cupones[codigo] = new_cupon
                new_cupones[codigo] = new_cupon

        path = os.getcwd()
        abs_path_cupones = f"{path}\data\cupones.csv"
        
        with open(abs_path_cupones, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            for codigo, cupon in new_cupones.items():
                writer.writerow((codigo, cupon.descuento, "0"))

            csv_file.close()

        if len(new_cupones.items()) > 0:
            return True
        else:
            return False

    def get_precios_peliculas(self):
        items = []
        for cine in self.cines.values():
            peliculas = cine.get_precios_peliculas()
            
            for pelicula in peliculas:
                if pelicula.dob_sub:
                    formato = "Doblada"
                else:
                    formato = "Subtitulada"

                item = (pelicula.id, pelicula.nombre, cine.nombre, formato, pelicula.precio) 
                items.append(item)

        return items

    def modificar_precio(self, id_pelicula, nombre_cine, precio):
        cine = self.cines.get(nombre_cine)

        cine.modificar_precio(id_pelicula, precio)

        path = os.getcwd()
        abs_path_peliculas = f"{path}\data\{nombre_cine}\\peliculas.csv"
        tempfile = NamedTemporaryFile(mode='a', delete=False)
        fields = ['nombre', 'id', 'duracion', 'año', 'generos', 'precio', 'dob_sub']

        with open(abs_path_peliculas, 'r+', newline='') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
            for row in reader:
                if row['id'] == str(id_pelicula):  
                    row['precio'] = precio
                writer.writerow(row)

        shutil.move(tempfile.name, abs_path_peliculas)
        
    def agregar_admin_local (self): #deberia recibir (self, nombre_cine)
        rut = "12245184"
        contraseña = "qps2021"
        nombre_cine = "vina_del_mar"
        path = os.getcwd()
        abs_path_credenciales = f"{path}\data\\credenciales.csv"
        
        with open(abs_path_credenciales, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerow((rut, contraseña, "administrador_local", self.cine.nombre))

            csv_file.close()