with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = [i.strip() for i in f.readlines()]

def main():
    sum_of_jolts_part_1 = 0
    sum_of_jolts_part_2 = 0
    for battery in raw_input:
        battery_jolts_2 = calc_battery_jolts(battery=battery, lenght=2)
        sum_of_jolts_part_1 += battery_jolts_2

        battery_jolts_12 = calc_battery_jolts(battery=battery, lenght=12)
        sum_of_jolts_part_2 += battery_jolts_12

    print(sum_of_jolts_part_1)
    print(sum_of_jolts_part_2)

def calc_battery_jolts(battery: str, lenght: int) -> int:
    cur_max = battery[:lenght]

    for jolt in battery[lenght:]:
        best = cur_max

        for i in range(lenght):
            candidate = cur_max[:i] + cur_max[i+1:] + jolt
            if int(candidate) > int(best):
                best = candidate
        cur_max = best

    return int(cur_max)

if __name__ == '__main__':
    main()
