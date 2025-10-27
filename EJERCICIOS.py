"""PY0016"""

# print("Numeros del 1 al 20")
# for numero in range(0, 21):
#     print(numero)
# print("Numeros pares del 0 al 20")
# for numero in range(0,21):
#     if numero % 2 == 0:
#         print(numero)
# print("Numeros impares del 0 al -20")
# for numeros in range(0,-21,-1):
#     if numeros%2!=0:
#         print(numeros)


"""Py0017"""

# pares_hasta_100= range(1,101,2)
# sum_total = sum(pares_hasta_100)
# print(f"la suma de todos los numeros es:{sum_total}")


"""Py0019"""

# while True:
#     try:
#         entrada = input("Introduce un número entero impar: ")
#         n = int(entrada.strip())
#     except ValueError:
#         print("Entrada inválida. Debes introducir un número entero impar. Inténtalo de nuevo.")
#         continue
#     except EOFError:
#         print("\nEntrada finalizada. Saliendo.")
#
#
#     if n % 2 != 0:
#         print(f"El número {n} es impar. Fin del programa.")
#         break
#     else:
#         print(f"El número {n} es par. Debes introducir un número impar.")

"""Py0014"""


"""PY0018"""
# registro = ("zèrep nuaJ,01")
# registro2 = registro[::-1]
# nota, nombre = registro2.split(",")
# print(f"{nombre} ha sacado un : {nota}")

"""PY0043"""
# cadena=input("Dime la cadena")
# cadena=cadena.replace(" ","").lower()
# letras_contadas=[]
# print("\nOcurrencias de cada carácter\n")
#
# for c in cadena:
#     if c not in letras_contadas:
#         contador=0
#         for x in cadena:
#             if x==c:
#                 contador+=1
#         print(f"{c}: {contador}")
#         letras_contadas.append(c)
"""Py0013"""
