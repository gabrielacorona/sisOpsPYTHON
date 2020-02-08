# Proyecto sistemas operativos
# Implementacion FIFO LRU

# Version de lenguaje:  Python 3


# Integrantes del equipo:
# Gabriela Corona Garza A01282529
# Marlon Omar Lopez A00139431
# Paulina Gonzalez Davalos A01194111
# Jorge Arturo Ramirez A01088601
# Victor Andres Villarreal Grimaldo A01039863


# *************** COMENZAR ***************
# C = Comenzamos
# Comenzar una ejecucion del programa

# *************** CARGAR UN PROCESO ***************
# P n k
# n = nmero de bytes para cargar a la memoria
# k = nmero entero arbitrario que indica el id del proceso

# ejemplo
# P 124 1 --> asignar 124 bytes al proceso 1

# *************** ACCESAR LA DIRECCION VIRTUAL ***************
# A d p m
# d = direccion virtual
# p = id del proceso
# m = 1 --> se lee
# m = 0 --> se modifica

# ejemplo
# A 17 5 0 --> accesar para lectura la direccion virtual 17 del proceso 5

# *************** LIBERAR PAGINAS DEL PROCESO ***************
# L p --> liberar las paginas del proceso p
# output --> comando de input y lista de marcos de pagina que se liberaron

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


from timeit import default_timer as timer





def FIFO(comandos):
    print( ' -------------- FIFO --------------')
    print('')
    queue = []
    pageFaults = {}
    memoriaV = []
    memoriaActual = 2048
    memoriaVirtual = 4096

    
    """
    Como se compone nuestra estructura que simula la memoria virtual
    queue de pairs
    pairs [lista con la informacion del proceso, milisegundos]
    """

    for comand in comandos:
        if comand[0] == 'P': # cargar un proceso

            if memoriaActual - comand[1] > 0: #checa si cabe en la memoria
                start = timer()
                pair = [] #crea el pair que se compone del comando y el timestamp
                memoriaActual -= comand[1] #resta la memoria que ocupa ese proceso
                pair.append(comand)
                pair.append(start)
                queue.append(pair) #mete el pair a la queue

                if comand[2] in pageFaults: #agrega al dict de pagefaults que genera cada uno de los procesos
                    pageFaults[comand[2]] += 1
               
                else:
                    pageFaults[comand[2]] = 1

            else: #si no cabe dentro de la memoria, comienza a sacar el primer elemento de la queue hasta que pueda entrar el proceso

                while memoriaActual - comand[1] < 0 and  pair in queue: 
                 #mientras que no quepa dentro de la memoria sigue sacando o mientras que haya elementos en la queue
                        temp = pair[0]
                        memoriaActual += temp[1]
                        memoriaV.append(queue[0]) #mete a memoria virtual los procesos que se van sacando para meter el proceso grande
                        queue.pop(0)

                        if comand[2] in pageFaults: #agrega al dict de pagefaults que genera cada uno de los procesos
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1
                
        if comand[0] == 'L': #libera de la memoria el proceso con el id correspondiente
            for pair in queue:
                temp = (pair[0])
                if temp[2] == comand[1]: #cada que se libera un proceso de la memoria principal se calcula su turnaround y se intercambia 
                    end = timer()
                    start = pair[1]

                    pair.pop()
                    pair.append(end-start)
                    memoriaV.append(pair) #mete a memoria virtual el proceso se que libero
                    memoriaVirtual -= pair[1] #actualiza la memoria actual restando los bytes que se ocuparon de la memoria virtual
                    memoriaActual += pair[1] #actualiza la memoria actual agregandole los bytes que se liberaron
                    queue.remove(pair) #saca de la queue el elemento correspondiente

                    
        if comand[0] == 'A': #Leer o modificar un proceso

            if comand[3] == 0: #leer, si no esta en la memoria principal se genera un pagefault
                for pair in queue:
                    temp = pair[0]
                    if temp[2] == comand[2]:
                        print('Lectura de Proceso '+str(temp))
               
                for pair in memoriaV: #si no esta en la memoria principal se genera un pagefault
                    temp = pair[0]
                    if temp[2] == comand[2]:
                        print('El proceso ' + str(temp) + ' no se encuentra en la memoria principal')

                        if comand[2] in pageFaults:
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1            
 

            if comand[3] == 1: #modificar
                for pair in queue:
                    temp = pair[0]
                    if temp[2] == comand[2]: 
                        pair = []
                        appnd = temp[2]
                        #se intercambian los valores por los nuevos del comando
                        temp.remove(temp[1])
                        temp.remove(temp[1])

                        temp.append(comand[1])
                        temp.append(appnd)


                    
                    else:
                        if comand[2] in pageFaults:
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1

    # *************** FIN ***************
    # despliega un reporte de estadsiticas que incluye:
    # - turnaround time de cada proceso que se consider --> diferencia de timestamps
    # - turnaround promedio
    # - nmero de page faults
    # - nmero de page faults por proceso
    # - nmero total de operaciones swap-out swap-in

        if comand[0] == 'F':
            totalPf = 0
            totalTurn = 0
            totalPro = 0
            for f in pageFaults:
                totalPf += pageFaults[f]

            print('Page faults totales: ' + str(totalPf) )
            print('')
            print('Page Faults por id de proceso: ')
            print('')

            for f in pageFaults:
                print( str(f) + ' = ' + str(pageFaults[f]))
            print('')
            print('Turnaround por proceso FIFO')
            for m in memoriaV:
                temp = m[0]
                totalTurn += m[1]
                totalPro += 1
                print(str(temp[2]) + ' = ' + str(m[1]))
            for m in queue:
                temp = m[0]
                totalTurn += m[1]
                totalPro += 1
                print(str(temp[2]) + ' = ' + str(m[1]))  
            
            print('')
            if totalPro != 0:
                print('Turnaround promedio')
                print(totalTurn / totalPro)
                print('')
            #restartear las variables que simulan la memoria antes de volver a empezar con otro proceso
            queue = []
            pageFaults = {}
            memoriaV = []
            memoriaActual = 2048
            memoriaVirtual = 4096





def LRU(comandos):
    print( ' -------------- LRU --------------')
    print('')
    queue = []
    pageFaults = {}
    memoriaV = []
    memoriaActual = 2048
    memoriaVirtual = 4096

    """
    Como se compone nuestra estructura que simula la memoria virtual
    queue de trios
    trios [lista con la informacion del proceso, milisegundos desde que empezo, antiguedad]
    """

   

    for comand in comandos:
        if comand[0] == 'P': # cargar un proceso

            if memoriaActual - comand[1] > 0: #checa si cabe en la memoria
                start = timer()
                trio = [] #crea el trio que se compone del comando y el timestamp
                memoriaActual -= comand[1] #resta la memoria que ocupa ese proceso
                trio.append(comand)
                trio.append(start)
                trio.append(start)
                queue.append(trio) #mete el trio a la queue

                if comand[2] in pageFaults: #agrega al dict de pagefaults que genera cada uno de los procesos
                    pageFaults[comand[2]] += 1
               
                else:
                    pageFaults[comand[2]] = 1

            else: #si no cabe dentro de la memoria, comienza a sacar el primer elemento de la queue hasta que pueda entrar el proceso

                while memoriaActual - comand[1] < 0 and  trio in queue: 
                 #mientras que no quepa dentro de la memoria sigue sacando o mientras que haya elementos en la queue
                        temp = trio[0]
                        memoriaActual += temp[1]
                        memoriaV.append(queue[0]) #mete a memoria virtual los procesos que se van sacando para meter el proceso grande
                        queue.pop(0)

                        if comand[2] in pageFaults: #agrega al dict de pagefaults que genera cada uno de los procesos
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1
                
        if comand[0] == 'L': #libera de la memoria el proceso con el id correspondiente
            oldestPro = -1
            popId = -1
            proTemp = []
            for trio in queue:  #se hace inserta a la lista el tiempo que lleva el proceso dentro
                temp = trio[0]
                
                end = timer()
                start = trio[1]

                trio.pop()
                trio.append(end-start)


            for trio in queue: #saca el id del proceso mas viejo
                temp = trio[2]

                if temp > oldestPro:
                    oldestPro = temp
                    proTemp = trio[0]
                    popId = proTemp[2]




            for trio in queue:
                temp = (trio[0])
                if temp[2] == popId: #saca el proceso mas viejo y se calcula su turnaround time
                    end = timer()
                    start = trio[1]
                    appnd = trio[2]

                    trio.pop()
                    trio.pop()

                    trio.append(end-start) #intercambia los valores para guardar el turnaround
                    trio.append(appnd)
                    memoriaV.append(trio) #mete a memoria virtual el proceso se que libero
                    memoriaVirtual -= trio[1] #actualiza la memoria actual restando los bytes que se ocuparon de la memoria virtual
                    memoriaActual += trio[1] #actualiza la memoria actual agregandole los bytes que se liberaron
                    queue.remove(trio) #saca de la queue el elemento correspondiente

                    
        if comand[0] == 'A': #Leer o modificar un proceso

            if comand[3] == 0: #leer, si no esta en la memoria principal se genera un pagefault
                for trio in queue: 
                    temp = trio[0]
                    
                    if temp[2] == comand[2]:
                        print('Lectura de Proceso '+str(temp))
                        start = timer()
                        trio.pop()
                        trio.append(start)
                        
               
                for trio in memoriaV: #si no esta en la memoria principal se genera un pagefault
                    temp = trio[0]
                    if temp[2] == comand[2]:
                        print('El proceso ' + str(temp) + ' no se encuentra en la memoria principal')

                        if comand[2] in pageFaults:
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1            
 

            if comand[3] == 1: #modificar
                for trio in queue:
                    temp = trio[0]
                    if temp[2] == comand[2]: 
                        trio = []
                        appnd = temp[2]
                        #se intercambian los valores por los nuevos del comando
                        temp.remove(temp[1])
                        temp.remove(temp[1])

                        temp.append(comand[1])
                        temp.append(appnd)


                    
                    else:
                        if comand[2] in pageFaults:
                            pageFaults[comand[2]] += 1
                        else:
                            pageFaults[comand[2]] = 1

    # *************** FIN ***************
    # despliega un reporte de estadsiticas que incluye:
    # - turnaround time de cada proceso que se consider --> diferencia de timestamps
    # - turnaround promedio
    # - nmero de page faults
    # - nmero de page faults por proceso
    # - nmero total de operaciones swap-out swap-in

        if comand[0] == 'F':
            totalPf = 0
            totalTurn = 0
            totalPro = 0
            for f in pageFaults:
                totalPf += pageFaults[f]

            print('Page faults totales: ' + str(totalPf) )
            print('')
            print('Page Faults por id de proceso: ')
            print('')

            for f in pageFaults:
                print( str(f) + ' = ' + str(pageFaults[f]))

            print('Turnaround por proceso LRU')
            print('')
            for m in memoriaV:
                temp = m[0]
                totalTurn += m[1]
                totalPro += 1
                print(str(temp[2]) + ' = ' + str(m[1]))

            for m in queue:
                temp = m[0]
                totalTurn += m[1]
                totalPro += 1
                print(str(temp[2]) + ' = ' + str(m[1]))                
            print('')
            if totalPro != 0:
                print('Turnaround promedio')
                print(totalTurn / totalPro)
            #restartear las variables que simulan la memoria antes de volver a empezar con otro proceso
            queue = []
            pageFaults = {}
            memoriaV = []
            memoriaActual = 2048
            memoriaVirtual = 4096 






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
        
        if words[0] == 'E':
            comando.append(listaLineas[0])

        if words[0] == 'F':
            comando.append(listaLineas[0])
        
        #else:
        
        comandos.append(comando)    
   # print(comandos)
    FIFO(comandos)
    LRU(comandos)
       



if __name__ == '__main__':
    main()