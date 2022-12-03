#!/usr/bin/env python3

ITEM_OPTS = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    input = []

    with open("input/input.txt", "r") as f:
        input = f.readlines()


    total = 0
    for line in input:
        pouch_1 = [*line.replace("\n", "")[0:len(line)//2]]
        pouch_2 = [*line.replace("\n", "")[len(line)//2:]]
        
        for item in pouch_1:
            if item in pouch_2:
                total += ITEM_OPTS.index(item)
                break

    print(total)

    group = []
    groups = []
    for line in input:
        group.append(line)

        if (input.index(line) + 1) % 3 == 0:
            groups.append(group)
            group = []
    
    total = 0
    for group in groups:
        elf_1 = group[0]
        elf_2 = group[1]
        elf_3 = group[2]

        for item in elf_1:
            if item in elf_2 and item in elf_3:
                total += ITEM_OPTS.index(item)
                break

    print(total)

if __name__ == "__main__":
    main()