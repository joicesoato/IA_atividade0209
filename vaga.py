vagas = [
    {
        'nome': 'Vaga coberta, longe da entrada',
        'distancia_m': 80,
        'preco': 8.0,
        'coberta': True
    },
    {
        'nome': 'Vaga descoberta, perto da entrada',
        'distancia_m': 15,
        'preco': 6.0,
        'coberta': False
    },
    {
        'nome': 'Vaga coberta, perto da entrada',
        'distancia_m': 20,
        'preco': 12.0,
        'coberta': True
    },
]


def utilidade_vaga(
    vaga,
    peso_distancia=1.0,
    peso_preco=1.0,
    bonus_coberta=0.0
):
    custo = (
        peso_distancia * vaga['distancia_m']
        + peso_preco * vaga['preco']
    )

    beneficio = bonus_coberta if vaga['coberta'] else 0

    return beneficio - custo


def agente_baseado_utilidade_vaga(vagas, **pesos):
    return max(
        vagas,
        key=lambda v: utilidade_vaga(v, **pesos)
    )


if __name__ == '__main__':

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