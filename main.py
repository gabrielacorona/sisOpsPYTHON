# Proyecto sistemas operativos
# Implementación FIFO LRU

# Versión de lenguaje:  C++17


# Integrantes del equipo:
# Gabriela Corona Garza A01282529
# Marlon Omar López A00139431
# Paulina González Dávalos A01194111
# Jorge Arturo Ramirez A01088601
# Victor Andres Villarreal Grimaldo A01039863


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
    f = open("txtFiles/ArchivoTrabajo.txt", "r")
    lines = f.read().splitlines()

    comandos = []


    for i, linea in enumerate(lines):
        words = linea.rstrip()
        words = words.lstrip()
        words =' '.join(words.split())

        """
        L: int
        P: int int
        A: int int int

        """ 
        listaLineas = words.split()
        comando = []

        if words[0] == 'A':
            comando.append(listaLineas[0])
            comando.append(int(listaLineas[1]))
            comando.append(int(listaLineas[2]))
            comando.append(int(listaLineas[3]))

        if words[0] == 'P':
            comando.append(listaLineas[0])
            comando.append(int(listaLineas[1]))
            comando.append(int(listaLineas[2]))
        
        if words[0] == 'L':
            comando.append(listaLineas[0])
            comando.append(int(listaLineas[1]))

        if words[0] == 'C':
            comando.append(listaLineas[0])
            print('')
        
        if words[0] == 'E':
            comando.append(listaLineas[0])
            print('')

        if words[0] == 'F':
            comando.append(listaLineas[0])
            print('')
        
        #else:
        
        comandos.append(comando)    
   # print(comandos)
    FIFO(comandos)
    LRU(comandos)        












if __name__ == '__main__':
    main()

