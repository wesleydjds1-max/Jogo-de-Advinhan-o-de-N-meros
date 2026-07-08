# ==========================================
# Jogo de Adivinhação de Números
# Autor: Wesley
# ==========================================

import random
import time

# Estatísticas
vitorias = 0
derrotas = 0
pontuacao = 0
recorde = None
historico = []


while True:

    print("\n" + "=" * 40)
    print("      JOGO DE ADIVINHAÇÃO")
    print("=" * 40)

    # --------------------------
    # Escolha da dificuldade
    # --------------------------

    print("\nEscolha a dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Difícil (2 tentativas)")

    while True:

        dificuldade = input("Opção: ")

        if dificuldade == "1":
            tentativas = 10
            break

        elif dificuldade == "2":
            tentativas = 5
            break

        elif dificuldade == "3":
            tentativas = 2
            break

        print("Escolha uma opção válida.")

    numero_secreto = random.randint(1, 100)

    tentativas_iniciais = tentativas

    inicio = time.time()

    venceu = False

    # --------------------------
    # Jogo
    # --------------------------

    while tentativas > 0:

        while True:

            try:

                palpite = int(input("\nDigite um número entre 1 e 100: "))

                if 1 <= palpite <= 100:
                    break

                print("Digite um número entre 1 e 100.")

            except ValueError:
                print("Digite apenas números inteiros.")

        if palpite == numero_secreto:

            fim = time.time()

            tempo = round(fim - inicio, 2)

            usadas = tentativas_iniciais - tentativas + 1

            print("\n🎉 Parabéns!")
            print(f"Você acertou em {usadas} tentativa(s).")
            print(f"Tempo: {tempo} segundos.")

            venceu = True

            vitorias += 1

            # Pontuação
            pontos = (tentativas * 10) + 10
            pontuacao += pontos

            # Recorde
            if recorde is None or usadas < recorde:
                recorde = usadas
                print("🏆 Novo recorde!")

            historico.append("Vitória")

            break

        elif palpite < numero_secreto:

            print("O número é MAIOR.")

        else:

            print("O número é MENOR.")

        tentativas -= 1

        if tentativas > 0:
            print(f"Tentativas restantes: {tentativas}")

    if not venceu:

        derrotas += 1

        historico.append("Derrota")

        print("\nGame Over!")
        print(f"O número era {numero_secreto}.")

    # --------------------------
    # Estatísticas
    # --------------------------

    print("\n========== PLACAR ==========")
    print(f"Vitórias : {vitorias}")
    print(f"Derrotas : {derrotas}")
    print(f"Pontuação: {pontuacao}")

    if recorde is None:
        print("Recorde: ---")
    else:
        print(f"Recorde: {recorde} tentativa(s)")

    print("\nHistórico:")

    for indice, resultado in enumerate(historico, start=1):
        print(f"{indice}. {resultado}")

    # --------------------------
    # Jogar novamente
    # --------------------------

    while True:

        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()

        if resposta in ("s", "n"):
            break

        print("Digite apenas 's' ou 'n'.")

    if resposta == "n":
        break

print("\n===================================")
print("Obrigado por jogar!")
print("=========== RESUMO ===========")
print(f"Vitórias : {vitorias}")
print(f"Derrotas : {derrotas}")
print(f"Pontuação Final: {pontuacao}")

if recorde is not None:
    print(f"Melhor partida: {recorde} tentativa(s)")

print("Até a próxima!")
    