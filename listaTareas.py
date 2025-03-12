tareas=['lavar', 'hacer aseo', 'barrer', 'trapear']

def create(tarea):
    tareas.append(tarea)
    
def delete(tareas):
    #buscar
    #eliminar por posicion
    tareas.remove(tareas)

def get():
    for tarea in tareas:
        print(tarea)


menu = "1. Adiccionar  2.Eliminar 3.Listar"
opc=input("Seleccione una opción: " + menu)

print (opc)

if (opc == "1"):
    tarea = input("Ingresa la tarea a agregar ")
    create(tarea)
    get()
    
elif (opc == "2"):
    tarea = input("Ingresa la tarea a eliminar ")
    delete(tarea)
    get()
    
elif(opc == "3"):
    get()
    