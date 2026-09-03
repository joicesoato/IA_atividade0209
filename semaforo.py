# -*- coding: utf-8 -*-

import random


class AmbienteSemaforo:

    def __init__(self):
        self.carros = {
            'RuaA': random.randint(0, 20),
            'RuaB': random.randint(0, 20)
        }

        self.sinal_verde = 'RuaA'

    def perceber(self):
        return dict(self.carros)

    def executar(self, acao):
        self.sinal_verde = acao

        for rua in self.carros:
            if rua == acao:
                self.carros[rua] = max(
                    0,
                    self.carros[rua] - random.randint(3, 6)
                )
            else:
                self.carros[rua] += random.randint(0, 4)


def agente_semaforo(percepcao):

    if percepcao['RuaA'] >= percepcao['RuaB']:
        return 'RuaA'

    return 'RuaB'


# Desafio da Aula 5:
# agente reativo com margem de segurança.
# Ele só troca de sinal quando a diferença entre as filas
# atinge a margem definida e o sinal já permaneceu ativo
# durante o número mínimo de ciclos.


class AgenteSemaforoComMargem:

    def __init__(self, margem=5, ciclos_minimos=2):

        self.sinal_atual = 'RuaA'
        self.ciclos_no_sinal_atual = 0
        self.margem = margem
        self.ciclos_minimos = ciclos_minimos

    def oposto(self):

        if self.sinal_atual == 'RuaA':
            return 'RuaB'

        return 'RuaA'

    def decidir(self, percepcao):

        diferenca = (
            percepcao[self.oposto()]
            - percepcao[self.sinal_atual]
        )

        pode_trocar = (
            self.ciclos_no_sinal_atual
            >= self.ciclos_minimos
        )

        if pode_trocar and diferenca >= self.margem:

            self.sinal_atual = self.oposto()
            self.ciclos_no_sinal_atual = 0

        else:

            self.ciclos_no_sinal_atual += 1

        return self.sinal_atual


if __name__ == '__main__':

    print("=== AGENTE REATIVO — SEMÁFORO ===")

    ambiente = AmbienteSemaforo()

    print("Estado inicial:", ambiente.carros)

    for ciclo in range(1, 6):

        percepcao = ambiente.perceber()

        acao = agente_semaforo(percepcao)

        ambiente.executar(acao)

        print(
            f"Ciclo {ciclo}: "
            f"percebeu {percepcao} "
            f"-> abre para {acao} "
            f"| novo estado: {ambiente.carros}"
        )

    print("\n=== AGENTE COM MARGEM DE SEGURANÇA ===")

    ambiente = AmbienteSemaforo()

    agente_margem = AgenteSemaforoComMargem(
        margem=5,
        ciclos_minimos=2
    )

    print("Estado inicial:", ambiente.carros)

    for ciclo in range(1, 6):

        percepcao = ambiente.perceber()

        acao = agente_margem.decidir(percepcao)

        ambiente.executar(acao)

        print(
            f"Ciclo {ciclo}: "
            f"{percepcao} -> {acao}"
        )