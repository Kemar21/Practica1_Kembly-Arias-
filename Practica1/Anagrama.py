# funcion con dos parametros. Anagrama
def detectorAnagrama(c, b):
    sorted(c)
    sorted(b)
    return c == b


def anagrama():
    c = input('Ingrese la primera palabra\n')
    b = input('Ingrese la segunda palabra\n')
    return detectorAnagrama(c, b)


print(anagrama())