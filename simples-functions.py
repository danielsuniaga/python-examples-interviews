"""

1. Function to determine the greatest of two numbers

"""

def funcion_max(n1,n2):
    
    if (n1>n2):
    
        return n1
    
    else:
    
        return n2
    

print(funcion_max(500,400))

print("--------------------------------------------------------")

"""

2. max_de_tres() function that takes three numbers as arguments and returns the largest of them. 

"""

def funcion_max_de_tres(n1,n2,n3):

    if (n1>n2) and (n1>n3):
    
        return n1
    
    elif(n2>n1) and (n2>n3):

        return n2
    
    else:

        return n3
    
print(funcion_max_de_tres(10,20,30))

print("--------------------------------------------------------")

"""

3. is_vocal function determine if the character sent is a vowel. 

"""

def is_vocal(caracter):

    _lista_vocales=['a','e','i','o','u']

    if caracter in _lista_vocales:

        return True
    
    else:
        
        return False
    

print(is_vocal('a'))

print("--------------------------------------------------------")

"""

4. suma function that adds the elements of a list. 

"""


def suma(lista):

    _result = 0

    for n in lista:

        _result = _result + (n)

    return _result

print(suma([1,2,-1]))

print("--------------------------------------------------------")

"""

5. multi function that multiplies the elements of a list. 

"""

def multi(lista):

    _result = 1

    for n in lista:

        _result = _result * (n)

    return _result

print(multi([1,2,3]))

print("--------------------------------------------------------")

"""

6. inversa function reverse a string. 

"""

def inversa(cadena):

    _result = ""

    for n in reversed(cadena):

        _result +=n

    return _result   

print(inversa("cadena"))

print("--------------------------------------------------------")

"""

6. is_palindroma function identifies if string is palindrome

"""

def is_palindroma(cadena):

    _cadena_inversa=inversa(cadena).replace(" ","").lower()

    cadena=cadena.replace(" ","").lower()

    return True if  (_cadena_inversa==cadena) else False


print("Es palindroma: "+str(is_palindroma("Sometamos o matemos")))

print("--------------------------------------------------------")

"""

7. superposicion function Analyzes the elements of a list and identifies if they have elements in common.

"""

def superposicion(lista1,lista2):

    for i in lista1: 

        if  i in lista2:

            return True
        
    return False

print("Listas parecidas: "+str(superposicion([1,2,3],[1,4,5])))

print("--------------------------------------------------------")

"""

7. generar_n_caracteres function generates characters according to the parameter sent

"""

def generar_n_caracteres(caracter,cantidad):

    _result =""

    for n in range(cantidad):

        _result +=caracter

    return _result

print("Multiplicando caracteres: "+generar_n_caracteres("x",5))

print("--------------------------------------------------------")

"""

8. procedimiento function generate a histogram with * and based on the submitted list

"""

def procedimiento(lista):

    for n in lista: 

        histograma = "*" * n

        print(f'{histograma}\n')


procedimiento([7,3,5])

print("--------------------------------------------------------")
