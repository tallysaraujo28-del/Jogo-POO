# Arquivo: 666

## 1. Visão Geral

**Arquivo: 666** é um jogo de investigação e ação em mundo aberto, ambientado na cidade de **Cine City**. O protagonista, **John Souza**, é um investigador criminal que acaba descobrindo que a cidade abriga vários assassinos em série inspirados em figuras famosas da indústria cinematográfica.

- **Gênero:** Investigação / Ação / Mundo aberto
- **Plataforma:** PC (Windows)
- **Tecnologia:** Python + Pygame

---

## 2. Objetivo do Jogo

O jogador precisa desvendar uma série de casos, cada um representado por uma **fase** com um assassino diferente.

- Cada caso deve ser investigado: coletar pistas, interrogar NPCs e explorar a cidade.
- A fase só termina quando o jogador **mata ou prende** o serial killer daquele caso.
- O jogo é vencido ao **resolver todos os casos**.

---

## 3. Personagem Principal

**John Souza** é um investigador criminal da Polícia Federal com 4 anos de serviço. Apesar da experiência, é um pouco incompetente, o que dá um tom de humor e humanidade ao personagem.

**Movimentação:** anda devagar, mas pode correr.

**Status:**

| Status | Descrição |
|---|---|
| Pontos de Vida (PV) | Saúde do personagem |
| Pontos de Esforço (PE) | Usados em ações especiais, como correr e habilidades |
| Pontos de Experiência (EXP) | Progressão do personagem |

**Atributos principais:**

| Atributo | Função |
|---|---|
| Força | Dano em combate corpo a corpo |
| Agilidade | Velocidade e esquiva |
| Inteligência | Investigação, puzzles e análise de pistas |
| Vigor | Vida e resistência |
| Carisma | Interações com NPCs, interrogatórios e preços |

---

## 4. Inimigos e Obstáculos

Os antagonistas são os **assassinos principais** e seus **capangas**. O comportamento varia de vilão para vilão:

- **Diretos:** partem para o confronto aberto.
- **Táticos e furtivos:** usam armadilhas, emboscadas e manipulação, tanto em combate quanto fora dele.

Ao colidir com um inimigo, o jogador pode **perder pontos de vida** ou, em situações críticas, **perder o jogo**.

---

## 5. Cenário

O jogo se passa nas diferentes áreas de **Cine City**, uma metrópole comum com alguns **easter eggs** referenciando o cinema.

- O **objetivo final** de cada caso é a área do chefão (o assassino do caso).
- Os **itens** podem ser obtidos de três formas:
  - entregues por NPCs;
  - encontrados em cenas de crime;
  - dropados por vilões ou achados pela cidade.

---

## 6. Progressão e Recompensas

| Recurso | Formato | Como obter |
|---|---|---|
| Experiência | EXP: 0 | Derrotar inimigos e completar missões |
| Dinheiro | R$ 0,00 | Completar missões, derrotar inimigos e eventos paralelos |
| Progresso do caso | 0% | Exibido nos detalhes do caso, indica quanto a fase está completa |

---

## 7. Sistema de Vida

- **Vida inicial:** `10 + Vigor inicial`.
- A vida máxima aumenta conforme o atributo **Vigor** evolui.
- O jogador perde vida ao ser atacado por inimigos, envenenado, ao sofrer sangramento, entre outros efeitos.

---

## 8. Controles

| Tecla | Ação |
|---|---|
| ↑ (UP) | Mover para cima |
| ↓ (DOWN) | Mover para baixo |
| ← (LEFT) | Mover para a esquerda |
| → (RIGHT) | Mover para a direita |
| TAB | Abrir caderno de anotações |
| ESC | Abrir menu de pausa |
| SPACE | Ação / interagir |
| Q | Usar item |
| W | Atacar |

---

## 9. Fluxo do Jogo

1. O jogo começa com o protagonista em sua **sala**, onde escolhe o primeiro caso.
2. Na **jogabilidade normal**, o jogador enfrenta inimigos, explora o mapa e interage com NPCs.
3. **Minigames de investigação** e **puzzles** quebram o ritmo e diversificam a experiência.
4. O caso termina quando o assassino é morto ou preso.
5. **Derrota:** os pontos de vida chegam a zero.
6. **Vitória:** todos os casos são resolvidos.

---

## 10. Regras

- Nem todos os itens terão acesso livre.
- O jogador não pode ultrapassar os limites da cidade.
- Nem todos os elementos do cenário são interativos.
- Não é possível fazer dois casos ao mesmo tempo.
- Sprites que não fazem parte do chão não podem ser atravessadas.
- O personagem não se movimenta enquanto o jogo estiver pausado.
- Só é possível comprar itens se o jogador tiver dinheiro suficiente.

---

## 11. Estrutura do Projeto

Código e sprites ficam em arquivos separados, com organização por responsabilidade:

```
arquivo-666/
├── codigo/
│   ├── mapa.py
│   ├── npcs.py
│   ├── protagonista.py
│   ├── viloes.py
│   └── main.py
└── sprites/
    ├── mapa/
    ├── npcs/
    ├── protagonista/
    └── viloes/
```

---

## 12. Requisitos Mínimos

- Computador ou laptop com **Windows**.
- **Python** e **Pygame** instalados.

---

## 13. Melhorias Futuras

- Melhorar os gráficos.
- Expandir o mapa da cidade.
- Adicionar mais casos e assassinos.
- Publicar o jogo.
