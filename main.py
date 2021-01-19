
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

def transListas (arch,cad):
    for i in cad:
        arch.append(f'{i}')
    return arch


def start (cad):
    archivo = open('cadena.txt', 'w')
    cero = cad.count('0')
    uno = cad.count('1')
    arch = []
    if cero >= uno:
        if cad.index('0') == 0:
            pila = Stack()
            arch = transListas(arch, cad)
            arch1 = arch.copy()
            archivo.write(f'(q, {arch}, {pila}Z0)+')
            for i in cad:
                if cad.index(i) == 0:
                    pila.Add('X')
                else:
                    if len(pila) == 0:
                        print('Error pila vacia')
                        exit()
                    else:
                        pila.Remove()
                del arch[0]
                if len(arch) == 0:
                    if len(pila) == 0:
                        archivo.write(f'(q, e, Z0)+(f, e, Z0)\n')
                    else:
                        archivo.write(f'(q, e, {pila}Z0)+(f, e, {pila}Z0)\n')
                else:
                    archivo.write(f'(q, {arch}, {pila}Z0)+')
                print(pila)
            if len(pila) == 0:
                archivo.write(f'(q, {arch1}, Z0)+*(f, e, Z0) ')
            else:
                archivo.write(f'(q, {arch1}, Z0)+*(f, e,{pila} Z0) ')
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
