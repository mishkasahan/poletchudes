import random


spysok_sliv = ('молоко', 'корова', 'лис', 'смерека', 'хата')
b = random.choice(spysok_sliv)
n = ["*" for i in b]
print("".join(n))
c = int(input("Введіть кількість спроб:"))

while True:
    k = input('Введіть букву або слово повністю:')
    if len(k) == 1:
        if k in b:
            for i in range(len(b)):
                if k == b[i]:
                    n[i] = k
            print("".join(n))
        else:
            print("Такої літери немає!")
            print("".join(n))
            c += -1
    else:
        if k == b:
            print("Вітаю, ви вгадали слово")
            break
        else:
            print("Слово не вірне!")
            print("".join(n))
            c += -1
    if "*" not in n:
        print("Вітаю, ви вгадали слово")
        break
    if c == 0:
        print("Кількість спроб закінчилась. Ви програли!")
        break
