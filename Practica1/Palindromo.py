#Funcion para comprobar cuando un conjunto de caracteres son palindromo
def detectorDePalindromo(a):
    return a == a[::-1]

def Palindroma():
    a = input("Ingrese los caracteres o una palabra para verificar si es palindroma o no\n")
    return detectorDePalindromo(a)

print(Palindroma())
