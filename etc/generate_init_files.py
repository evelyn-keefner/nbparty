import system

INITSTAGESFILENAME = "initStages.msc"

def openFileToWriteErrorChecked(filename:str) -> TextIOWrapper:
    try: 
        f = open(filename, "w")
    except:
        print(f"{filename} failed to open. Exiting...")
        exit(1)
    return f

def openFileToAppendErrorChecked(filename:str) -> TextIOWrapper:
    try: 
        f = open(filename, "a")
    except:
        print(f"{filename} failed to open. Exiting...")
        exit(1)
    return f

def initialPrompt() -> int:
    awaiting_input = True;
    os.system('cls||clear')
    print("[nbparty]")
    print("\t1. Append a stack of stages to init file")
    print("\t2. Delete an init file")

    while (awaiting_input):
        choice = input("Enter selection: (as a number)")
        try:
            choice = int(choice)

            if (choice != 1 && choice != 2):
                raise Exception()

            awaiting_input = False
        except:
            print("Incorrect input. Please enter another number.")

    return choice


def main():
    f = openFileToWriteErrorChecked(INITSTAGESFILENAME)

    match initialPrompt():
        case 1:
            
        case 2:
    # TODO 
    # - 1. Append to init file from stage stack
    #       * prompts user for which file
    #           - creates header if not there already
    #           - prompts for # of stages in stack
    #           - prompts for coordinates of bottom stack 
    #           - prompts for # of blocks of air in between each stack
    #               - for every stage line, prompts text style, then color, then either name or authors. User can click enter to go forward and type things themselves
    # - 2. Delete init file
    #       * prompts user for which file
    # - 

if (__name__ == "__main__"):
    main()
