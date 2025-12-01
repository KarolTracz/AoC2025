with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = f.readlines()
    raw_input_strip = [i.strip() for i in raw_input]

def main():
    # Lxx or Rxx indicate Left or Right movement of dial, number indicate distance
    # So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19.
    # After that, a rotation of L19 would cause it to point at 0.
    # Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
    #
    # The dial starts by pointing at 50.

    score = 0
    dial = 50

    for line in raw_input_strip:
        direction = line[0]
        distance = int(line[1:])

        if dial == 0:
            score += 1

        if direction == 'L':
            dial -= int(str(distance)[-2:])
            if dial < 0:
                dial = 100 + dial
        elif direction == 'R':
            dial += int(str(distance)[-2:])
            if dial > 99:
                dial = -100 + dial
    print(f'{score=}')

if __name__ == '__main__':
    main()
