
def findValidPws():
    with open("input_day2.txt") as f:
        lines = f.readlines()
        for x in range (len(lines)):
            policy = lines[x].split(" ")[0]
            letter = lines[x].split(" ")[1][0]
            string = lines[x].split(":")[1].strip()

            minimum = int(policy.split("-")[0])
            maximum = int(policy.split("-")[1])
            count = 0
            for char in string:
                if(char==letter):
                    count+=1
            
            print("Number of occurances", count)
            print("Min",minimum)
            print("max",maximum)
            if(count >= minimum and count <= maximum):
                print("PASS")

def findValidPwsNew():
    with open("input_day2.txt") as f:
        lines = f.readlines()
        for x in range (len(lines)):
            policy = lines[x].split(" ")[0]
            letter = lines[x].split(" ")[1][0]
            string = lines[x].split(":")[1].strip()
            string = "X" + string

            validPos1 = int(policy.split("-")[0])
            validPos2 = int(policy.split("-")[1])

            if(string[validPos1] == letter and string[validPos2] != letter or string[validPos1] != letter and string[validPos2] == letter):
                print("YES")

findValidPwsNew()

