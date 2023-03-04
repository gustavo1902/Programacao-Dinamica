## Conceito

O problema consiste em encontrar um subconjunto de vértices de um grafo que cubra todas as suas arestas. Uma solução para esse problema pode ser encontrada utilizando programação dinâmica.

A ideia é utilizar uma tabela dp para armazenar o tamanho mínimo do vertex cover (VC) de um grafo, considerando somente os vértices até o índice i. O valor dp[i][0] representa o tamanho mínimo do VC do grafo formado pelos primeiros i vértices, onde o vértice i não é incluído no VC. O valor dp[i][1] representa o tamanho mínimo do VC do grafo formado pelos primeiros i vértices, onde o vértice i é incluído no VC.

## Funcionamento

Neste exemplo, a classe Graph representa um grafo não direcionado com n vértices, e a função vertex_cover recebe um objeto 



