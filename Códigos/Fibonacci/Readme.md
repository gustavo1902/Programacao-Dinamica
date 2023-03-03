## Conceito
A sequência de Fibonacci é uma sequência numérica em que cada número é a soma dos dois números anteriores. A sequência começa com 0 e 1, e os próximos números são calculados somando os dois números anteriores. Assim, a sequência começa assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

O algoritmo de Fibonacci é um dos problemas mais comuns resolvidos com programação dinâmica. A técnica de memorização é usada para evitar o cálculo repetido de soluções de subproblemas, tornando a função mais eficiente.

## Funcionamento

O código implementado é um algoritmo para calcular o n-ésimo número na sequência de Fibonacci usando programação dinâmica com a técnica de memorização.

O código implementado define uma função **fib(n, memo={})** que recebe um número inteiro n e um dicionário memo como argumentos. O dicionário memo armazena as soluções de subproblemas para evitar o cálculo repetido de soluções de subproblemas. Se o valor de n já estiver no dicionário memo, a função retorna o valor armazenado no dicionário.

Se o valor de n for menor ou igual a 2, a função retorna 1. Caso contrário, a função calcula o valor de **fib(n-1) e fib(n-2)** usando recursão e armazena a soma desses valores em memo[n]. Por fim, a função retorna memo[n].

Para calcular o n-ésimo número da sequência de Fibonacci, basta chamar a função **fib(n)** com o valor de n desejado. Como a função usa a técnica de memorização, a chamada subsequente da função **fib(n) com** o mesmo valor de n será mais rápida, pois a solução já estará armazenada em memo.

## Como executar o código

O código pode ser executado em qualquer ambiente Python, como um ambiente virtual ou no próprio computador. O código não tem dependências externas e pode ser executado diretamente no prompt de comando ou terminal.

Para executar o código, basta criar um arquivo Python e copiar a implementação da função **fib** apresentada anteriormente. Em seguida, é possível chamar a função **fib** com o valor desejado de n.

print(fib(10))


