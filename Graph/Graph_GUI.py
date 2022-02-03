"""
@autor: Mario Alberto Flormig
@github: https://github.com/Mithrandirflormig
"""
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sympy as sp

class Graph_GUI:
    """Clase encargada de gestionar widgets y variable de control de la parte gráfica
    Esta clase contiene los siguiente métodos:
    - __init__: Se definen las variables de control que almacenan el contenido de lo que ingrese.
    - Graph_Display: Establece la forma inicial que tiene la pantalla que mostrará la gráfica.
    - Widgets_Zone: Establece Labels y Entrys que se mostraran en la ventana
    - Clear_Display: Reestablece la pantalla inicial
    - Get_Graph: Obtiene el rango en x,y y la expresión ingresada por el usuario para posteriormente graficar
    - Animation_Init: Actualiza el canvas y produce una animación de una gráfica existente.
    - Animate: Método encapsulado que produce una animación específica para las coordenadas en y
    - Stop_Animate: Detiene la animación
    """
    x = None
    y = None
    fig = None
    ax = None
    frame_sup = None
    canvas = None
    ani = None
    line = None

    def __init__(self, parent):
        self.parent = parent

        #Variables de control
        self.expression = StringVar()
        self.range_x = StringVar()
        self.range_y = StringVar()

        self.Graph_Display()
        self.Widgets_Zone()


    def Graph_Display(self):
         #Frame que contendrá a la figura
        self.frame_sup = Frame(self.parent)
        self.frame_sup.grid(row = 0, column = 0, columnspan = 4)

        self.fig, self.ax = plt.subplots(facecolor = "#424874")
        self.ax.tick_params(direction = 'out', length = 5, width = 1, colors = 'white')
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame_sup)
        self.canvas.get_tk_widget().pack(expand = 1, fill = 'both')

    def Widgets_Zone(self):
        #zona de labels y entrys
        exp_label = Label(self.parent, text = "Ingresa una expresión: ", font = ("Helvetica", 12), bg = "#393956", fg = "white")
        exp_label.grid(row = 1, column = 0, padx = 15, pady = 5, sticky = "w")
        ranx = Label(self.parent, text = "Rango de x: ", font = ("Helvetica", 12), bg = "#393956", fg = "white")
        ranx.grid(row = 2, column = 0, padx = 15, pady = 5, sticky = "w")
        rany = Label(self.parent, text = "Rango de y: ", font = ("Helvetica", 12), bg = "#393956", fg = "white")
        rany.grid(row = 3, column = 0, padx = 15, pady = 5, sticky = "w")

        exp_entry = Entry(self.parent, textvariable = self.expression, font = ('Arial black', 12))
        exp_entry.grid(row = 1, column = 2, ipadx = 10)
        ranx_entry = Entry(self.parent, textvariable = self.range_x, font = ('Arial black', 12)) 
        ranx_entry.grid(row = 2, column = 2, ipadx = 10)
        rany_entry = Entry(self.parent, textvariable = self.range_y, font = ('Arial black', 12)) 
        rany_entry.grid(row = 3, column = 2, ipadx = 10)

        #zona de botones
        graph = Button(self.parent, text = "Graficar", width = 8, relief = "raised", command = lambda:self.Get_Graph())
        graph.config(bg = "#424874", fg = "white")
        graph.grid(row = 5, column = 0, sticky = "w")

        animate = Button(self.parent, text = "Animar", width = 8, relief = "raised", command = lambda: self.Animation_Init())
        animate.config(bg = "#424874", fg = "white")
        animate.grid(row = 5, column = 1, sticky = "w")

        stop = Button(self.parent, text = "Detener", width = 8, relief = "raised", command = lambda: self.Stop_Animate())
        stop.config(bg = "#424874", fg = "white")
        stop.grid(row = 5, column = 2, sticky = "w")

        clean = Button(self.parent, text = "Borrar", width = 8, relief = "raised", command = lambda: self.Clear_Display())
        clean.config(bg = "#424874", fg = "white")
        clean.grid(row = 5, column = 3, sticky = "w")

    def Clear_Display(self):
        self.Graph_Display()
        self.expression.set("")
        self.range_x.set("")
        self.range_y.set("")

    def Get_Graph(self):
        x_range = self.range_x.get().split(",")
        y_range = self.range_y.get().split(",")
        s = sp.Symbol('x')
        self.x = np.arange(float(x_range[0]), float(x_range[1]), 0.001)
        self.y = sp.lambdify(s, self.expression.get())
        self.line, = self.ax.plot(self.x, self.y(self.x), color='violet', marker='o', linestyle='dotted', linewidth = 6, markersize = 1, markeredgecolor = 'm')
        plt.xlim([float(x_range[0]), float(x_range[1])])
        plt.ylim([float(y_range[0]), float(y_range[1])])
        self.canvas.draw()

    def Animation_Init(self):
        self.ani = animation.FuncAnimation(self.fig, self.__Animate, interval = 20, blit = True, save_count = 10, repeat = True)
        self.canvas.draw()

    def __Animate(self, i):
        #self.line.set_xdata(self.x + i/40)
        self.line.set_ydata(self.y(self.x + i/40))
        return self.line,
        
    def Stop_Animate(self):
        self.ani.event_source.stop()
