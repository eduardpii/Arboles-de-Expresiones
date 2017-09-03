class Pila:#Clase pila
    def __init__(self):
        self.items=[]

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []

class Nodo():#clase arbol
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der
        
#Esta función convierte la lista,en una pila.
def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":#evalua los operadores
            nodo_der = pila.desapilar()#Desapila debido a la posfija
            nodo_izq = pila.desapilar()#Desapila debido a la posfija
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))#apila los nodos
        else:
            pila.apilar(Nodo(lista[0]))#apila nodos
        return convertir(lista[1:],pila)#recursividad
    
#Esta función resuelve el árbol           
def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    
expresion = input("Ingrese una expresión en POSFIJA: ").split(" ")

pila = Pila()

convertir(expresion, pila)

print (evaluar(pila.desapilar()))
