with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = [i.strip() for i in f.readlines()]

def main():
    sum_of_jolts = 0
    for battery in raw_input:
        battery_jolts = calc_battery_jolts(battery=battery)
        sum_of_jolts += battery_jolts
    print(sum_of_jolts)

def calc_battery_jolts(battery: str) -> int:
    cur_max = int(battery[:2])

    for i in battery[2:]:
        first_candidate = int(str(cur_max)[0] + i)
        second_candidate = int(str(cur_max)[1] + i)

        if first_candidate > cur_max:
            cur_max = first_candidate
        if second_candidate > cur_max:
            cur_max = second_candidate

    return cur_max

if __name__ == '__main__':
    main()
