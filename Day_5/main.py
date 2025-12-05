with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = [i.strip() for i in f.readlines()]
ids = [i for i in raw_input[raw_input.index('')+1:]]
ranges = [i for i in raw_input[:raw_input.index('')]]

print(raw_input)
print(f'{len(ranges)} {ranges=}')
print(f'{len(ids)} {ids=}')


def main():
    result_1 = 0
    for id_ in ids:
        id_ = int(id_)
        for ran in ranges:
            start, end = ran.split('-')
            start, end = int(start), int(end)
            if id_ in range(start, end+1):
                result_1 += 1
                break
    print(result_1)

if __name__ == '__main__':
    main()
