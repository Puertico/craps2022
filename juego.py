
from tirador import Tirador

class Juego:

    def __init__(self):
        self.tirador=Tirador()
        self.estado=False


    def lanzar_punto(self):
        tiro=self.tirador.lanzar()

        if tiro==2 or tiro==3 or tiro==12:
            print("perdio!")
            self.estado=False
        else:
            if tiro==7 or tiro==11:
                print("gano")
                self.estado=False
            else:
                print("El juego sigue con un punto de: ", tiro)
                self.estado=True



