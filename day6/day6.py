import re
with open("input.txt") as f:
    groups = [line.replace("\n", " ").strip() for line in f.read().split("\n\n")]
    any_counts = 0
    every_counts = 0
    for group in groups:
        any_questions = set()
        every_questions = {char for char in group.split(" ")[0]}
        every_copy = every_questions.copy()

        for line in group.split(" "):
            for char in line:
                if char not in any_questions:
                    any_questions.add(char)
            for char in every_questions:
                if char not in {c for c in line} and char in every_copy:
                    every_copy.remove(char)

        any_counts += len(any_questions)
        every_counts += len(every_copy)

    print("Part 1:", any_counts)
    print("Part 2:", every_counts)
