
import random as rd

class Stack:
    def __init__(self):
        self.Stack = []

    def Add (self, Element):
        self.Stack.append(Element)
        return self.Stack

    def Remove (self):
        self.Stack.pop()
        return self.Stack

    def __str__(self):
        return str(self.Stack)

    def __len__(self):
        return len(self.Stack)


def manual ():
    cad = input('Ingrese una cadena compuesta de 1 y 0 :')
    start(cad)

def auto ():
    k = rd.randint(1, 10)
    cad = ''

    for i in range(k):
        j = rd.randint(0, 1)
        cad = f'{cad}{j}'
    print(cad)
    start(cad)

def salir():
    exit()

def handle_error ():
    mss = 'Opcion invalida\n'
    return mss

def start (cad):
    cero = cad.count('0')
    uno = cad.count('1')
    if cero >= uno:
        if cad.index('0') == 0:
            pila = Stack()
            for i in cad:
                if cad.index(i) == 0:
                    pila.Add('X')
                else:
                    if len(pila) == 0:
                        print('Error pila vacia')
                        exit()
                    else:
                        pila.Remove()

                print(pila)
            exit()
        else:
            print('La cadena no inicia con 0')
            exit()
    else:
        print('Muchos 1 y pocos 0')
        exit()


if __name__ == '__main__':

    print('''
        1.-Manual
        2.-Automatica
        3.-Salir
         ''')
    op = int(input('Ingrese una opcion: '))
    opc = [manual, auto, salir]
    output = opc[op-1]()
    print(opc)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
