numb_tick = int(input("Введите количество посетителей: "))
numb_tick_1 = numb_tick
tot_summ = 0
summ = 0
while 0 < numb_tick:
    numb_tick = numb_tick - 1
    age = int(input("Сколько посетителю лет? "))
    if age < 18:
        summ += 0
    elif 18 <= age <= 25:
        summ += 990
    else:
        summ += 1390
if numb_tick_1 > 3:
    tot_summ = summ * 0.9
    print("Сумма к оплате: ", str(tot_summ), ' рублей')
else:
    tot_summ = summ
    print("Сумма к оплате: ", str(tot_summ), ' рублей')
