with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = [i.split() for i in f.readlines()]

for i, line in enumerate(raw_input[:-1]):
    raw_input[i] = list(map(int, line))
signs = [i for i in raw_input[-1]]

def main():
    result_1 = 0
    result_2 = 0

    for i, sign in enumerate(raw_input[-1]):
        if sign == '+':
            result_1 += raw_input[0][i] + raw_input[1][i] + raw_input[2][i] + raw_input[3][i]
        elif sign == '*':
            result_1 += raw_input[0][i] * raw_input[1][i] * raw_input[2][i] * raw_input[3][i]

    print(result_1)

if __name__ == '__main__':
    main()
