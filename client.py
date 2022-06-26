from person_Abstract import Person

class Client(Person):
    """Clase Cliente que Hereda de Persona 
    Args:
        Persona (Abstract): Person es la clase padre
    """
    def __init__(self, id: int, name: str) -> None:
        """Inicializador de la clase Persona

        Args:
            id (int): identificador de la persona 
            name (str): nombre de la persona
        """
        super().__init__(id, name)
    
    def __str__(self) -> str:
        """Sobre escribimos el método str aecuandolo para mostrar los datos de Client

        Args:
            id (int): identificador de la persona 
            name (str): nombre de la persona
        """
        return f'ID Cliente: {self._id}, Nombre del Cliente: {self._name}'
    
