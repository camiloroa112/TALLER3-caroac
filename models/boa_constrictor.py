from models.animal_exotico import Animal_Exotico
class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self._ratones_comidos = 0

    def sonido_animal(self) -> str:
        return "¡Tsss!"
    
    def comer(self, raton_comido: int) -> None:
        if self._ratones_comidos >= 20:
            raise ValueError('¡Demasiados Ratones!')
        else:
            self._ratones_comidos += raton_comido
    
    def get_ratones_comidos(self) -> int:
        return self._ratones_comidos