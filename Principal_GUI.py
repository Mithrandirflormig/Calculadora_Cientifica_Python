"""
@autor: Mario Alberto Flormig
@github: https://github.com/Mithrandirflormig
"""
from tkinter import *
from tkinter import messagebox
from Scientist.Scientist_GUI import Scientist_GUI
from Graph.Graph_GUI import Graph_GUI


class Principal_Container:
    """Clase encargada de gestionar las instancias de las correspondientes GUI's para cada funcionalidad de la calculadora.
    Los métodos se encuentran 
    De momento cuenta con dos modos:
    - Calculadora Científica
    - Calculadora Gráfica """

    principal_frame = None
    def __init__(self, root):
        """El constructor de la clase requiere de un objeto de tipo Tk, que funja como raíz principal"""
        self.root = root
        self.root.title("Calculadora Estándar")
        self.root.resizable(0,0)
        self.root.config(cursor = "hand1")
        self.__Menu_bar()
        self.__Type_Calculator("Scientist")

    def __Menu_bar(self):
        """Barra de Menú"""
        menu_bar = Menu(self.root)
        btn_file = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "≡", menu = btn_file)
        btn_file.add_command(label = "Científica", command = lambda:self.__Type_Calculator("Scientist"))
        btn_file.add_command(label = "Gráfica", command = lambda:self.__Type_Calculator("Graph"))
        btn_file.add_separator()
        btn_file.add_command(label = "Información", command = lambda:self.__Info())
        btn_file.add_command(label = "Acerca de", command = lambda:self.__About())
        self.root.config(menu = menu_bar)

    def __Type_Calculator(self, gui_type):
        #Dependiendo el botón que se accione, dará una interface u otra.
        if gui_type == "Scientist":
            self.__Scientist()
        elif gui_type == "Graph":
            self.__Graph()

    def __Scientist(self):
        #Frame Principal que contiene a los widgets de la calculadora
        if self.principal_frame:
            self.principal_frame.destroy() 
        self.root.title("Calculadora Científica")
        self.root.geometry("420x440")
        self.root.resizable(0,0)
        self.root.minsize(width=420,height=440)
        self.principal_frame = Frame(self.root)
        self.principal_frame.pack()
        self.principal_frame.config(bg = "#082b96")
        self.display_frame = Scientist_GUI(self.principal_frame)
        
    def __Graph(self):
        #Frame Principal que contiene a los widgets de la parte gráfica
        if self.principal_frame:
            self.principal_frame.destroy()
        self.root.title("Ventana Gráfica")
        self.root.resizable(0,0)
        #self.root.geometry("642x535")
        self.root.minsize(width = 642, height = 612)
        self.principal_frame = Frame(self.root, bg ='gray22', bd = 3)
        self.principal_frame.pack()
        self.principal_frame.config(bg = "#393956")
        self.display_frame = Graph_GUI(self.principal_frame)

    def __Info(self):
        messagebox.showinfo("Calculadora Científica", """
- Type: Te permite alternar entre funciones trigonométricas usuales o hiperbólicas.
- Rad/Deg: Te permite realizar el calculo en radianes o degrados.
- Ventana Gráfica: La función, el rango en x e y son parámetros obligatorios para poder realizar la gráfica correctamente. El movimiento de ciertas gráficas es genérico, es decir, un desplazamiento de 1/40 para cada valor que toma y. Pueden modificarlo a su conveniencia.""")

    def __About(self):
        messagebox.showinfo("Calculadora Científica", """
        - Versión 1.0 (Beta)
        - Sistema Operativo: Windows 10
        - Dependencias: Tkinter, Numpy, Matplotlib, Sympy
        - Autor: Mario Al. Flormig""")
        


root = Tk()
Principal_Container(root)
root.mainloop()