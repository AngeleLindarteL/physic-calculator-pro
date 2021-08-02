
class Relleno:
    def __init__(self, nombre, cantidad, medida, quest):
        self._nombre = nombre
        self._cantidad = cantidad
        self._medida = medida
        self._quest = quest

    def __str__(self):
        return f'''
        Relleno propiedades :
            Nombre: {self._nombre}
            Cantidad: {self._cantidad}{self._medida}
    '''
    @property
    def quest(self):
        return self._quest

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def medida(self):
        return self._medida

    @medida.setter
    def medida(self, medida):
        self._medida = medida