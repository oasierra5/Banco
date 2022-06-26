from abc import ABC

class Person(ABC):
    """Clase Abstracta Persona 
    Args:
        ABC (Abstract): ABC es la clase padre para herencia abstracta
    """
    
    _id: int
    _name: str
    
    def __init__(self, id: int, name: str) -> None:
        """Inicializador de la clase Persona

        Args:
            id (int): identificador de la persona 
            name (str): nombre de la persona
        """
        self._id = id
        self._name = name
    
    @property
    def id(self) -> int:
        """Método getter de id
        Returns:
            int: identificador de la persona
        """
        return self._id
    
    @property
    def name(self) -> str:
        """Método getter de name
        Returns:
            str: nombre de la persona
        """
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        """Método getter de name
        Args:
            name (str): nombre de la persona
        """
        self._name = name
    
