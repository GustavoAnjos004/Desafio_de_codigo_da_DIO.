name = input("Qual o seu nome: ")
xp = None 
lv = ""

while xp is None:
    try:
        xp = int(input("Qual o seu nivel (digite um número): "))
    except ValueError:
        print("Por favor, digite um número válido.")

if xp <= 1000:
    lv = "Ferro"
elif 1001 <= xp <= 2000:
    lv = "Bronze"
elif 2001 <= xp <= 6000:
    lv = "Prata"
elif 6001 <= xp <= 7000:
    lv = "Ouro"
elif 7001 <= xp <= 8000:
    lv = "Platina"
elif 8001 <= xp <= 9000:
    lv = "Ascendente"
elif 9001 <= xp <= 10000:
    lv = "Imortal"
elif xp >= 10001:
    lv = "Radiante"

print("Olá {}, seus equipamentos são de nível {}.".format(name, lv))