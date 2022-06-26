import unittest

from account import Account
from client import Client

class TestAccount(unittest.TestCase):
    """Clase para probar los métodos de Account
    Los métodos no reciben parámetros
    Los métodos de no retornan valores
    Args:
        unittest (unittest.TestCase): Hereda de unittest
    """
    def test_deposit_float(self) -> None:
        """
            Método para probar el deposito con un valor float
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10.12, "VRT01", cliente_1)
        account.deposit(100.38)
        self.assertEqual(account.balance, 110.50)
    
    def test_deposit_int(self) -> None:
        """
            Método para probar el deposito con un valor int
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        account.deposit(100)
        self.assertEqual(account.balance, 110)
        
    def test_deposit_negativo(self) -> None:
        """
            Método para probar el deposito con un valor negativo
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.deposit(-100)
        self.assertEqual(str(exc.exception), 'Deposito debe ser un número positivo')
        
    def test_deposit_str(self) -> None:
        """
            Método para probar el deposito con un valor string
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.deposit("100")
        self.assertEqual(str(exc.exception), 'Deposito debe ser un número')
        
    def test_deposit_bool(self) -> None:
        """
            Método para probar el deposito con un valor boolean
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.deposit(True)
        self.assertEqual(str(exc.exception), 'Deposito debe ser un número')
        
    def test_withdraw_float(self) -> None:
        """
            Método para probar el retiro con un valor float y menor al saldo
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(100.0, "VRT01", cliente_1)
        account.withdraw(10.0)
        self.assertEqual(account.balance, 90.0)
    
    def test_withdraw_int(self) -> None:
        """
            Método para probar el retiro con un valor int y menor al saldo
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(100, "VRT01", cliente_1)
        account.withdraw(10)
        self.assertEqual(account.balance, 90)
        
    def test_withdraw_negativo(self) -> None:
        """
            Método para probar el retiro con un valor negativo
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.withdraw(-100)
        self.assertEqual(str(exc.exception), 'El retiro debe ser un número positivo')
        
    def test_withdraw_higher(self) -> None:
        """
            Método para probar el retiro con un valor int y mayor al saldo de la cuenta
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.withdraw(100)
        self.assertEqual(str(exc.exception), 'El retiro es mayor al saldo de la cuenta')
        
    def test_withdraw_str(self) -> None:
        """
            Método para probar el retiro con un valor string
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.deposit("100")
        self.assertEqual(str(exc.exception), 'El retiro debe ser un número')
        
    def test_withdraw_bool(self) -> None:
        """
            Método para probar el retiro con un valor boolean
        """
        cliente_1 = Client(10, "fransisco")
        account = Account(10, "VRT01", cliente_1)
        with self.assertRaises(ValueError) as exc:
            account.deposit(True)
        self.assertEqual(str(exc.exception), 'El retiro debe ser un número')
    
    def test_transfer_amount_negative(self) -> None:
        """
            Método para probar la transferencia con un valor negativo
        """
        cliente_1 = Client(10, "fransisco")
        cuenta_1 = Account(100.0, "VRT01", cliente_1)
        cliente_2 = Client(11, "Ana")
        cuenta_2 = Account(50, "VRT02", cliente_2)
        with self.assertRaises(ValueError) as exc:
            cuenta_1.transfer(-10.0, cuenta_2.account_number)
        self.assertEqual(str(exc.exception), 'La transferencia debe ser positiva')
        
    def test_transfer_amount_higher(self) -> None:
        """
            Método para probar la transferencia con un valor mayor al saldo
        """
        cliente_1 = Client(10, "fransisco")
        cuenta_1 = Account(100.0, "VRT01", cliente_1)
        cliente_2 = Client(11, "Ana")
        cuenta_2 = Account(50, "VRT02", cliente_2)
        with self.assertRaises(ValueError) as exc:
            cuenta_1.transfer(1000, cuenta_2.account_number)
        self.assertEqual(str(exc.exception), 'Fondos Insuficientes')
        
    def test_transfer_accepted(self) -> None:
        """
            Método para probar la transferencia con un valor menor al saldo y positivo
        """
        cliente_1 = Client(10, "fransisco")
        cuenta_1 = Account(100.0, "VRT01", cliente_1)
        cliente_2 = Client(11, "Ana")
        cuenta_2 = Account(50, "VRT02", cliente_2)
        cuenta_1.transfer(10.0, cuenta_2.account_number)
        self.assertEqual(cuenta_1.balance, 90.0)
    
if __name__=="__main__":
    unittest.main()
