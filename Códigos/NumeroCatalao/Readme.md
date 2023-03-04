## Conceito
Os números catalães são definidos como uma sequência matemática que consiste em números inteiros positivos, que podem ser usados ​​para encontrar o número de possibilidades de várias combinações. 


## Funcionamento

a função catalan recebe um inteiro n e utiliza programação dinâmica para calcular o número de Catalão C(n). A tabela table é inicializada com 0's e o caso base é C(0) = 1. Em seguida, a tabela é preenchida utilizando a fórmula de Bellman:

*C(n) = C(0)*C(n-1) + C(1)*C(n-2) + ... + C(n-1)*C(0)*

Ou seja, o valor de C(n) é a soma dos produtos de C(i) e C(n-i-1), para todo i entre 0 e n-1. Essa fórmula leva em conta todas as possíveis combinações de parênteses balanceados com n pares de parênteses.

Por fim, o valor de C(n) é retornado. O programa pede ao usuário o valor de n e imprime o resultado. Note que este algoritmo utiliza a técnica de memoization, que é uma das abordagens comuns de programação dinâmica, para evitar recalcula de valores já calculados e reduzir a complexidade temporal do algoritmo.
