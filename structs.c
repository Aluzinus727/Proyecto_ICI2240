#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include "headers/list.h"
#include "headers/hashmap.h"
#include "headers/treemap.h"

typedef struct
{
    char rut[9];
    char contrasenia[256];
    char cargo[50];
    char cine[50];
    void *trabajador;
} Usuario;

typedef struct
{
    char nombre[50];
    int anio;
    int stock;
    List *generos;
    HashMap *funciones;
    int precio;
    char formato[4];
    int dob_sub;
} Pelicula;

typedef struct
{
    int numero;
    int asientos_totales;
    int estado;
    Pelicula pelicula;
} Sala;

typedef struct
{
    time_t inicio;
    time_t final;
} Horario;

typedef struct
{
    Horario horario;
    Sala sala;
    Pelicula pelicula;
    int entradas_vendidas;
} Funcion;

typedef struct
{
    char nombre[20];
    char rut[10];
    int sueldo;
    char cargo[12]; // empleado, admin, admin_global
    Horario horario;
    char password[8];
    int ventas;
    List *asistencia;
} Trabajador;

typedef struct
{
    char nombre[30];
    int total_ventas;
    HashMap *trabajadores;
    HashMap *peliculas;
    List *salas;
} Cine;

typedef struct
{
    bool usado;
    int descuento;
} Codigo;