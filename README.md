# DNS_HUNTER
Este projeto totalmente feito em Python teve como intuito desenvolver uma ferramenta que enumerasse servidores DNS.

A enumeração dos servidores ocorre da seguinte forma, o programa possui uma wordlist com aproximadamente 57.000 linhas, com nomes de
possíveis servidores DNS, esta wordlist é baseada no repositório https://github.com/danielmiessler/SecLists/. O programa utiliza então
a entrada de dados do usuário e a wordlist para configurar o alvo e seus possíveis servidores DNS, formando assim sua entrada de pesquisa
que irá tentar estabelecer uma conexão. se a resposta for bem sucedida o programa listará a URL e o possivel IP deste servidor!

Para executa-lo: sudo python3 dns_hunter.py

Colaboradores do projeto:

https://github.com/fegma59 
implementou OO no código, Processamento Paralelo e Concorrência, com a finalidade de melhorar o desempenho e rapidez da enumeração, também implementou a escrita     do resultado em disco, em um arquivo, deixando assim mais facil de acessar os resultados. 
