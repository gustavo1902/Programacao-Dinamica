## Conceito

O algoritmo de Floyd-Warshall usa uma matriz de distâncias para armazenar as distâncias entre os vértices. Inicialmente, essa matriz é preenchida com as distâncias diretas entre os vértices (ou infinito, se não houver uma aresta entre os vértices). Em seguida, o algoritmo compara as distâncias diretas com as distâncias que passam por outros vértices, atualizando a matriz de distâncias conforme necessário. O processo é repetido para cada vértice como vértice intermediário.

## Funcionamento

Nesta implementação, a matriz graph é uma matriz de adjacência que representa o grafo com pesos. Cada elemento graph[i][j] representa o peso da aresta entre os vértices i e j. Se não houver uma aresta entre os vértices i e j, o valor de graph[i][j] deve ser 0.

A matriz dist é inicializada com as distâncias diretas entre os vértices (ou infinito, se não houver uma aresta entre os vértices). Em seguida, o algoritmo compara as distâncias diretas com as distâncias que passam por outros vértices, atualizando a matriz dist conforme necessário.

Ao final, a função retorna a matriz dist com as distâncias mínimas entre cada par de vértices. Note que se a distância entre dois vértices for infinita, isso significa que não há um caminho entre esses vértices.