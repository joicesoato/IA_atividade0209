# -*- coding: utf-8 -*-


class AmbienteMapa:

    def __init__(self, tamanho=5, posicao_inicial=(0, 0)):

        self.tamanho = tamanho
        self.posicao = posicao_inicial
        self.objetivo = (tamanho - 1, tamanho - 1)

    def perceber(self):

        return self.posicao, self.objetivo

    def executar(self, acao):

        x, y = self.posicao

        if acao == 'Direita' and x < self.tamanho - 1:
            x += 1

        elif acao == 'Esquerda' and x > 0:
            x -= 1

        elif acao == 'Baixo' and y < self.tamanho - 1:
            y += 1

        elif acao == 'Cima' and y > 0:
            y -= 1

        self.posicao = (x, y)


# Agente baseado em objetivos.
# O objetivo é chegar à posição definida no mapa.
# O agente escolhe ações que reduzem a distância até o objetivo.


def agente_baseado_objetivo(percepcao):

    (x, y), (gx, gy) = percepcao

    if x < gx:
        return 'Direita'

    if x > gx:
        return 'Esquerda'

    if y < gy:
        return 'Baixo'

    if y > gy:
        return 'Cima'

    return 'Parar'


# Função auxiliar para verificar se uma posição está livre.


def posicao_livre(pos, obstaculos, tamanho):

    x, y = pos

    dentro = (
        0 <= x < tamanho
        and 0 <= y < tamanho
    )

    return dentro and pos not in obstaculos


# Desafio da Aula 6:
# agente baseado em objetivos que tenta desviar de obstáculos.


def agente_com_obstaculos(
    percepcao,
    obstaculos,
    tamanho
):

    (x, y), (gx, gy) = percepcao

    candidatos = []

    if x < gx:
        candidatos.append('Direita')

    if x > gx:
        candidatos.append('Esquerda')

    if y < gy:
        candidatos.append('Baixo')

    if y > gy:
        candidatos.append('Cima')

    for acao in candidatos:

        nx, ny = x, y

        if acao == 'Direita':
            nx += 1

        elif acao == 'Esquerda':
            nx -= 1

        elif acao == 'Baixo':
            ny += 1

        elif acao == 'Cima':
            ny -= 1

        if posicao_livre(
            (nx, ny),
            obstaculos,
            tamanho
        ):
            return acao

    return 'Parar'


def mover(pos, acao):

    x, y = pos

    if acao == 'Direita':
        x += 1

    elif acao == 'Esquerda':
        x -= 1

    elif acao == 'Baixo':
        y += 1

    elif acao == 'Cima':
        y -= 1

    return x, y


if __name__ == '__main__':

    print("=== AGENTE BASEADO EM OBJETIVOS ===")

    ambiente = AmbienteMapa()

    print(
        f"Início: {ambiente.posicao} "
        f"-> Objetivo: {ambiente.objetivo}"
    )

    for passo in range(1, 12):

        percepcao = ambiente.perceber()

        acao = agente_baseado_objetivo(
            percepcao
        )

        if acao == 'Parar':

            print(
                f"Chegou ao objetivo em "
                f"{ambiente.posicao}"
            )

            break

        ambiente.executar(acao)

        print(
            f"Passo {passo}: "
            f"{acao} -> {ambiente.posicao}"
        )

    print("\n=== NAVEGAÇÃO COM OBSTÁCULOS ===")

    tamanho = 5

    obstaculos = [
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2)
    ]

    posicao = (0, 0)
    objetivo = (4, 4)

    print("Obstáculos:", obstaculos)
    print(
        f"Início: {posicao} "
        f"-> Objetivo: {objetivo}"
    )

    for passo in range(1, 15):

        acao = agente_com_obstaculos(
            (posicao, objetivo),
            obstaculos,
            tamanho
        )

        if acao == 'Parar':

            print(
                f"Preso em {posicao}"
            )

            break

        nova_posicao = mover(
            posicao,
            acao
        )

        print(
            f"{passo}. {acao} "
            f"-> {nova_posicao}"
        )

        posicao = nova_posicao

        if posicao == objetivo:

            print("Chegou ao objetivo!")

            break