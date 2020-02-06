# Proyecto sistemas operativos
# Implementacin FIFO LRU

# Versin de lenguaje:  Python 3


# Integrantes del equipo:
# Gabriela Corona Garza A01282529
# Marlon Omar Lpez A00139431
# Paulina Gonzlez Dvalos A01194111
# Jorge Arturo Ramirez A01088601
# Victor Andres Villarreal Grimaldo A01039863


# *************** COMENZAR ***************
# C = Comenzamos
# Comenzar una ejecucin del programa

# *************** CARGAR UN PROCESO ***************
# P n k
# n = nmero de bytes para cargar a la memoria
# k = nmero entero arbitrario que indica el id del proceso

# ejemplo
# P 124 1 --> asignar 124 bytes al proceso 1

# *************** ACCESAR LA DIRECCIN VIRTUAL ***************
# A d p m
# d = direccin virtual
# p = id del proceso
# m = 1 --> se lee
# m = 0 --> se modifica

# ejemplo
# A 17 5 0 --> accesar para lectura la direccin virtual 17 del proceso 5

# *************** LIBERAR PGINAS DEL PROCESO ***************
# L p --> liberar las pginas del proceso p
# output --> comando de input y lista de marcos de pgina que se liberaron

# *************** COMENTARIO ***************
# Si la lnea del input no va con los comandos solo imprimirla

# *************** FIN ***************
# F = Fin
# despliega un reporte de estadsiticas que incluye:
# - turnaround time de cada proceso que se consider --> diferencia de timestamps
# - turnaround promedio
# - nmero de page faults
# - nmero de page faults por proceso
# - nmero total de operaciones swap-out swap-in

# *************** EXIT ***************
# E = se termina el programa y se despliega un mensaje de despedida


import time


def FIFO(comandos):
    queue = []
    pageFaults = {}
    memoriaActual = 2048

#  instances = {}
#     for i in word:
#         if i  in instances:
#             instances[i] += 1
#         else:
#             instances[i] = 1
    



    millis = int(round(time.time() * 1000))
    for comand in comandos:
        if comand[0] == 'P':
            if memoriaActual - comand[1] > 0:
                pair = []
                memoriaActual -= comand[1]
                pair.append(comand)
                pair.append(millis)
                queue.append(pair)

                if comand[2] in pageFaults:
                    pageFaults[comand[2]] += 1
                else:
                    pageFaults[comand[2]] = 1

            else:
                #print('pageFault')
                #### GENERA PAGE FAULT AL SACAR O METER INFO
                
                while memoriaActual - comand[1] < 0 or pair in queue:
                    temp = pair[0]
                    memoriaActual += temp[1]
                    queue.pop(0)

                    if comand[2] in pageFaults:
                        pageFaults[comand[2]] += 1
                    else:
                        pageFaults[comand[2]] = 1

                else:
                    pair = []
                    memoriaActual -= comand[1]
                    pair.append(comand)
                    pair.append(millis)
                    queue.append(pair)

                   

        if comand[0] == 'L':
            for pair in queue:
                temp = (pair[0])
                if temp[2] == comand[1]:
                    queue.remove(pair)
 
        if comand[0] == 'A':
            #print (comand)
            #print(queue)
            if comand[3] == 0:
                for pair in queue:
                    temp = pair[0]
                    #print (temp[2])
                    #if temp[2] == comand[2]:
                     #print(pair)

            if comand[3] == 1:
                print('mod')
            for pair in queue:
                temp = pair[0]
                #if temp[2] == comand[2]:


        if comand[0] == 'F':
            totalP = 0
            for f in pageFaults:
                totalP += pageFaults[f]
            print('Page faults totales: ' + str(totalP) )
            print('')
            print('Page Faults por id de proceso: ')
            for f in pageFaults:
                print( str(f) + ' = ' + str(pageFaults[f]))


            


        


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
       



if __name__ == '__main__':
    main()