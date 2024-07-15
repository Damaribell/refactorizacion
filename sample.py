def ingresar_puntos_y_comentarios():
    while True:
        print('Ingrese una calificación del 1 al 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Ingrese un valor de 1 a 5')
            else:
                print('Ingrese su comentario')
                comment = input()
                post = f'Puntos: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Ingrese los puntos de evaluación en números')

def verificar_resultados():
    print('Resultados hasta ahora')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def seleccionar_proceso():
    while True:
        print('Seleccione la operación que desea realizar')
        print('1: Ingresar puntos de evaluación y comentarios')
        print('2: Verificar los resultados hasta ahora')
        print('3: Salir')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntos_y_comentarios()
            elif num == 2:
                verificar_resultados()
            elif num == 3:
                print('Saliendo')
                break
            else:
                print('Ingrese un número del 1 al 3')
        else:
            print('Ingrese un número del 1 al 3')

seleccionar_proceso()