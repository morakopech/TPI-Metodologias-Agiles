def Sumar(numeros):
    if not numeros:
        return 0

    delimitador = ","
    if numeros.startswith("//"):
        delimitador, numeros = numeros.split("\n", 1)
        delimitador = delimitador[2:]

    numeros = numeros.replace("\n", delimitador)

    lista_numeros = numeros.split(delimitador)
    suma = 0
    negativos = []
    for num in lista_numeros:
        num = int(num)
        if num < 0:
            negativos.append(num)
        suma += num

    if negativos:
        raise Exception("no se permiten negativos: " + ", ".join(map(str, negativos)))
    return suma

