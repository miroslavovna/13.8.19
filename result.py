kol_vo = int(input("Введите количество билетов и нажмите enter: "))
print("Введите возраст для каждого участника и нажмите enter: ")
summa = 0

for i in range(kol_vo):
    vozrast = int(input("Возраст (полных лет): "))
    if vozrast < 18:
        summa += 0
    elif vozrast >= 25:
        summa += 1390
    else:
        summa += 990

if kol_vo < 3:
    itogo = summa
else:
    itogo = summa*0.9

print("К оплате: " , itogo)

