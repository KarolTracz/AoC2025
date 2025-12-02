with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = f.read().split(',')

def main():
    result = []
    for id_range in raw_input:
        start, end = id_range.split('-')

        try:
            search_start = int(start[:len(start)//2])
        except ValueError:
            search_start = int(start)


        start, end = int(start), int(end)
        range_size = end - start

        # print(f'{range_size=}')
        for i in range(search_start,search_start+range_size):
            if start <= int(str(i) + str(i)) <= end:
                print(start, end, str(i) + str(i))
                result.append(int(str(i) + str(i)))

    print(sum(result))



if __name__ == '__main__':
    main()
