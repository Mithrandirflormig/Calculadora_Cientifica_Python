#Función encargada de limpiar la pantalla caracter a caracter
def del_display(display_num):
    if len(display_num.get()):
        lista_aux = list(display_num.get())[:-1]
        if len(lista_aux) == 0:
            display_num.set("0")
        else:
            display_num.set(''.join(lista_aux))
