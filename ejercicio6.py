# Escriba una rotate que gire una matriz bidimensional (una matriz) ya sea en sentido horario o
# antihorario 90 grados y devuelva la matriz rotada.
# La función acepta dos parámetros: una matriz y una cadena que especifica la dirección o
# rotación. La dirección será "clockwise"o "counter-clockwise".
# Aquí hay un ejemplo de cómo se usará su función:
# var matrix = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]];
# rotate(matrix, "clockwise"); // Would return [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# Para ayudarlo a visualizar la matriz rotada, aquí está formateada como una cuadrícula:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
# Girado en sentido contrario a las agujas del reloj se vería así:
# [[3, 6, 9],
#  [2, 5, 8],
#  [1, 4, 7]]

matrix=[[1,2,3,0],
        [4,5,6,0],
        [7,8,9,0]]

# Extra:
# def traspuesta(matrix):
#     mat=[]
#     for i in range(len(matrix[0])): #3
#         mataux=[]
#         for j in range(len(matrix)): #4
#             mataux.append(matrix[j][i])
#         mat.append(mataux)
#     return mat

def counter_clockwise(matrix):
    mat=[]
    for i in reversed(range(len(matrix[0]))): #3
        mataux=[]
        for j in range(len(matrix)): #4
            mataux.append(matrix[j][i])
        mat.append(mataux)
    return mat

def clockwise(matrix):
    mat=[]
    for i in range(len(matrix[0])): #3
        mataux=[]
        for j in range(len(matrix)): #4
            mataux.append(matrix[::-1][j][i])
        mat.append(mataux)
    return mat

def rotate(matrix, direccion):
    if direccion=="counter-clockwise":
        return counter_clockwise(matrix)
    elif direccion=="clockwise":
        return clockwise(matrix)

print(rotate(matrix,"clockwise"))
print(rotate(matrix,"counter-clockwise"))
