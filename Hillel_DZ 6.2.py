time = int(input("Введить секунди: "))

if 0 <= time < 8640000:
    days = time // (24 * 60 * 60)
    hours, rem = divmod(time % (24 * 60 * 60), 3600)
    min, sec = divmod(rem, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_str = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_str = "дні"
    else:
        day_str = "днів"

    print(f"{days} {day_str}, \
{str(hours).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")
else:
    print("Помилка, невірне число")
