def traversal():
    with open("input_day3.txt") as f:
        lines = f.readlines()
    
    pos = 0
    a = False
    for line in lines:
        print("Line:", line)
        print("We are at line:",lines.index(line))
        print("We are at pos:", pos)
        pos+=1
        
        steps = 0
        if(a and pos >=  len(line)):
            return

        for x in range(len(lines)):
            print("Step taken")
            steps+=1
            
            if(steps == 3):
                if(lines[x] == "#"):
                    print("A tree, X")
                else:
                    print("Not a tree, O")

                pos = pos + (x)           
                print("which index am i at?", pos)
                a = True
                break
global pos
traversal()
