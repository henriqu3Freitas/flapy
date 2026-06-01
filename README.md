# Flapy

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Gustavo Albuquerque
- Henrique de Freitas
- Juan Pedro
- Leonardo Gonzaga

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Descreva brevemente a ideia principal do jogo.

Flapy é um jogo de habilidade em que o jogador controla um pássaro que deve atravessar espaços entre obstáculos sem colidir com eles. A cada obstáculo ultrapassado, o jogador ganha pontos.

O objetivo é sobreviver o máximo possível e alcançar a maior pontuação antes de colidir com um obstáculo ou com o chão.

## Objetivo do jogador

Explique o que o jogador precisa fazer para vencer ou avançar no jogo.

Controlar o pássaro para atravessar o maior número possível de obstáculos, acumulando pontos e tentando superar o recorde armazenado pelo jogo.

## Regras do jogo

Liste as principais regras do jogo.

Exemplo:

- O pássaro se movimenta continuamente para frente.
- A gravidade faz o pássaro cair constantemente.
- Ao pressionar a tecla de ação, o pássaro realiza um salto.
- Cada obstáculo ultrapassado aumenta a pontuação do jogador.
- Colidir com um obstáculo encerra a partida.
- Colidir com o chão encerra a partida.
- O jogo registra o maior recorde obtido.

## Controles

Informe as teclas ou comandos utilizados no jogo.

Espaço: fazer o pássaro subir.
ENTER: iniciar ou reiniciar a partida.
ESC: sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
