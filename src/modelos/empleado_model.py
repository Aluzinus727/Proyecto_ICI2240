import os
import csv
import time
import shutil
from tempfile import NamedTemporaryFile
from datetime import datetime
from src.horario import Horario

class EmpleadoModel:
    """
        Clase que contiene la parte lógica del menú de un empleado.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_horario, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cine, cupones):
        self.empleado = empleado
        self.cine = cine
        self.cupones = cupones

        self.venta = Venta()

    def _registrar_venta(self):
        """
            Se guardan los datos de la venta en los archivos csv correspondientes.
        """
        pass

    def get_peliculas(self):
        return self.cine.get_peliculas()

    def get_funciones(self, id_pelicula):
        return self.cine.get_funciones(id_pelicula)
    
    def guardar_venta(self, id_pelicula, inicio):
        pelicula = self.cine.get_pelicula(id_pelicula)
        funcion = pelicula.get_funcion(inicio)

        self.venta.funcion = funcion

        print(f"Pelicula almacenada: {self.venta.funcion.pelicula.nombre} Inicio: {self.venta.funcion.horario.inicio} Sala: {self.venta.funcion.sala.numero}")

    def mostrar_horario_mod(self):
        horarios = self.empleado.get_horario_semana()
        horarios_concatenados = ""

        for horario in horarios:
            horarios_concatenados += f"Fecha:{horario.inicio.strftime('%d/%m')} Hora ingreso:{horario.inicio} Hora salida:{horario.final}\n"
            print("Fecha:", horario.inicio.strftime("%d/%m"), "Hora ingreso:", horario.inicio, "Hora salida:", horario.final)

        return horarios_concatenados
                
    def marcar_asistencia_mod(self):
        horario = self.empleado.get_horario_actual()

        if horario is not None:
            unixtime = int(time.mktime(horario.timetuple()))

            path = os.getcwd()
            absolute_path = f"{path}\data\{self.empleado.cine}\empleados\{self.empleado.rut}\\asistencia.csv"

            tempfile = NamedTemporaryFile(mode='a', delete=False)

            fields = ['horario_inicio', 'asistencia']

            with open(absolute_path, 'r+', newline='') as csvfile, tempfile:
                reader = csv.DictReader(csvfile, fieldnames=fields)
                writer = csv.DictWriter(tempfile, fieldnames=fields, lineterminator='\n')
                for row in reader:
                    if row['horario_inicio'] == str(unixtime):
                        if row['asistencia'] == "1":
                            return (False, "Ya ha registrado la asistencia.")
                        row['horario_inicio'], row['asistencia'] = unixtime, 1
                    row = {'horario_inicio': row['horario_inicio'], 'asistencia': row['asistencia']}
                    writer.writerow(row)

            shutil.move(tempfile.name, absolute_path)

            return (True, "Se ha marcado la asistencia con éxito")
        else:
            return (False, "No hay horarios que mostrar.")

    def verificar_cupon(self, codigo: str) -> bool:
        cupon = self.cupones.get(codigo)

        if cupon is not None:
            if cupon.verificar():
                self.venta.descuento = cupon
                return True
            
        return False 

    def concretar_venta(self):
        """
            Función que se llama cuando el empleado hace click en el botón de concretar venta de la interfaz gráfica.
        """
        if self.venta.es_valida() and self.venta.hay_entradas_disponibles():
            datos_boleta = self.venta.get_datos_boleta()
            return datos_boleta

        return None

    def concretar_venta_confirmacion(self):
        """
            Función que se llama luego de que el empleado confirma la boleta.
        """
        self.venta.aumentar_entradas_vendidas()
        self._registrar_venta()

        self.venta.funcion = None
        self.venta.descuento = None

    def cancelar_venta(self):
        """
            Se cancela la venta reseteando los valores almacenados.
        """
        self.venta.funcion = None
        self.venta.descuento = None


class Venta:
    def __init__(self, funcion = None, descuento = None):
        self.funcion = funcion
        self.descuento = descuento

    def es_valida(self):
        if self.funcion is not None:
            return True

        return False

    def get_datos_boleta(self):
        datos_boleta = {
            "nombre_pelicula": self.funcion.get_nombre_pelicula(),
            "sala": self.funcion.get_numero_sala(),
            "hora_inicio": self.funcion.get_horario_inicio(),
            "precio": self.calcular_precio()
        }

        return datos_boleta

    def calcular_precio(self):
        precio_normal = self.funcion.get_precio()

        if self.descuento is None:
            return precio_normal

        return precio_normal * (1 - (self.descuento.descuento / 100))

    def hay_entradas_disponibles(self):
        if self.funcion.entradas_vendidas < self.funcion.get_tamaño_sala():
            return True
        else:
            return False

    def aumentar_entradas_vendidas(self):
        self.funcion.entradas_vendidas += 1