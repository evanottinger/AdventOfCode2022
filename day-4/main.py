#!/usr/bin/env python3

def main():
    input = []
    with open("input/input.txt", "r") as f:
        input = f.readlines()

    sections = []
    full_overlap = 0
    any_overlap = 0
    for line in input:
        section = line.replace("\n", "").split(",")
        sections.append(section)
        elf_1 = section[0].split("-")
        range_elf_1 = [x for x in range(int(elf_1[0]), int(elf_1[1]) + 1)]
        
        elf_2 = section[1].split("-")
        range_elf_2 = [x for x in range(int(elf_2[0]), int(elf_2[1]) + 1)]

        if all(x in range_elf_2 for x in range_elf_1) or all(x in range_elf_1 for x in range_elf_2):
            full_overlap += 1

        if bool(set(range_elf_1) & set(range_elf_2)):
            any_overlap += 1
        

    print(full_overlap, any_overlap)

if __name__ == "__main__":
    main()