from semaforo import (
    AmbienteSemaforo,
    agente_semaforo,
    AgenteSemaforoComMargem
)

from navegacao import (
    AmbienteMapa,
    agente_baseado_objetivo,
    agente_com_obstaculos
)

from utilidade import (
    rotas,
    rotas_v2,
    agente_baseado_utilidade,
    agente_utilidade_v2
)

from vaga import (
    vagas,
    agente_baseado_utilidade_vaga
)


# Função responsável por direcionar cada cenário
# para o agente correspondente.


def meta_agente(cenario, percepcao=None):

    # CENÁRIO TRANSITO
    #
    # Tipo: agente reativo.
    # O agente reage diretamente à quantidade de carros
    # percebida nas duas ruas.


    if cenario == 'transito':

        return agente_semaforo(percepcao)


    # CENÁRIO NAVEGACAO
    #
    # Tipo: agente baseado em objetivos.
    # O agente possui como objetivo chegar ao destino
    # e escolhe uma ação que aproxima sua posição do objetivo.


    elif cenario == 'navegacao':

        return agente_baseado_objetivo(
            percepcao
        )


    # CENÁRIO ESCOLHA_ROTA
    #
    # Tipo: agente baseado em utilidade.
    # O agente compara as rotas considerando tempo,
    # pedágio e segurança.


    elif cenario == 'escolha_rota':

        pesos = {
            'peso_tempo': 0.3,
            'peso_pedagio': 1,
            'peso_seguranca': 6
        }

        return agente_utilidade_v2(
            rotas_v2,
            **pesos
        )['nome']


    # CENÁRIO ESTACIONAMENTO
    #
    # Tipo: agente baseado em utilidade.
    # O agente compara distância, preço e cobertura
    # para escolher a vaga mais vantajosa.


    elif cenario == 'estacionamento':

        return agente_baseado_utilidade_vaga(
            vagas,
            peso_distancia=0.2,
            peso_preco=1,
            bonus_coberta=20
        )['nome']


    else:

        raise ValueError(
            'Cenário desconhecido'
        )


# Demonstração completa.


if __name__ == '__main__':

    print("=" * 50)
    print("DEMONSTRAÇÃO — AGENTES INTELIGENTES")
    print("=" * 50)


    # -------------------------------------------------
    # 1. TRÂNSITO
    # -------------------------------------------------

    print("\n1. CENÁRIO: TRÂNSITO")

    ambiente = AmbienteSemaforo()

    percepcao = ambiente.perceber()

    acao = meta_agente(
        'transito',
        percepcao
    )

    print(
        "Percepção:",
        percepcao
    )

    print(
        "Ação escolhida:",
        acao
    )


    # -------------------------------------------------
    # 2. NAVEGAÇÃO
    # -------------------------------------------------

    print("\n2. CENÁRIO: NAVEGAÇÃO")

    ambiente = AmbienteMapa()

    percepcao = ambiente.perceber()

    acao = meta_agente(
        'navegacao',
        percepcao
    )

    print(
        "Posição:",
        ambiente.posicao
    )

    print(
        "Objetivo:",
        ambiente.objetivo
    )

    print(
        "Ação escolhida:",
        acao
    )


    # -------------------------------------------------
    # 3. ESCOLHA DE ROTA
    # -------------------------------------------------

    print("\n3. CENÁRIO: ESCOLHA DE ROTA")

    rota_escolhida = meta_agente(
        'escolha_rota'
    )

    print(
        "Rota escolhida:",
        rota_escolhida
    )


    # -------------------------------------------------
    # 4. ESTACIONAMENTO
    # -------------------------------------------------

    print("\n4. CENÁRIO: ESTACIONAMENTO")

    vaga_escolhida = meta_agente(
        'estacionamento'
    )

    print(
        "Vaga escolhida:",
        vaga_escolhida
    )


    # -------------------------------------------------
    # DESAFIO DA AULA 5 — MARGEM DE SEGURANÇA
    # -------------------------------------------------

    print("\n5. DESAFIO: MARGEM DE SEGURANÇA")

    agente_margem = AgenteSemaforoComMargem(
        margem=5,
        ciclos_minimos=2
    )

    percepcao = ambiente_semaforo = AmbienteSemaforo().perceber()

    acao = agente_margem.decidir(
        percepcao
    )

    print(
        "Percepção:",
        percepcao
    )

    print(
        "Ação com margem:",
        acao
    )


    print("\n" + "=" * 50)
    print("DEMONSTRAÇÃO FINALIZADA")
    print("=" * 50)

def meta_agente(cenario, percepcao):

    if cenario == 'transito':
        # Agente reativo:
        # escolhe a ação diretamente com base na percepção atual.
        return agente_semaforo(percepcao)

    elif cenario == 'navegacao':
        # Agente baseado em objetivo:
        # escolhe a ação para alcançar a posição objetivo.
        return agente_baseado_objetivo(percepcao)

    elif cenario == 'escolha_rota':
        # Agente baseado em utilidade:
        # considera tempo, pedágio e segurança.
        #
        # Aqui também foi integrado o desafio da Aula 7,
        # adicionando o critério de segurança.
        escolhida = agente_utilidade_v2(
            rotas_v2,
            peso_tempo=0.3,
            peso_pedagio=1,
            peso_seguranca=6
        )

        return escolhida['nome']

    elif cenario == 'estacionamento':
        # Agente baseado em utilidade:
        # compara distância, preço e benefício de uma vaga coberta.
        escolhida = agente_baseado_utilidade_vaga(
            percepcao,
            peso_distancia=0.2,
            peso_preco=1,
            bonus_coberta=20
        )

        return escolhida['nome']

    else:
        raise ValueError('Cenário desconhecido')

if __name__ == '__main__':

    print('=== CENÁRIO 1: TRÂNSITO ===')

    ambiente = AmbienteSemaforo()
    percepcao = ambiente.perceber()

    print('Percepção:', percepcao)
    print('Ação:', meta_agente('transito', percepcao))


    print('\n=== CENÁRIO 2: NAVEGAÇÃO ===')

    ambiente = AmbienteMapa(
        tamanho=5,
        posicao_inicial=(0, 0)
    )

    percepcao = ambiente.perceber()

    print('Percepção:', percepcao)
    print('Ação:', meta_agente('navegacao', percepcao))


    print('\n=== CENÁRIO 3: ESCOLHA DE ROTA ===')

    print(
        'Rota escolhida:',
        meta_agente('escolha_rota', rotas_v2)
    )


    print('\n=== CENÁRIO 4: ESTACIONAMENTO ===')

    print(
        'Vaga escolhida:',
        meta_agente('estacionamento', vagas)
    )


    print('\n=== TESTES DE CONFIGURAÇÃO DAS VAGAS ===')

    configuracoes = [
        {
            'peso_distancia': 1,
            'peso_preco': 1,
            'bonus_coberta': 0
        },
        {
            'peso_distancia': 0.2,
            'peso_preco': 3,
            'bonus_coberta': 0
        },
        {
            'peso_distancia': 0.2,
            'peso_preco': 1,
            'bonus_coberta': 20
        }
    ]

    for configuracao in configuracoes:

        escolhida = agente_baseado_utilidade_vaga(
            vagas,
            **configuracao
        )

        print(
            configuracao,
            '->',
            escolhida['nome']
        )