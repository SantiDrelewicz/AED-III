# A. Máquina misteriosa

**Tiempo limite por test:** 2 s  
**Memoria limite por test:** 256 MB

Carlos ha encontrado un dispositivo extraño. En el panel frontal del dispositivo hay: un botón rojo, un botón azul y una pantalla que muestra un número entero positivo. Después de presionar el botón rojo, el dispositivo multiplica el número mostrado por dos. Después de presionar el botón azul, el dispositivo resta uno al número en la pantalla. Si en algún momento el número deja de ser positivo, el dispositivo se descompone. La pantalla puede mostrar números arbitrariamente grandes. Inicialmente, la pantalla muestra el número $n$.

Ana quiere obtener el número $m$ en la pantalla. ¿Cuál es el número mínimo de clics que tiene que hacer para lograr este resultado?

## Entrada

La primera y única línea de la entrada contiene dos enteros distintos $n$ y $m$ ($1 \le n, m \le 10^4$), separados por un espacio.

## Salida

Imprima un solo número: el número mínimo de veces que se necesita presionar el botón requerido para obtener el número $m$ a partir del número $n$.

## Ejemplos

| entrada | salida |
|---------|--------|
| `8 12`  | `3`    |
| `20 15` | `5`    |
