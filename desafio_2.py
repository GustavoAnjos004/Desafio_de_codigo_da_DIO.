def get_valid_number(value):
    while True:
        try:
            number = int(input(value))
            return number
        except ValueError:
            print("Por favor, digite um número válido.")

victories = get_valid_number ("Qual o seu saldo de vitórias (digite um número): ")
defeats = get_valid_number ("Qual o seu saldo de derrotas (digite um número): ")

lv = (victories-defeats)

if lv <= 0:
    classification = "lets play another game, son!"
elif lv <= 10:
    classification = "Ferro"
elif 11 <= lv <= 20:
    classification = "Bronze"
elif 21 <= lv <= 50:
    classification = "Prata"
elif 51 <= lv <= 80:
    classification = "Ouro"
elif 81 <= lv <= 90:
    classification = "Diamante"
elif 91 <= lv <= 100:
    classification = "Lendário"
elif lv <= 101:
    classification = "Imortal"

print("O Herói tem de saldo de {} vitorias e está no nível: {}".format(lv, classification))