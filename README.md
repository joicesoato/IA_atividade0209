# Agentes Inteligentes — Unidade 1

Projeto desenvolvido para a Unidade 1 da disciplina de Inteligência Artificial.

O projeto reúne três tipos de agentes estudados nas Aulas 5, 6 e 7 e adiciona um quarto cenário de estacionamento.

## Estrutura do projeto

### semaforo.py

Implementa um agente reativo para controle de um semáforo.

O agente percebe a quantidade de carros nas ruas RuaA e RuaB e decide para qual rua abrir o sinal.

Também contém o desafio da Aula 5, utilizando margem de segurança e quantidade mínima de ciclos antes de trocar o sinal.

### navegacao.py

Implementa um agente baseado em objetivos.

O agente navega em uma grade 5×5, partindo de uma posição inicial até um objetivo.

O arquivo também contém uma versão que tenta desviar de obstáculos.

### utilidade.py

Implementa agentes baseados em utilidade.

As rotas são avaliadas considerando:

- tempo;
- pedágio;
- nível de segurança.

A função `utilidade_v2` permite atribuir pesos diferentes para cada critério.

### vaga.py

Implementa o quarto cenário do projeto: estacionamento.

O agente escolhe entre três vagas considerando:

- distância até a entrada;
- preço;
- se a vaga é coberta.

Os pesos podem ser alterados para modificar a escolha.

### principal_unidade1.py

É o arquivo principal do projeto.

A função `meta_agente()` direciona cada cenário para o agente correspondente.

Os quatro cenários disponíveis são:

- `transito`
- `navegacao`
- `escolha_rota`
- `estacionamento`

## Tipos de agentes

| Cenário | Tipo de agente | Justificativa |
|---|---|---|
| Trânsito | Reativo | Reage diretamente à percepção das filas de carros |
| Navegação | Baseado em objetivos | Procura alcançar uma posição objetivo |
| Escolha de rota | Baseado em utilidade | Compara alternativas usando tempo, pedágio e segurança |
| Estacionamento | Baseado em utilidade | Compara distância, preço e cobertura |

## Desafio integrado

Foi integrado ao projeto o desafio da Aula 5 referente à margem de segurança do semáforo.

O agente `AgenteSemaforoComMargem` evita trocas excessivas de sinal, exigindo uma diferença mínima entre as filas e um número mínimo de ciclos antes de realizar uma troca.

## Como executar

É necessário ter Python instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python principal_unidade1.py

Esse comando executa a demonstração dos quatro cenários.

Também é possível executar cada agente individualmente:

```bash
python semaforo.py
python navegacao.py
python utilidade.py
python vaga.py