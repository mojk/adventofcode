
def findProductOfTwo():
    print("---- PART 1 ----")
    with open("input_day1.txt") as f:
        lines = [int(x) for x in f.read().split()]
        for value in lines:
            for value2 in lines:
                if(value + value2 == 2020):
                    print(value*value2)
                    return


def findProductOfThree():
    print("---- PART 2 ----")
    with open("input_day1.txt") as f:
        lines = [int(x) for x in f.read().split()]
        for value in lines:
            for value2 in lines:
                for value3 in lines:
                    if(value + value2 + value3 == 2020):
                        print(value*value2*value3)
                        return

findProductOfTwo()
findProductOfThree()
