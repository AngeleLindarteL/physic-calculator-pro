from math import pi as PI
from models.Relleno import Relleno

class Tanque:
    rellenoV = 10
    def __init__(self, diametro, alto, medida):
        self._diametro = diametro
        self._alto = alto
        self._radio = diametro / 2
        self._medida = medida

    def __str__(self):
        return f'''
        Tanque propiedades :
            Diametro: {self._diametro}{self._medida}
            Alto: {self._alto}{self._medida}
            Radio: {self._radio}{self._medida}
    '''

    @property
    def radio(self):
        return self._radio

    @property
    def diametro(self):
        return self._diametro

    @diametro.setter
    def diametro(self, diametro):
        self._diametro = diametro

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def medida(self):
        return self._medida

    @medida.setter
    def medida(self, medida):
        self._medida = medida

    def calcular_volumen_tanque(self):
        self.volumen = float("{:.2f}".format((PI*self.alto*(self._radio**2))))
        return f'Volumen: {float("{:.2f}".format((PI*self.alto*(self._radio**2))))} {self.medida}3'

    def calcular_area_tanque(self):
        areab = PI * (self._radio**2)
        areal = 2*PI*self._radio*self.alto
        return f'Area: {float("{:.2f}".format(2*areab+areal))} {self.medida}2'

    def rellenar(self, Relleno):
        rellenoV = 0
        if Relleno.medida == 'l':
            m3 = Relleno.cantidad / 1000
            if self._medida == 'km':
                rellenoV = m3/1e+9
            elif self._medida == 'm':
                rellenoV = m3
            elif self._medida == 'cm':
                rellenoV = m3 * 1e+6
        elif Relleno.medida == 'ml':
            m3 = Relleno.cantidad / 1e+6
            if self._medida == 'km':
                rellenoV = m3/1e+9
            elif self._medida == 'm':
                rellenoV = m3
            elif self._medida == 'cm':
                rellenoV = m3 * 1e+6
        else:
            rellenoV = 20202020
        return [
            f"La cantidad del relleno en medidas de volumen es: {rellenoV}{self._medida}3",
            rellenoV < PI*self.alto*(self._radio**2)
        ]

if __name__ == '__main__':
    tanque1 = Tanque(25, 100, 'cm')
    print(tanque1.calcular_area_tanque())
    print(tanque1.calcular_volumen_tanque())
    relleno1 = Relleno('agua', 20000, 'l')

    print(tanque1.rellenar(relleno1))