from typing import NamedTuple

class Conexion(NamedTuple):
    extremo: int
    peso: int

c = Conexion(1, 10)
v, p = c
print(v, p)