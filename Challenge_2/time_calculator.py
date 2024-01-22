def calculator():
    day = 0
    time = '06:30 PM'
    time = time.split(' ')
    period = time[1]
    numbers = time[0].split(':')
    time1 = int(numbers[0])
    time2 = int(numbers[1])
    dif = '205:12'
    dif = dif.split(':')
    dif1 = int(dif[0])
    dif2 = int(dif[1])
    hour1 = time1 + dif1
    hour2 = time2 + dif2
    while hour2 > 60:
        hour1 += 1
        hour2 -= 60
    if period == 'AM':
        if hour1 > 12:
            hour1 -= 12
            print(f'{hour1}:{hour2} PM')
        elif hour1 == 12:
            print(f'{hour1}:{hour2} PM')
        else:
            print(f'{hour1}:{hour2} AM')
    if period == 'PM':
        while period == 'PM' and hour1 > 12:
            day += 1
            hour1 -= 12
        if day > 0:
            if hour1 > 12:
                hour1 -= 12
                print(f'{hour1}:{hour2}, AM, {day} days later.')
            elif hour1 == 12:
                print(f'{hour1}:{hour2}, AM, {day} days later.')
            else:
                print(f'{hour1}:{hour2}, PM, {day} days later.')
        elif hour1 > 12:
                hour1 -= 12
                print(f'{hour1}:{hour2}, AM, {day} days later.')
        elif hour1 == 12:
            print(f'{hour1}:{hour2}, PM, {day} days later.')
        else:
                print(f'{hour1}:{hour2}, PM, {day} days later.')