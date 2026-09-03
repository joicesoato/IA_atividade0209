# Agentes Inteligentes — Unidade 1

Projeto desenvolvido para a **Unidade 1 da disciplina de Inteligência Artificial**, com foco no estudo e na implementação de diferentes tipos de agentes inteligentes.

O projeto reúne os conceitos trabalhados nas **Aulas 5, 6 e 7**, demonstrando agentes baseados em reação, objetivo e utilidade. Também foram incorporados desafios propostos nas aulas, incluindo **margem de segurança no controle de semáforos, obstáculos na navegação e critérios adicionais de utilidade**.

---

## Sobre o projeto

Um agente inteligente pode perceber um ambiente, tomar decisões e executar ações de acordo com seus objetivos.

Neste projeto foram implementados quatro cenários:

| Cenário | Tipo de agente | Critério principal |
|---|---|---|
| Trânsito | Reativo | Quantidade de carros |
| Navegação | Baseado em objetivo | Aproximação do destino |
| Escolha de rota | Baseado em utilidade | Tempo, pedágio e segurança |
| Estacionamento | Baseado em utilidade | Distância, preço e cobertura |

A proposta é observar como diferentes formas de tomada de decisão podem produzir escolhas diferentes dependendo das características do ambiente e dos pesos atribuídos a cada critério.

---

## Objetivos

- Compreender o funcionamento de agentes inteligentes.
- Implementar diferentes tipos de agentes em Python.
- Trabalhar com percepção, decisão e ação.
- Utilizar funções de utilidade para comparar alternativas.
- Analisar como diferentes pesos alteram uma decisão.
- Integrar diferentes agentes em uma função `meta_agente()`.
- Aplicar os conceitos estudados em um novo cenário de estacionamento.
- Organizar o projeto em módulos independentes e reutilizáveis.

---

## Estrutura do projeto

```text
agentes-unidade1/
│
├── principal_unidade1.py
├── semaforo.py
├── navegacao.py
├── utilidade.py
├── vaga.py
└── README.md
```

### `semaforo.py`

Implementa o ambiente de trânsito e o agente responsável por escolher qual rua deve receber o sinal verde.

Também contém o desafio da **margem de segurança**, no qual o agente evita realizar trocas muito frequentes de sinal.

Principais elementos:

- `AmbienteSemaforo`
- `agente_semaforo()`
- `AgenteSemaforoComMargem`

---

### `navegacao.py`

Implementa um ambiente de mapa no qual o agente precisa chegar até uma posição objetivo.

O agente observa sua posição atual e a posição do objetivo para decidir qual movimento realizar.

Também foi incorporado o tratamento de **obstáculos**, fazendo com que o agente verifique se uma posição está livre antes de realizar determinado movimento.

Principais elementos:

- `AmbienteMapa`
- `agente_baseado_objetivo()`
- `posicao_livre()`
- `agente_com_obstaculos()`
- `mover()`

---

### `utilidade.py`

Implementa agentes baseados em utilidade para escolher entre diferentes rotas.

A primeira versão considera:

- tempo de viagem;
- valor do pedágio.

A segunda versão adiciona um terceiro critério:

- nível de segurança.

A função de utilidade permite alterar o peso de cada característica e observar como isso modifica a decisão do agente.

Principais elementos:

- `utilidade()`
- `agente_baseado_utilidade()`
- `utilidade_v2()`
- `agente_utilidade_v2()`

---

### `vaga.py`

Implementa o cenário adicional de **estacionamento**, solicitado no Exercício 4.

O agente compara três vagas considerando:

- distância até a entrada;
- preço;
- benefício de ser uma vaga coberta.

A função de utilidade é:

```text
utilidade = benefício da cobertura - custo da distância e do preço
```

Principais elementos:

- `vagas`
- `utilidade_vaga()`
- `agente_baseado_utilidade_vaga()`

---

### `principal_unidade1.py`

É o arquivo principal do projeto.

Ele reúne os diferentes agentes por meio da função:

```python
meta_agente(cenario, percepcao)
```

A função identifica o cenário recebido e encaminha a percepção para o agente correspondente.

São demonstrados os quatro cenários:

```text
transito
navegacao
escolha_rota
estacionamento
```

Além disso, o arquivo apresenta testes com diferentes configurações de pesos para o cenário de estacionamento.

---

# Tipos de agentes utilizados

## 1. Agente reativo — Trânsito

O agente reativo toma sua decisão diretamente a partir da percepção atual do ambiente.

No cenário de trânsito, ele compara a quantidade de carros nas duas ruas e escolhe o sinal verde para a rua que apresenta maior quantidade de veículos.

### Por que é reativo?

Porque a decisão depende diretamente do estado percebido naquele momento, sem realizar um planejamento mais elaborado do futuro.

---

## 2. Agente baseado em objetivo — Navegação

O agente de navegação possui um objetivo: alcançar determinada posição no mapa.

A partir da posição atual e da posição de destino, ele escolhe movimentos como:

```text
Direita
Esquerda
Baixo
Cima
Parar
```

### Por que é baseado em objetivo?

Porque suas ações são escolhidas com a finalidade de alcançar um estado desejado: a posição objetivo.

---

## 3. Agente baseado em utilidade — Escolha de rota

O agente compara diferentes rotas utilizando uma função de utilidade.

Os critérios considerados são:

- tempo;
- pedágio;
- segurança.

A escolha pode mudar quando os pesos dos critérios são alterados.

Por exemplo, uma rota mais rápida pode ser escolhida quando o tempo possui maior peso. Já uma rota mais segura pode vencer quando o benefício da segurança recebe maior importância.

### Integração do desafio da Aula 7

Foi incorporado o critério de **segurança** ao agente de escolha de rota.

Isso demonstra que uma função de utilidade pode considerar mais de um fator para realizar uma decisão.

---

# 4. Agente baseado em utilidade — Estacionamento

Para o Exercício 4, foi criado um novo cenário de estacionamento.

Existem três vagas:

1. Vaga coberta, longe da entrada.
2. Vaga descoberta, perto da entrada.
3. Vaga coberta, perto da entrada.

O agente calcula a utilidade de cada alternativa considerando:

- distância;
- preço;
- bônus pela cobertura.

A escolha final depende dos pesos utilizados.

---

## Testes do estacionamento

Foram utilizadas três configurações diferentes.

### Configuração 1

```python
{
    'peso_distancia': 1,
    'peso_preco': 1,
    'bonus_coberta': 0
}
```

**Resultado:** Vaga descoberta, perto da entrada.

**Explicação:** distância e preço possuem o mesmo peso e não existe benefício adicional para vagas cobertas, favorecendo a opção de menor custo total.

---

### Configuração 2

```python
{
    'peso_distancia': 0.2,
    'peso_preco': 3,
    'bonus_coberta': 0
}
```

**Resultado:** Vaga descoberta, perto da entrada.

**Explicação:** o preço passa a ter maior importância, favorecendo a vaga mais barata.

---

### Configuração 3

```python
{
    'peso_distancia': 0.2,
    'peso_preco': 1,
    'bonus_coberta': 20
}
```

**Resultado:** Vaga coberta, perto da entrada.

**Explicação:** o bônus atribuído à cobertura passa a compensar o preço maior da vaga.

---

# Meta-agente

A função `meta_agente()` centraliza a escolha do agente de acordo com o cenário.

Exemplo:

```python
def meta_agente(cenario, percepcao):

    if cenario == 'transito':
        return agente_semaforo(percepcao)

    elif cenario == 'navegacao':
        return agente_baseado_objetivo(percepcao)

    elif cenario == 'escolha_rota':
        return agente_utilidade_v2(
            rotas_v2,
            peso_tempo=0.3,
            peso_pedagio=1,
            peso_seguranca=6
        )['nome']

    elif cenario == 'estacionamento':
        return agente_baseado_utilidade_vaga(
            percepcao,
            peso_distancia=0.2,
            peso_preco=1,
            bonus_coberta=20
        )['nome']

    else:
        raise ValueError('Cenário desconhecido')
```

Dessa forma, um único ponto de entrada permite trabalhar com diferentes tipos de agentes e diferentes ambientes.

---

# Como executar o projeto

## 1. Pré-requisitos

É necessário ter o **Python 3** instalado.

Para verificar:

```bash
python --version
```

ou:

```bash
python3 --version
```

O projeto utiliza apenas recursos da biblioteca padrão do Python, portanto não é necessário instalar bibliotecas externas.

---

## 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta:

```bash
cd agentes-unidade1
```

> Substitua `URL_DO_REPOSITORIO` pelo endereço do seu repositório no GitHub.

---

## 3. Executar a demonstração completa

Execute:

```bash
python principal_unidade1.py
```

O programa apresentará no terminal os resultados dos quatro cenários:

```text
=== CENÁRIO 1: TRÂNSITO ===

=== CENÁRIO 2: NAVEGAÇÃO ===

=== CENÁRIO 3: ESCOLHA DE ROTA ===

=== CENÁRIO 4: ESTACIONAMENTO ===

=== TESTES DE CONFIGURAÇÃO DAS VAGAS ===
```

---

## Executando os módulos individualmente

Também é possível executar cada arquivo separadamente.

### Trânsito

```bash
python semaforo.py
```

### Navegação

```bash
python navegacao.py
```

### Escolha de rota

```bash
python utilidade.py
```

### Estacionamento

```bash
python vaga.py
```

Os exemplos de execução foram protegidos com:

```python
if __name__ == '__main__':
```

Assim, os códigos de demonstração não são executados automaticamente quando os módulos são importados por outro arquivo.

---

# Conclusões

O projeto demonstra que diferentes tipos de agentes utilizam estratégias diferentes para tomar decisões.

O **agente reativo** responde diretamente às percepções do ambiente. O **agente baseado em objetivo** escolhe ações para alcançar um estado desejado. Já o **agente baseado em utilidade** permite comparar diferentes alternativas considerando vários critérios e seus respectivos pesos.

No cenário de estacionamento, foi possível observar claramente que **a decisão do agente depende dos critérios considerados mais importantes**. Ao modificar os pesos de distância, preço e cobertura, a vaga escolhida também pode mudar.

Isso mostra, na prática, como a definição da função de utilidade influencia o comportamento de um agente inteligente.

---

# Autoria

**Joice Soato**

Projeto acadêmico — Inteligência Artificial  
Tecnologia em Sistemas Inteligentes  
Fatec Pompéia — SP  
2026

---

## Exercícios contemplados

- Exercício 1 — Teste de pesos para escolha de rotas
- Exercício 2 — Função de utilidade com critério de segurança
- Exercício 3 — Integração dos agentes por meio da `meta_agente()`
- Exercício 4 — Novo cenário de estacionamento
- Desafio — Integração de critérios adicionais de decisão
