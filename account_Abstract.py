from abc import ABC

class AccountAbstract(ABC):
    """Clase Abstracta AccountAbstract 
    Args:
        ABC (Abstract): ABC es la clase padre para herencia abstracta
    """
    
    _balance: float
    
    def __init__(self, balance: float) -> None:
        """Inicializador de la clase Persona
        Args:
            balance (float): Lo que el cliente tiene en la cuenta
        """ 
        self._balance = balance
