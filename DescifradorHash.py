# Un hash es una funcion capas de codificar un texto , osea brinda la seguridad de
# codificar una texto o variable 

# Uno de los hashes mas usados es el MD5 versatil y seguro / Tiene conflicto de hashes...

# Caracteristicas de la funcion hash :
# Transfoma el archivo en un valor alfanumerico de una longitud determinada
# Cada hash tiene un algoritmo interno matematica 
# sha 1 , sha2 , ... tipos de hash

# Una ves ejecutado un valor hash no se puedes volver atras (Un encriptado SI),

# Donde se usa el hashing 
# Claves/Passport
# Integridad de datos
# Introducirlos en discos/Listas negras(Antipirateria, Derechos de autor)\
# BlockChain

# Ataque de Diccionario

import hashlib
import getpass
import time
import socket
import os

# Códigos de escape ANSI para los colores
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
# Hacer una base pero guardad Hashes 
# DataBase = { {"Name" : 'Juan124' , "Password" : "seguro4321"} }

# print(DataBase)

UserName = str(input("Ingrese su nombre de usuario → "))
os.system("cls")
Clave = getpass.getpass("Crea una clave → ")
os.system("cls")
hash_file = hash(Clave) 

if hash(getpass.getpass(f"Ingrese la clave → ")) == hash_file:
    os.system("cls")
    print("Verificando clave ...") 
    time.sleep(2)
    os.system("cls")
    print(GREEN+"Bienvenido"+RESET)

else:
    os.system("cls")
    print("Verificando clave ...") 
    time.sleep(2)
    os.system("cls")
    print(RED+"Acceso denegado"+RESET)



#ADVERTENCIA NO FUNCIONA DEBIDO A QUE NO SE SABE QUE TIPO DE ALGORITMO DE HASHING ESTAMOS USANDO
# with open(dic_file, "r") as file:

#     Data = [line.strip for line in file]

#     for password in Data:

#         hash_Calculado = hashlib.sha1(password.encode()).hexdigest()

#         if hash_Calculado == hash_file:
#             print(f"La clave original es : {password}")
#             break

#         else:
#             print("La clave no se encuentra en los datos")