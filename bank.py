from http import client
from account import Account
from client import Client
"""Es el enter point del programa se instancian las clases para la ejecución
"""
#Creamos dos clientes
cliente_1 = Client(10, "Lina")
cliente_2 = Client(11, "Ana")
print(cliente_1)
print(cliente_2)
#Creamos dos cuentas
cuenta_1 = Account(10, "VRT01", cliente_1)
cuenta_2 = Account(11, "VRT02", cliente_2)
print(cuenta_1)
print(cuenta_2)

#Realizamos depositos
cuenta_1.deposit(100)
print(cuenta_1)
cuenta_2.deposit(1000)
cuenta_2.deposit(-10000)
print(cuenta_2)
#Realizamos transferencias
cuenta_1.transfer(-50, cuenta_2.account_number)
cuenta_1.transfer(1000, cuenta_2.account_number)
cuenta_1.transfer(50, cuenta_2.account_number)
