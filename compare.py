#!/usr/bin/env python
import sys


def main(argv):
    GG = set()
    with open('ggautoblocker/sourcelist.txt', 'r') as gg:
        for line in gg:
            GG.add(line.strip())

    overlap = []
    with open('sjwautoblocker/block_names.txt') as sjw:
        for line in sjw:
            name = line.strip()
            if name in GG:
                overlap.append(name)
    print("Well done geniuses, you successfully blocked %d of your own clowns"
          % len(overlap))

    if '-v' in argv:
        print repr(overlap)


if __name__ == '__main__':
    main(sys.argv)
