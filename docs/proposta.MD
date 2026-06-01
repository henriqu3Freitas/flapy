# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Flapy

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Gustavo Albuquerque
- Nome 2: Henrique de Freitas
- Nome 3: Juan Pedro
- Nome 4: Leonardo Gonzaga

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo: jogo de desviar de obstáculos

> Escreva aqui.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogo é inspirado na mecânica de Flappy Bird. O jogador controla um personagem que deve atravessar obstáculos sem colidir com eles. A dificuldade aumenta gradualmente conforme a pontuação cresce, exigindo maior atenção e reflexos.

O objetivo do projeto é desenvolver um jogo simples, divertido e organizado, aplicando os conceitos estudados na disciplina.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Controlar o personagem para atravessar o maior número possível de obstáculos, acumulando pontos e tentando superar o recorde armazenado pelo jogo.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O personagem se movimenta continuamente para frente.
- Regra 2: O jogador pode realizar saltos para evitar obstáculos.
- Regra 3: Cada obstáculo ultrapassado gera pontos.
- Regra 4: A velocidade e a dificuldade podem aumentar ao longo da partida.
- Regra 5: O jogo termina quando ocorre colisão com um obstáculo ou com os limites do cenário.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O jogador vence ao atingir uma pontuação pré-definida (por exemplo, 50 pontos) ou ao completar o objetivo estabelecido para a partida.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> - Colisão com obstáculos.
- Colisão com o chão ou limite inferior da tela.
- Fechamento manual da janela pelo usuário.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

Pássaro (jogador)
descrição: personagem controlado pelo jogador, responsável por atravessar os obstáculos e acumular pontos.
Canos (obstáculos): 
descrição: barreiras distribuídas pelo cenário que o jogador deve evitar para continuar na partida.
Sistema de pontuação: 
descrição: contabiliza a quantidade de obstáculos ultrapassados durante a partida.
Recorde: 
descrição: armazena a maior pontuação obtida pelo jogador, permitindo comparação entre partidas.
Tela inicial: 
descrição: menu principal que permite iniciar o jogo e visualizar informações básicas.
Tela de Game Over: 
descrição: exibida ao final da partida, mostrando a pontuação obtida e opções para reiniciar ou sair.
Cenário de fundo: 
descrição: elemento visual utilizado para representar o ambiente do jogo e melhorar a experiência do usuário.
Efeitos sonoros: 
descrição: sons reproduzidos durante ações importantes, como saltos, pontuação e colisões.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Espaço: realizar salto
- Tecla/comando: ESC: retornar ao menu ou encerrar o jogo.
- Tecla/comando: Mouse: interação com botões do menu

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> - main.py: responsável por iniciar a aplicação.
- src/game.py: contém o loop principal do jogo e o controle dos estados da partida.
- src/player.py: responsável pela movimentação e comportamento do pássaro.
- src/pipes.py: responsável pela geração e movimentação dos obstáculos.
- src/score.py: controla a pontuação e o sistema de recordes.
- src/menu.py: contém as telas de menu inicial e fim de jogo.
- data/highscore.txt: armazena o recorde do jogador.
- assets/: contém imagens, sons e outros recursos utilizados pelo jogo.
- tests/: contém os testes das principais funções do projeto.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Imagens gratuitas para representar o pássaro, obstáculos e cenário.
Efeitos sonoros gratuitos para ações como salto, pontuação e colisão.
Fontes gratuitas para exibição de textos e pontuação.
Tutoriais e documentações sobre Python e Pygame utilizados apenas como referência de estudo.
Ícones e elementos gráficos livres de uso, caso necessário.


## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: implementar a movimentação do pássaro utilizando gravidade e saltos de forma adequada.
- Dificuldade 2: criar um sistema eficiente de colisão entre o jogador e os obstáculos.
- Dificuldade 3: organizar o código em módulos e funções, mantendo boa estrutura e legibilidade.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá um pássaro controlado pelo jogador, obstáculos aparecendo continuamente na tela, sistema de pontuação, detecção de colisões, tela de fim de jogo, armazenamento do recorde em arquivo e código organizado em módulos e funções, permitindo a execução completa da partida sem erros

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: adicionar efeitos sonoros e música de fundo.
- Melhoria 2: implementar aumento gradual da dificuldade conforme a pontuação.
- Melhoria 3: adicionar animações e melhorias visuais ao personagem e aos obstáculos.
- Melhoria 4: criar um menu inicial mais elaborado.
- Melhoria 5: implementar um sistema de ranking com múltiplas pontuações.
