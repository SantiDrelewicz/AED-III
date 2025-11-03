# B. Viaje Intergaláctico

**Tiempo límite por test:** 2 s.  
**Memoria límite por test:** 260 MB

El malvado comandante Zargon capturó al equipo del capitán Martínez. El capitán Martínez logró escapar, pero para ese momento la nave de Zargon ya había saltado al hiperespacio. Sin embargo, Martínez sabe en qué planeta aterrizará Zargon. Para salvar a sus amigos, Martínez debe viajar repetidamente a través de portales para llegar a ese planeta. En total, la galaxia tiene $n$ planetas, indexados con números del $1$ al $n$. Martínez está en el planeta con índice $1$, y Zargon aterrizará en el planeta con índice $n$. Martínez puede moverse entre algunos pares de planetas a través de portales (puede moverse en ambas direcciones); la transferencia toma una cantidad positiva de segundos. Martínez comienza su viaje en el tiempo $0$.

Puede suceder que otros viajeros estén llegando al planeta donde Martínez se encuentra. En este caso, Martínez tiene que esperar exactamente 1 segundo antes de poder usar el portal. Es decir, si en el tiempo $t$ otro viajero llega al planeta, Martínez solo puede atravesar el portal en el tiempo $t + 1$, a menos que haya más viajeros llegando en el tiempo $t + 1$ al mismo planeta. Conociendo la información sobre los tiempos de viaje entre los planetas, y los tiempos en los que Martínez no podría usar el portal en planetas particulares, determine el tiempo mínimo en el cual puede llegar al planeta con índice $n$.

## Entrada

La primera línea contiene dos enteros separados por espacio: $n$ $(3 \leq n \leq 10^4)$, el número de planetas en la galaxia; y $m$ $(0 \leq m \leq 10^4)$, el número de pares de planetas entre los cuales Martínez puede viajar usando portales.

Luego siguen $m$ líneas, cada una conteniendo tres enteros: la $i$-ésima línea contiene los números de los planetas $a_i$ y $b_i$ $(1 \leq a_i, b_i \leq n, a_i \neq b_i)$ que están conectados a través de portales, y el entero $w_i$ $(1 \leq w_i \leq 10^4)$ que representa el tiempo de transferencia (en segundos) entre estos planetas. Se garantiza que entre cualquier par de planetas hay como máximo una conexión de portal.

Luego siguen $n$ líneas: la $i$-ésima línea contiene un entero $k_i$ $(0 \leq k_i \leq 10^5)$ que denota el número de momentos de tiempo cuando otros viajeros llegan al planeta con índice $i$. Luego siguen $k_i$ enteros distintos separados por espacio $t_{ij}$ $(0 \leq t_{ij} < 10^6)$, ordenados en orden ascendente. Un entero $t_{ij}$ significa que en el tiempo $t_{ij}$ (en segundos) otro viajero llega al planeta $i$. Se garantiza que la suma de todos los $k_i$ no excede $10^6$.

## Salida

Imprima un solo número: la menor cantidad de tiempo que Martínez necesita para ir del planeta $1$ al planeta $n$. Si Martínez no puede llegar al planeta $n$ en ninguna cantidad de tiempo, imprima el número $-1$.

## Ejemplos

| entrada |
|---------|
| `4 6`<br>`1 2 2`<br>`1 3 3`<br>`1 4 9`<br>`2 3 5`<br>`2 4 6`<br>`3 4 3`<br>`0`<br>`1 3`<br>`2 3 4` <br>`0` | 
| **salida** |
| `8` |

| entrada |
|---------|
| `3 1`<br>`1 2 3`<br>`0`<br>`1 3`<br>`0`| 
| **salida** |
| `-1` |
