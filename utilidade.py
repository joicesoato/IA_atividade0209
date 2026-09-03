# -*- coding: utf-8 -*-


# Rotas utilizadas no exercício original da Aula 7.

rotas = [

    {
        'nome': 'Avenida Central',
        'tempo_min': 28,
        'pedagio': 0
    },

    {
        'nome': 'Marginal',
        'tempo_min': 22,
        'pedagio': 4.5
    },

    {
        'nome': 'Bairro Industrial',
        'tempo_min': 35,
        'pedagio': 0
    }

]


def utilidade(
    rota,
    peso_tempo=1.0,
    peso_pedagio=2.0
):

    custo = (
        peso_tempo * rota['tempo_min']
        + peso_pedagio * rota['pedagio']
    )

    return -custo


def agente_baseado_utilidade(
    rotas,
    **pesos
):

    return max(
        rotas,
        key=lambda r: utilidade(
            r,
            **pesos
        )
    )


# Versão com segurança.
# O agente considera tempo, pedágio e nível de segurança.
# Isso representa um agente baseado em utilidade porque
# compara alternativas de acordo com diferentes critérios.


rotas_v2 = [

    {
        'nome': 'Avenida Central',
        'tempo_min': 28,
        'pedagio': 0,
        'nivel_seguranca': 4
    },

    {
        'nome': 'Marginal',
        'tempo_min': 22,
        'pedagio': 4.5,
        'nivel_seguranca': 3
    },

    {
        'nome': 'Bairro Industrial',
        'tempo_min': 35,
        'pedagio': 0,
        'nivel_seguranca': 5
    }

]


def utilidade_v2(
    rota,
    peso_tempo=1.0,
    peso_pedagio=2.0,
    peso_seguranca=0.0
):

    custo = (
        peso_tempo * rota['tempo_min']
        + peso_pedagio * rota['pedagio']
    )

    beneficio = (
        peso_seguranca
        * rota['nivel_seguranca']
    )

    return beneficio - custo


def agente_utilidade_v2(
    rotas,
    **pesos
):

    return max(
        rotas,
        key=lambda r: utilidade_v2(
            r,
            **pesos
        )
    )


if __name__ == '__main__':

    print("=== AGENTE BASEADO EM UTILIDADE ===")

    escolhida = agente_baseado_utilidade(
        rotas
    )

    for rota in rotas:

        print(
            rota['nome'],
            '-> utilidade:',
            round(
                utilidade(rota),
                2
            )
        )

    print(
        "\nRota escolhida:",
        escolhida['nome']
    )

    print("\n=== TESTE DE PESOS ===")

    configuracoes = [

        {
            'peso_tempo': 1,
            'peso_pedagio': 0
        },

        {
            'peso_tempo': 1,
            'peso_pedagio': 2
        },

        {
            'peso_tempo': 0.2,
            'peso_pedagio': 5
        }

    ]

    for pesos in configuracoes:

        escolhida = agente_baseado_utilidade(
            rotas,
            **pesos
        )

        print(
            f"Pesos: {pesos} "
            f"-> {escolhida['nome']}"
        )

    print("\n=== UTILIDADE COM SEGURANÇA ===")

    pesos_seguranca = {
        'peso_tempo': 0.3,
        'peso_pedagio': 1,
        'peso_seguranca': 6
    }

    escolhida = agente_utilidade_v2(
        rotas_v2,
        **pesos_seguranca
    )

    print(
        "Pesos:",
        pesos_seguranca
    )

    print(
        "Rota escolhida:",
        escolhida['nome']
    )