def loop_year(year):
    x = 0
    while x < 20:
        if year % 4 != 0 and year % 400 != 0:
            year = year + 1
        elif year % 100 != 0:
            year = year +1
            print(f" {year} is a leap year ")
            x += 1


loop_year(2020)   