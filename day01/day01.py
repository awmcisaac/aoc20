with open("input.txt") as f:
    inpt = set()
    for line in f.readlines():
        inpt.add(int(line))
    total = 2020
    # part 1
    for elem in inpt:
        contra = total - elem
        if contra in inpt:
            print(elem*contra)
    # part 2
    for el1 in inpt:
        for el2 in inpt:
            contra = total - el1 - el2
            if contra in inpt:
                print(el1*el2*contra)
