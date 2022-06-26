from datetime import datetime

from account_Abstract import AccountAbstract
from client import Client

class Account(AccountAbstract):
    """Clase Account que hereda de la clase abstracta AccountAbstract

    Args:
        AccountAbstract (Abstract): AccountAbstract es la clase padre
    """
    __account_number: str
    __opening_date: datetime
    __client: Client
    
    def __init__(self, balance: float, account_number: str, client: Client) -> None:
        """Inicializador de la clase Client

        Args:
            balance (float): Lo que el cliente tiene en la cuenta 
            account_number (str): Número de la cuenta del client
            client (Client): Instancia de Client
            opening_date (datetime): Fecha completa de la apertura de la cuenta
        """
        super().__init__(balance)
        self.__account_number = account_number
        self.__client = client
        self.__opening_date = datetime.now()
        
    @property
    def account_number(self) -> float:
        """Método getter de account_number
        Returns:
            float: número de la cuenta
        """
        return self.__account_number
    
    @property
    def balance(self) -> float:
        """Método getter de balance
        Returns:
            float: Valor de lo que el cliente tiene en la cuenta
        """
        return self._balance
    
    @balance.setter
    def balance(self, balance) -> None:
        """Método getter de balance
        Args:
            balance (float): valor de lo que el cliente tiene en la cuenta
        """
        self._balance = balance
        
    def __str__(self):
        """Sobre escribimos el método str aecuandolo para mostrar los datos de la cuenta

        Returns:
            client (Client): Instancia de Client
            balance (float): Valor de lo que tiene el cliente tiene en la cuenta 
            account_number (str): Número de la cuenta del client
            opening_date (datetime): Fecha completa de la apertura de la cuenta
        """
        return f"{self.__client} Cuenta {self.__account_number}, Saldo {self._balance}, Apertura {self.__opening_date}"
        
    def deposit(self, increase: float) -> None:
        """Método para realizar un deposito en la cuenta
        Se valida cuando el increase es positivo

        Args:
            increase (float): Valor del increase
        """
        if increase > 0:
            self._balance += increase
        else:
            print("Error el incremento debe ser positivo")
            
    def withdraw(self, decrease: float) -> None:
        """Método para realizar un retiro en la cuenta
        Se valida cuando el decrease es negativo y 
        cuando decrease es menor al saldo de la cuenta
        para que se pueda realizar el descuento en el balance
        Args:
            increase (float): Valor del retiro
        """
        if decrease < 0:
            print("No puede retirar")
        elif decrease > self.balance:
            print("Fondos Insuficientes")
        else:
            self._balance -= decrease
            print(f"Nuevo saldo es: {self._balance}")
            
    def transfer(self, amount: float, other_account_number: str) -> None:
        """Método para realizar una transferencia en la cuenta
        Se valida cuando el amount es negativo y 
        cuando amount es menor al saldo de la cuenta
        para que se pueda realizar la trasnferencia en el balance
        Args:
            increase (float): Valor de la transferencia
        """
        if amount < 0:
            print("Error el valor de la transferencia debe ser positiva")
        elif amount > self._balance:
            print("No se puede realizar ala transferencia Fondos Insuficientes")
        else:
            self._balance -= amount
            print(f"Transferencia realizada a la cuenta {other_account_number} con valor de {amount}, Su nuevo saldo es: {self._balance}")
            
