from fluxCenter import fluxCenter
from Vector2D import Vector2D as v2
print(
    fluxCenter([
        v2(0,2),
        v2(5,0),
        v2(-1,-3),
        v2(-1,-2),
        v2(-2,-1),
        v2(-1,1)
    ])
)
