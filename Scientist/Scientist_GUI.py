"""
@autor: Mario Alberto Flormig
@github: https://github.com/Mithrandirflormig
"""
from tkinter import *
from tkinter.font import Font
from Operations.Clear_Display import del_display
from Operations.ReversePolishNotation import RPN

class Scientist_GUI:
    """Clase encargada de gestionar los widgets de la calculadora y las variables de control.
    Contiene los siguiente métodos:
    _ __init__: Se definen las variables de control que podrán cambiar a lo largo de la ejecución del programa
    - Standard_Display: Método en donde se construye la pantalla de la calculadora.
    - Font_Style: Tipo y tamaño de letras que se muestra en la pantalla.
    - SetDisplayValues: Método que establece los diversos carácteres en la pantalla.
    - Operations: Método que crea un objeto de la clase RPN y gestiona el resultado de aplicar las distintas operaciones.
    - Change_Raddeg: Nos permite cambiar entre radianes y degrados estableciendo el valor en el atributo radeg.
    - Change_TypeTri: Nos permite cambiar entre funciones trigonométrica usuales e hiperbólicas.
    - Scientist_Buttons: Construye y posiciona los botones de la calculadora."""
    display_num = None

    def __init__(self, parent):
        self.parent = parent
        
        #Variable de control
        self.display_num = StringVar()
        self.radeg = StringVar()
        self.sinh = StringVar()
        self.cosh = StringVar()
        self.tanh = StringVar()
        self.asinh = StringVar()
        self.acosh = StringVar()
        self.atanh = StringVar()
        self.radeg.set("RAD")
        self.sinh.set("sin")
        self.cosh.set("cos")
        self.tanh.set("tan")
        self.asinh.set("sin⁻¹")
        self.acosh.set("cos⁻¹")
        self.atanh.set("tan⁻¹")

        #Estableciendo un valor inicial en la pantalla
        self.display_num.set("0")

        #Creando la pantalla
        self.Standard_Display()

    def Font_Style(self):
        font = Font(family = "Helvetica", size = 24)
        return font

    def Standard_Display(self):
        #Instancia del frame que contiene el display
        child_frame = Frame(self.parent, width = "370", height = "200")
        child_frame.pack_propagate(False)
        child_frame.grid(row = 1, column = 1, padx = 15, pady = 15, columnspan = 5)

        #Display simulado mediante un Entry
        display = Entry(child_frame, textvariable = self.display_num, bd = 20, font = self.Font_Style(), state = "disabled")
        display.pack(fill = "both", expand = 1)
        display.config(bg = "#D4D2DD", fg = "black", justify = "right")

        #Generando botones
        self.Scientist_Buttons()

    def SetDisplayValues(self, caracter):
        if self.display_num.get() == "0" and caracter == "0":
            self.display_num.set(caracter)
        elif ("." in self.display_num.get()) and caracter == ".":
            self.display_num.set(self.display_num.get())
        elif self.display_num.get() == "0" and caracter != "0":
            self.display_num.set(caracter)
        else:
            self.display_num.set(self.display_num.get() + caracter)

    def Operations(self):
        try:
            rpn = RPN()
            elements = rpn.Separating_Elements(self.display_num.get())
            rpn_expr = rpn.Create_RPN(elements)
            result = rpn.Evaluate_RPN(rpn_expr, self.radeg.get())
            self.display_num.set(result)
        except Exception:
            self.display_num.set("SYNTAX ERROR")

    def Change_Raddeg(self):
        if self.radeg.get() == "DEG":
            self.radeg.set("RAD")
        else:
            self.radeg.set("DEG")
        self.Scientist_Buttons()

    def Change_TypeTri(self):
        if self.sinh.get() == "sin":
            self.sinh.set("sinh")
            self.cosh.set("cosh")
            self.tanh.set("tanh")
            self.asinh.set("asinh")
            self.acosh.set("acosh")
            self.atanh.set("atanh")
        else:
            self.sinh.set("sin")
            self.cosh.set("cos")
            self.tanh.set("tan")
            self.asinh.set("sin⁻¹")
            self.acosh.set("cos⁻¹")
            self.atanh.set("tan⁻¹")
        self.Scientist_Buttons()

    def Scientist_Buttons(self):
        #Primera fila
        b_abs = Button(self.parent, text = "Type", width = 8, relief = "raised",command = lambda:self.Change_TypeTri())
        b_abs.config(bg = "#281A58", fg = "#D4D2DD")

        b_percent = Button(self.parent, text = "%", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("%"))
        b_percent.config(bg = "#281A58", fg = "#D4D2DD")

        b_sqrt = Button(self.parent, text = "√▥", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("√("))
        b_sqrt.config(bg = "#281A58", fg = "#D4D2DD")

        b_pow = Button(self.parent, text = "xⁿ", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("^("))
        b_pow.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        b_fact = Button(self.parent, text = "!", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("!"))
        b_fact.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        #Segunda fila
        b_sin = Button(self.parent, text = self.sinh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.sinh.get() + "("))
        b_sin.config(bg = "#281A58", fg = "#D4D2DD")

        b_cos = Button(self.parent, text = self.cosh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.cosh.get() + "("))
        b_cos.config(bg = "#281A58", fg = "#D4D2DD")

        b_tan = Button(self.parent, text = self.tanh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.tanh.get() + "("))
        b_tan.config(bg = "#281A58", fg = "#D4D2DD")

        b_ln = Button(self.parent, text = "ln", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("ln("))
        b_ln.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        b_log = Button(self.parent, text = "log", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("log("))
        b_log.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        #Tercera fila
        b_arcsin = Button(self.parent, text = self.asinh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.asinh.get() + "("))
        b_arcsin.config(bg = "#281A58", fg = "#D4D2DD")

        b_arccos = Button(self.parent, text = self.acosh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.acosh.get() + "("))
        b_arccos.config(bg = "#281A58", fg = "#D4D2DD")

        b_arctan = Button(self.parent, text = self.atanh.get(), width = 8, relief = "raised", command = lambda:self.SetDisplayValues(self.atanh.get() + "("))
        b_arctan.config(bg = "#281A58", fg = "#D4D2DD")

        b_parA = Button(self.parent, text = "(", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("("))
        b_parA.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        b_parB = Button(self.parent, text = ")", width = 9, relief = "raised", command = lambda:self.SetDisplayValues(")"))
        b_parB.config(bg = "#281A58", fg = "#D4D2DD", font = ("Arial", 11))

        #Cuarta fila
        b_9 = Button(self.parent, text = "9", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("9"))
        b_9.config(bg = "#281A58", fg = "#D4D2DD")

        b_8 = Button(self.parent, text = "8", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("8"))
        b_8.config(bg = "#281A58", fg = "#D4D2DD")

        b_7 = Button(self.parent, text = "7", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("7"))
        b_7.config(bg = "#281A58", fg = "#D4D2DD")

        b_del = Button(self.parent, text = "⌫", width = 9, relief = "raised", command = lambda:del_display(self.display_num))
        b_del.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        b_cls = Button(self.parent, text = "Cls", width = 9, relief = "raised", command = lambda:self.display_num.set("0"))
        b_cls.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        #Quinta fila
        b_4 = Button(self.parent, text = "4", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("4"))
        b_4.config(bg = "#281A58", fg = "#D4D2DD")

        b_5 = Button(self.parent, text = "5", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("5"))
        b_5.config(bg = "#281A58", fg = "#D4D2DD")

        b_6 = Button(self.parent, text = "6", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("6"))
        b_6.config(bg = "#281A58", fg = "#D4D2DD")

        b_mult = Button(self.parent, text = "x", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("x"))
        b_mult.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        b_div = Button(self.parent, text = "÷", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("/"))
        b_div.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        #Sexta fila
        b_1 = Button(self.parent, text = "1", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("1"))
        b_1.config(bg = "#281A58", fg = "#D4D2DD")

        b_2 = Button(self.parent, text = "2", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("2"))
        b_2.config(bg = "#281A58", fg = "#D4D2DD")

        b_3 = Button(self.parent, text = "3", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("3"))
        b_3.config(bg = "#281A58", fg = "#D4D2DD")

        b_suma = Button(self.parent, text = "+", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("+"))
        b_suma.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        b_resta = Button(self.parent, text = "-", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("-"))
        b_resta.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        #Septima fila
        b_point = Button(self.parent, text = ".", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("."))
        b_point.config(bg = "#281A58", fg = "#D4D2DD")

        b_0 = Button(self.parent, text = "0", width = 8, relief = "raised", command = lambda:self.SetDisplayValues("0"))
        b_0.config(bg = "#281A58", fg = "#D4D2DD")

        b_equal = Button(self.parent, text = "=", width = 8, relief = "raised", command = lambda:self.Operations())
        b_equal.config(bg = "#281A58", fg = "#D4D2DD")

        b_pi = Button(self.parent, text = "π", width = 9, relief = "raised", command = lambda:self.SetDisplayValues("π"))
        b_pi.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        b_rad = Button(self.parent, text = self.radeg.get(), width = 9, relief = "raised", command = lambda:self.Change_Raddeg())
        b_rad.config(bg = "#741C0D", fg = "#D4D2DD", font = ("Arial", 11))

        #Orillas
        l_orillaA = Label(self.parent)
        l_orillaA.grid(row = 0, column = 0, sticky = "nswe", rowspan = 10)
        l_orillaA.config(bg = "#768AE3")

        l_orillaB = Label(self.parent)
        l_orillaB.grid(row = 0, column = 7, sticky = "nswe", rowspan = 10)
        l_orillaB.config(bg = "#768AE3")

        #Posicionando los botones
        lista_botones = [
            b_abs, b_percent, b_sqrt, b_pow, b_fact,
            b_sin, b_cos, b_tan, b_ln, b_log,
            b_arcsin, b_arccos, b_arctan, b_parA, b_parB,
            b_9, b_8, b_7, b_del, b_cls,
            b_4, b_5, b_6, b_mult, b_div,
            b_1, b_2, b_3, b_suma, b_resta,
            b_point, b_0, b_equal, b_pi, b_rad
        ]
        rows = len(lista_botones) // 5
        columns = 5
        init = 0
        cont = 1

        for row in range(0,rows):
            for column in range(init,columns):
                lista_botones[column].grid(row = row+2, column = cont)
                cont += 1
            cont = 1

            columns += 5
            init += 5









        



