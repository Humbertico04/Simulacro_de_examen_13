# ¡Empiezas a trabajar para una nueva empresa elegante que espera revolucionar las redes
# sociales! ¡JADEAR! Tuvieron esta gran idea de que los usuarios deberían poder especificar
# palabras clave relevantes para sus publicaciones utilizando una idea ingeniosa al anteponer
# esas palabras clave con el signo de libra (#). Su trabajo es extraer esas palabras clave para que
# puedan usarse más tarde para cualquier propósito.
# Nota:
# • Los signos de libra por sí solos no cuentan, por ejemplo: la cadena "#" devolvería una
# matriz vacía.
# • Si una palabra está precedida por más de un hashtag, solo cuenta el último hashtag
# (por ejemplo, "##alot" devolvería ["alot"])
# • Los hashtags no pueden estar en medio de una palabra (por ejemplo, "hashtag en
# #línea" devuelve una matriz vacía)
# • Los hashtags deben preceder a los caracteres alfabéticos (por ejemplo, "#120398" o
# "#?" no son válidos)
# Entrada: cadena de palabras, donde algunas palabras pueden contener un hashtag.
# Salida: matriz de cadenas que tenían el prefijo del hashtag, pero que no contienen el hashtag.


#Bucle que detecte si hay un # en la cadena
#Si hay un #, detectar la palabra que sigue al #
#Si la palabra que sigue al # es alfabética, añadirla a la lista
#Si la palabra que sigue al # no es alfabética, no añadirla a la lista
#Si no hay un #, no añadir nada a la lista

def checkio(text):
    lista = []
    for i in range(len(text)):
        if text[i] == "#":
            palabra = text[i+1:]
            
            if palabra[0].isalpha():
                lista.append(palabra)
    return print(lista)


checkio("#h6a678shtag")
checkio("#h6a678shtag #h6a678shtag")