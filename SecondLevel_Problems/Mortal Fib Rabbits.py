def Wabbits(n,m):
    # intial rabbit months
    wabbit_list = [0,1,1] # each index is the month (first is month 0)
    month = 3
    death_time = m + 1

    # loop through each month
    while month <= n:
        if month <= m:
            # Normal Fibonacci sequence while no rabbits are dying yet
            wabbit_list.append(wabbit_list[month-1] + wabbit_list[month-2])
        elif month == m+1:
            # the first month the rabbits start dying, the og wabbit pair dies. Without this, we will be out of index
            wabbit_list.append(wabbit_list[month - 1] + wabbit_list[month - 2] - 1)
        else:
            # After month m, rabbits start dying, so subtract those that died
            wabbit_list.append(wabbit_list[month-1] + wabbit_list[month-2] - wabbit_list[month-death_time])
        month += 1

    return wabbit_list[-1]


print(Wabbits(81,19))


