Problema: https://codeforces.com/contest/440/problem/D

Solución aceptada en codeforces: https://codeforces.com/contest/440/submission/282413740


#Expicación del código
Este código aborda el problema de dividir Berland en estados con conexiones interestatales mínimas, al tiempo que garantiza que al menos un estado tenga exactamente `k` ciudades. A continuación, se muestra un desglose de cómo funciona:

## Constantes y bibliotecas

- `N`: Número máximo de ciudades (1077).
- `inf`: Representa el infinito para los cálculos (valor suficientemente grande).
- `MOD`: Módulo para los cálculos (evita el desbordamiento).
- `eps`: Valor de épsilon para comparaciones de punto flotante.

## Funciones de utilidad
-`binpow(a, b)`: Calcula la exponenciación modular de manera eficiente.

## Variables globales
- `n`: Número de ciudades en Berland.
- `k`: Número objetivo de ciudades en al menos un estado.
- `ans`: Almacena el número mínimo de conexiones interestatales encontradas hasta el momento.
- `g[N]`: Lista de adyacencia que representa la red de carreteras (ciudades conectadas por carreteras).
- `dpr[N][N]`: Almacena información adicional para soluciones óptimas (explicado más adelante).
- `answ`: Almacena la lista de carreteras que forman las conexiones interestatales mínimas.
- `dp[N][N]`: Almacena el número mínimo de conexiones interestatales necesarias para un arbol con raiz en i y una ciudad de tamaño j.
- `rebro[N][N]`: Almacena el índice de la carretera que conecta cada par de ciudades para referencia posterior.

## Función `dfs`
- Toma un vértice (`v`) y su padre (`p`, opcional) como argumentos.
- Inicializa `dp[v][1]` (conexiones mínimas para un estado con 1 ciudad) a 0.
- Itera a través de todos los vecinos (`to`) de `v` excepto el padre.
- Llama recursivamente a `dfs` con `to` como vértice y `v` como padre.
- Itera a través de todos los tamaños de estado posibles (`i = n` hasta 1).
- Comprueba si el mínimo actual para un estado con `i + j` ciudades (`dp[v][i + j]`) es mayor que la suma de las conexiones mínimas para los estados con `j` ciudades (`dp[to][j]`) y `i` ciudades (`dp[v][i]`).
-  Si es así, actualiza `dp[v][i + j]` con la suma y almacena la combinación correspondiente de los estados encontrados previamente en `dpr[v][i + j]`.
- Esta matriz `dpr` ayuda a rastrear la solución óptima al mantener información sobre las carreteras utilizadas para lograr ese recuento mínimo de conexiones.
- Incrementa `dp[v][i]` (número de conexiones necesarias para un estado con `i` ciudades considerando `v`).
- Agrega el índice de la carretera que conecta `v` y su vecina (`to`) a `dpr[v][i]`.
- Comprueba si las conexiones mínimas para un estado con `k` ciudades a partir de `v` (`dp[v][k]`) más una conexión al padre (`(p != 0)`) es menor que la mejor solución actual (`ans`).
- Si es así, actualiza `ans` con el nuevo mínimo y `answ` con la lista correspondiente de carreteras que forman las conexiones interestatales mínimas utilizando la información almacenada en `dpr[v][k]`.
- Si el padre existe (`p != 0`), agrega la carretera que conecta `v` y su padre a `answ`.

## Función `solve`
- Lee la cantidad de ciudades (`n`) y el tamaño del estado de destino (`k`) de la entrada.
- Lee las conexiones entre ciudades y las almacena en la lista de adyacencia `g` y en la matriz `rebro` para indexar las carreteras.
- Inicializa `dp` con infinito para todas las combinaciones.
- Establece `ans` en infinito para la comparación inicial.
- Llama a `dfs(1)` para iniciar la búsqueda en profundidad desde la primera ciudad (`1`).
- Imprime el tamaño de la lista `answ` (número de conexiones entre estados).
-  Imprime cada índice de carretera en la lista `answ`, que representa las conexiones mínimas entre estados.
