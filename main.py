# Proyecto sistemas operativos
# Implementación FIFO LRU

# Versión de lenguaje:  C++17


# Integrantes del equipo:
# Gabriela Corona Garza A01282529
# Marlon Omar López A00139431
# Paulina González Dávalos A01194111


# *************** COMENZAR ***************
# C = Comenzamos
# Comenzar una ejecución del programa

# *************** CARGAR UN PROCESO ***************
# P n k
# n = número de bytes para cargar a la memoria
# k = número entero arbitrario que indica el id del proceso

# ejemplo
# P 124 1 --> asignar 124 bytes al proceso 1

# *************** ACCESAR LA DIRECCIÓN VIRTUAL ***************
# A d p m
# d = dirección virtual
# p = id del proceso
# m = 1 --> se lee
# m = 0 --> se modifica

# ejemplo
# A 17 5 0 --> accesar para lectura la dirección virtual 17 del proceso 5

# *************** LIBERAR PÁGINAS DEL PROCESO ***************
# L p --> liberar las páginas del proceso p
# output --> comando de input y lista de marcos de página que se liberaron

# *************** COMENTARIO ***************
# Si la línea del input no va con los comandos solo imprimirla

# *************** FIN ***************
# F = Fin
# despliega un reporte de estadísiticas que incluye:
# - turnaround time de cada proceso que se consideró --> diferencia de timestamps
# - turnaround promedio
# - número de page faults
# - número de page faults por proceso
# - número total de operaciones swap-out swap-in

# *************** EXIT ***************
# E = se termina el programa y se despliega un mensaje de despedida


def main():
    memoriaActual = 2048

    f = open("ArchivoTrabajo.txt", "r")
    words = f.read().split()

    for w in words:
        print(w)


if __name__ == '__main__':
    main()

