Problema: https://codeforces.com/contest/321/problem/E

Solución aceptada en codeforces: https://codeforces.com/contest/321/submission/281919044

# Explicación del código

## Variables Globales
- N y k son constantes que representan los límites superiores de n (número de personas) y k (número de grupos).
- sum[][] es una matriz acumulativa que almacena los valores de "desconocimiento" entre los grupos de personas.
- f[][] es la tabla de programación dinámica que almacena los resultados parciales de las particiones mínimas.

## Funcion calc
- Esta función calcula el costo de agrupar a las personas desde la posición x hasta la posición y. El costo de agrupar a las personas en este intervalo está basado en la matriz acumulativa sum[][].
- El costo de agrupar a las personas entre x y y se calcula utilizando la fórmula de acumulación de sumas, que permite obtener la suma total de "distancia" o "desconocimiento" en tiempo constante. La función aprovecha los valores precomputados en sum[][] para evitar tener que recalcular las sumas de manera repetitiva.

## Funcion solve
- Esta función es la implementación del algoritmo de divide y vencerás para optimizar la búsqueda de la mejor partición en cada paso de la programación dinámica.
- Caso base: Si el límite izquierdo l es mayor que el límite derecho r, la función termina (no hay nada que procesar).
- Dividir el rango: La función divide el rango actual [l, r] en dos mitades usando el punto medio mid.
- Buscar el punto de partición óptimo:
        Se inicializa f[mid][s] con el valor infinito (INF).
- Luego, se itera sobre todos los posibles puntos de partición i entre L y min(mid, R), tratando de encontrar el mejor lugar para dividir el grupo.
- El costo de particionar en el punto i se calcula como f[i-1][s-1] (el costo óptimo de dividir los primeros i-1 elementos en s-1 grupos) más calc(i, mid) (el costo de agrupar a las personas entre i y mid).
- Si este costo es mejor que el valor actual en f[mid][s], se actualiza y se guarda el punto de partición óptimo p = i.
- Después de encontrar el punto de partición óptimo para mid, la función se llama recursivamente para las dos mitades del rango [l, mid-1] y [mid+1, r], ajustando los límites de búsqueda para las particiones (L y R) según el valor de p para mantener la propiedad de monotonicidad (la partición óptima solo puede moverse hacia adelante).

## Función main

Esta es la función principal que ejecuta el programa y calcula la partición óptima del conjunto de personas.

- Se leen los valores de n (número de personas) y k (número de grupos) desde la entrada.
- Se construye la matriz acumulativa sum[][]
- Para todas las personas (i de 1 a n), se inicializa f[i][0] con INF ya que no es posible dividir a i personas en 0 grupos.
- Se llama a solve() k veces (una por cada número de grupos)
- Al final, el valor óptimo de dividir n personas en k grupos se encuentra en f[n][k]. Dado que el cálculo del costo en este problema genera el doble del valor esperado, se divide el resultado entre 2 antes de imprimirlo.