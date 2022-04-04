from Puzzle import *
import os
print("15-PUZZLE SOLVER")

while(True):
    arrayContext = []
    print("\nMENU")
    print("1. Masukan file (*.txt)")
    print("2. Masukan Command Line")
    print("3. Exit")
    print("Pilih Menu : ", end="")
    select = input()
    print()
    if(select != "3"):
        if(select == "1"):
            fn = input("Input file txt : ")
            contents = open((os.path.join(os.getcwd(), "test",fn)), "r")
            contents = contents.read()
            arrayContext = contents.split()
        elif(select == "2"):
            romawi = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI"]
            print("=======================")
            print("| I  | II  | III | IV |")
            print("=======================")
            print("| V  | VI  | VII | IX |")
            print("=======================")
            print("| IX |  X  | XI  | XII|")
            print("=======================")
            print("|XIII| XIV | XV  | XVI|")
            print("=======================")
            print("Input sesuai box :")
            for x in romawi:
                inp = input(f"{x} : ")
                arrayContext.append(inp)

        elementContent = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]    
        for x in arrayContext:
            if x in elementContent:
                elementContent.remove(x)

        if (len(elementContent) != 0 or len(arrayContext) > 16):
            print("Invalid Input")
        else:
            for i in range(len(arrayContext)):
                arrayContext[i] = int(arrayContext[i])
            
            root = Puzzle(0,arrayContext,"")
            if(root.reachable()):
                start = time.time()
                initPuzzleList = []
                initPuzzleList.append(root)
                print("\nCOUNTING....")
                count, solution = BranchnBound(initPuzzleList)
                end = time.time()
                print(f"SOLUTION : {solution}")
                print(f"TOTAL ACCESS : {count}")
                print(f"TIME EXECUTION : {end-start} s")
            else:
                print ("Not Reachable")
                print("TIME EXECUTION : -")
                print ("TOTAL ACCESS : - ")
        print()
    else:
        break


                
        