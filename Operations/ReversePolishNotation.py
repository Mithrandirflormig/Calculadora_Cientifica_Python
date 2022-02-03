"""
@autor: Mario Alberto Flormig
@github: https://github.com/Mithrandirflormig
"""
from Operations.Stack import Lifo_Queue
import math as mt
#from Stack import Lifo_Queue

class RPN:
    """Clase que crea y evalua expresiones en Notación Polaca Inversa (RPN-Reverse Polish Notation).
    Esta compuesta de los siguientes métodos:
    __init__: Se definen listas con las operaciones a realizar acorde a su aridad, una lista de dígitos y una lista de posibles variables a utilizar (el abecedario casi completo)
    Separating_Elements: Este método se encarga de separar las cadenas de texto introducidas en operadores y operandos, devolviendo una lista.
    Create_RPN: Método que recibe una lista y crea la expresión en su forma RPN, devuelve una lista con los elementos.
    Evaluate_RPN: Método que evalua una expresión en forma RPN, recibe una lista y devuelve un número (en cado de que la operación sea válida).
    """
    def __init__(self):
        self.unaryOperators = ["sin", "cos", "tan", "sin⁻¹", "cos⁻¹", "tan⁻¹", "ln", "log", "√", "!", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh"]
        self.binaryOperators = ["+", "-", "x", "/", "^", "(", ")", "π", "%"]
        self.digits = list(map(chr, range(48,58)))
        self.abc = list(map(chr, range(97,120)))

    def Separating_Elements(self, expr):
        string = ""
        list_elements = []
        expression = expr

        for character in expression:
            if character in self.digits or character == ".":
                string += character
            elif character in self.abc:
                string += character 
            else:
                if string in self.unaryOperators and character == "⁻" or character == "¹":
                    string += character
                else:
                    if string == "" and character in self.binaryOperators:
                        list_elements.append(character)
                    elif string == "" and character in self.unaryOperators:
                        list_elements.append(character)
                    elif string == "":
                        pass 
                    else:
                        list_elements.append(string)
                        string = ""
                        list_elements.append(character)
        if string != "":
            list_elements.append(string)

        return list_elements


    def Create_RPN(self, list_elements):
        priority_operator = {
        "(" : 0,
        "+" : 1,
        "-" : 1,
        "x" : 2,
        "/" : 2,
        "%" : 2,
        "sin" : 3,
        "cos" : 3,
        "tan" : 3,
        "sin⁻¹" : 3,
        "cos⁻¹" : 3,
        "tan⁻¹" : 3,
        "ln" : 3,
        "√" : 3,
        "^" : 3,
        "!" : 3,
        "|" : 3
        }

        Intermediate_stack = Lifo_Queue()
        Final_Stack = []

        for element in list_elements:
            if element[0].isdigit() or element == "π":
                Final_Stack.append(element)
            elif element == "(":
                Intermediate_stack.push(element)
            elif element == ")":
                pop_element = Intermediate_stack.pop()
                while pop_element != "(":
                    Final_Stack.append(pop_element)
                    pop_element = Intermediate_stack.pop()
            else:
                while (not Intermediate_stack.empty()) and (priority_operator[element] <= priority_operator[Intermediate_stack.peek()]):
                    Final_Stack.append(Intermediate_stack.pop())
                Intermediate_stack.push(element)

        while not Intermediate_stack.empty():
            Final_Stack.append(Intermediate_stack.pop())

        return Final_Stack


    def Evaluate_RPN(self, Final_Stack, angle):
        Operations_Stack = Lifo_Queue()      

        for element in Final_Stack:
            try:
                if element == "π":
                    num = mt.pi 
                elif "." in element:
                    num = float(element)  
                else:
                    num = int(element)
                Operations_Stack.push(num)
            except ValueError:
                if element not in self.unaryOperators and element not in self.binaryOperators:
                    raise ValueError(f"La operación {element} no es válida")       
                try:
                    if element in self.unaryOperators:
                        op = Operations_Stack.pop()
                    elif element in self.binaryOperators:
                        op1 = Operations_Stack.pop()
                        op2 = Operations_Stack.pop()
                except IndexError:
                    raise ValueError("Faltan elementos a operar. La expresión ingresada no es correcta")

                if element == self.unaryOperators[0]:
                    if angle == "RAD":
                        r = mt.sin(op)
                    else:
                        r = mt.sin(mt.radians(op))
                elif element == self.unaryOperators[1]:
                    if angle == "RAD":
                        r = mt.cos(op)
                    else:
                        r = mt.cos(mt.radians(op))
                elif element == self.unaryOperators[2]:
                    if angle == "RAD":
                        r = mt.tan(op)
                    else:
                        r = mt.tan(mt.radians(op))
                elif element == self.unaryOperators[3]:
                    if angle == "RAD":
                        r = mt.asin(op)
                    else:
                        r = mt.asin(mt.radians(op))
                elif element == self.unaryOperators[4]:
                    if angle == "RAD":
                        r = mt.acos(op)
                    else:
                        r = mt.acos(mt.radians(op))
                elif element == self.unaryOperators[5]:
                    if angle == "RAD":
                        r = mt.atan(op)
                    else:
                        r = mt.atan(mt.radians(op))
                elif element == self.unaryOperators[6]:
                    r = mt.log(op)
                elif element == self.unaryOperators[7]:
                    r = mt.log10(op)
                elif element == self.unaryOperators[8]:
                    r = mt.sqrt(op)
                elif element == self.unaryOperators[9]:
                    r = mt.factorial(op)
                elif element == self.unaryOperators[10]:
                    if angle == "RAD":
                        r = mt.sinh(op)
                    else:
                        r = mt.sinh(mt.radians(op))
                elif element == self.unaryOperators[11]:
                    if angle == "RAD":
                        r = mt.cosh(op)
                    else:
                        r = mt.cosh(mt.radians(op))
                elif element == self.unaryOperators[12]:
                    if angle == "RAD":
                        r = mt.tanh(op)
                    else:
                        r = mt.tanh(mt.radians(op))
                elif element == self.unaryOperators[13]:
                    if angle == "RAD":
                        r = mt.asinh(op)
                    else:
                        r = mt.asinh(mt.radians(op))
                elif element == self.unaryOperators[14]:
                    if angle == "RAD":
                        r = mt.acosh(op)
                    else:
                        r = mt.acosh(mt.radians(op))
                elif element == self.unaryOperators[15]:
                    if angle == "RAD":
                        r = mt.atanh(op)
                    else:
                        r = mt.atanh(mt.radians(op))
                elif element == self.binaryOperators[0]:
                    if isinstance(op2, float) == True or isinstance(op1, float) == True:
                        r = float(op2) + float(op1)
                    else:
                        r = op2 + op1 
                elif element == self.binaryOperators[1]:
                    if isinstance(op2, float) == True or isinstance(op1, float) == True:
                        r = float(op2) - float(op1)
                    else:
                        r = op2 - op1 
                elif element == self.binaryOperators[2]:
                    r = op2 * op1
                elif element == self.binaryOperators[3]:
                    r = op2 / op1
                elif element == self.binaryOperators[4]:
                    r = op2 ** op1
                elif element == self.binaryOperators[8]:
                    r = (op2 * op1) / 100

                Operations_Stack.push(r)

        result = Operations_Stack.pop()
        if Operations_Stack.empty():
            return result
        else:
            raise ValueError("Sobran elementos a operar. La expresión ingresada no es correcta")

path_operations = r'C:\Users\Mario Alberto\Documents\Cursos extracurriculares\Cosas nuevas python\Calculadora_gráfica\Calculadora_version2\Operations\operaciones.txt'  
path_results = r'C:\Users\Mario Alberto\Documents\Cursos extracurriculares\Cosas nuevas python\Calculadora_gráfica\Calculadora_version2\Operations\resultados.txt'  


'''
expresion = RPN()

with open(path_operations, 'r', encoding = 'utf-8') as operation, open(path_results, 'r', encoding = 'utf-8') as result:
    lines_op = operation.readlines()
    lines_re = result.readlines()
    for line in range(len(lines_op)):
        operation = lines_op[line].strip()
        result = lines_re[line].strip()
        #print(type(operation))
        lista_elementos = expresion.Separating_Elements(operation)
        rpn = expresion.Create_RPN(lista_elementos)
        resultado = expresion.Evaluate_RPN(rpn)
        print(f"Lista de elementos: {lista_elementos}")
        print(f"Notación Polaca Inversa: {rpn}")
        print(f"Resultado programa: {resultado}")
        print(f"Resultado: {result}")
        print("============================================================================================================\n")
        #print(operation)
'''

'''expresion = RPN()
lista = expresion.Separating_Elements('sin⁻¹(25)')
print(lista)
Stack_final = expresion.Create_RPN(lista)
print(Stack_final)
Resultado = expresion.Evaluate_RPN(Stack_final, "RAD")
print(Resultado)'''

