import os
from colorama import Fore, Back, Style
INIT_FILES = ["initStages.msc", "initEvilStages.msc"]

def clean_exit(code):
    print("Exiting...")
    exit(code)

def openFileToReadErrorChecked(filename:str):
    try:
        f = open(filename, "r")
    except:
        print(f"{filename} failed to open. Exiting...")
        exit(1)
    return f

def openFileToWriteErrorChecked(filename:str):
    try:
        f = open(filename, "w")
    except:
        print(f"{filename} failed to open. Exiting...")
        exit(1)
    return f

def openFileToAppendErrorChecked(filename:str):
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
        choice = input("Enter selection: (as a number)\n")
        try:
            choice = int(choice)

            if (choice != 1 and choice != 2):
                raise Exception()

            awaiting_input = False
        except:
            print("Incorrect input. Please enter another number.")

    return choice

def appendStackToFilePrompt() -> int:
    awaiting_input = True;
    os.system('cls||clear')
    print("[nbparty]")
    for i, init_file in enumerate(INIT_FILES):
        print(f"{i}: {init_file}")

    while (awaiting_input):
        choice = input("Enter selection: (as a number. enter -1 to exit)\n")
        try:
            choice = int(choice)
            
            if choice == -1:
                return choice

            INIT_FILES[choice]

            awaiting_input = False
        except:
            print("Incorrect input. Please enter another number.")

    return choice

def deleteInitFilePrompt() -> int:
    awaiting_input = True
    os.system('cls||clear')
    print("[nbparty]")
    for i, init_file in enumerate(INIT_FILES):
        print(f"{i}: {init_file}")

    while (awaiting_input):
        choice = input("Enter selection: (as a number. enter -1 to exit)\n")
        try:
            choice = int(choice)

            if choice == -1:
                return choice

            INIT_FILES[choice]

            awaiting_input = False
        except:
            print("Incorrect input. Please enter another number.")

    return choice

def validateStageData(stage_data) -> bool:
    x1, y1, z1, x2, y2, z2, gap = stage_data

    # ensure stage is 32x32
    if (x2 - x1) + 1 != 32:
        return False

    if (z2 - z1) + 1 != 32:
        return False

    # ensure gap # makes senses for y values
    total_height = y2 - y1 + 1
    if (total_height % (gap + 1) != 1):
        return False

    return True

# [x1, y1, z1, x2, y2, z2, gap]
def promptStackInitFile() -> []:
    stage_data = []
    prompts = [
        "x1",
        "y1",
        "z1",
        "x2",
        "y2",
        "z2",
        "gap"
    ]

    for prompt in prompts:
        os.system('cls||clear')
        print("[nbparty]")
        print("Enter stage information.")
        print("x1, y1 and z1 is the NW corner of the lowest stage.")
        print("x2, y2, and z2 is the SE corner of the highest stage.")
        print("gap is the # of blocks of air inbetween every stage.")
        print("Ensure you are writing your block coordinates, and not your player coordinates.")

        awaiting_input = True

        while awaiting_input:
            print()
            data = input(f"Enter the value for {prompt}: ")

            try:
                data = int(data)

                stage_data.append(data)
                awaiting_input = False
            except:
                print("Invalid input. Please enter a number.")

    if not validateStageData(stage_data):
        print("Double check data. Coordinates either don't imply a 32x32 sized stage or gap # for given y values doesn't make sense.")
        clean_exit(0)

    print("Stage data: ")
    for i, p in enumerate(prompts):
        print(f"{p} = {stage_data[i]}")

    return stage_data

def writeHeader(filename):
    f = openFileToWriteErrorChecked(filename)
    f.write("# initStages()\n")
    f.write("@fast\n")
    f.write("\n")
    f.write("@var nbparty::stages = nbparty::Stage[]\n")
    f.write("\n")
    f.close()

def getStyleCode():
    print("Enter the character corresponding to text style. (Only first character will count)")
    print("k: Obfuscated")
    print("l: Bold")
    print("m: Strikethrough")
    print("n: Underline")
    print("o: Italic")
    print("Enter r or nothing for default text style.")
    print()
    style = input("Enter character here: ")

    try:
        if style[0] == "k":
            style = "&k"
        elif style[0] == "l":
            style = "&l"
        elif style[0] == "m":
            style = "&m"
        elif style[0] == "n":
            style = "&n"
        elif style[0] == "o":
            style = "&o"
        else:
            # no if statement for r, same as default
            style = ""
    except:
        style = ""

    return style

def getColorCode():
    print("Enter the character corresponding to text color. (Only first character will count)")
    print("0: Black")
    print(Back.BLUE + "1: Dark Blue")
    print(Back.GREEN + "2: Dark Green")
    print(Back.CYAN + "3: Dark Aqua")
    print(Back.RED + "4: Dark Red")
    print(Back.MAGENTA + "5: Dark Purple")
    print(Fore.BLACK + Back.YELLOW + "6: Gold")
    print(Fore.WHITE + Back.LIGHTBLACK_EX + "7: Gray")
    print(Back.LIGHTBLACK_EX + "8: Dark Gray")
    print(Back.LIGHTBLUE_EX + "9: Blue")
    print(Fore.BLACK + Back.LIGHTGREEN_EX + "a: Green")
    print(Back.LIGHTCYAN_EX + "b: Aqua")
    print(Fore.WHITE + Back.LIGHTRED_EX + "c: Red")
    print(Back.LIGHTMAGENTA_EX + "d: Light Purple")
    print(Fore.BLACK + Back.LIGHTYELLOW_EX + "e: Yellow")
    print(Style.RESET_ALL + "Enter f or nothing for default white text color.")
    print()
    color = input("Enter character here: ")

    try:
        if color[0] == "0":
            color = "&0"
        elif color[0] == "1":
            color = "&1"
        elif color[0] == "2":
            color = "&2"
        elif color[0] == "3":
            color = "&3"
        elif color[0] == "4":
            color = "&4"
        elif color[0] == "5":
            color = "&5"
        elif color[0] == "6":
            color = "&6"
        elif color[0] == "7":
            color = "&7"
        elif color[0] == "8":
            color = "&8"
        elif color[0] == "9":
            color = "&9"
        elif color[0] == "a":
            color = "&a"
        elif color[0] == "b":
            color = "&b"
        elif color[0] == "c":
            color = "&c"
        elif color[0] == "d":
            color = "&d"
        elif color[0] == "e":
            color = "&e"
        else:
            # no if statement for r, same as default
            color = ""
    except:
        color = ""

    return color

def promptStageName(y):

    print(f"Entering name information for the stage at y = {y}")
    
    print()
    print("Which text style do you want for stage name?")
    style_code = getStyleCode()

    print()
    print("Which color do you want for stage name?")
    color_code = getColorCode()

    print()
    name = input("Enter the name of the stage at y = {y}: ")

    return style_code + color_code + name

# TODO Make creator names just the colors of their ranks.
def promptCreatorNames(y):
    print(f"Entering name information for the creators of the stage at y = {y}")
        
    print()
    print("Which text style do you want for stage creators names?")
    style_code = getStyleCode()

    print()
    print("Which color do you want for stage creator names?")
    color_code = getColorCode()

    print()
    name = input("Enter the names of the creators at y = {y}: ")

    return style_code + color_code + name

def appendStages(filename, stage_data):
    f = openFileToAppendErrorChecked(filename)
    x1, y1, z1, x2, y2, z2, gap = stage_data

    for y in range(y1, y2 + 1, gap + 1):
        stage_name = promptStageName(y)
        creator_names = promptCreatorNames(y)

        f.write(f"@var nbparty::stages.append(nbparty::Stage({x1}, {z1}, {x2}, {z2}, {y}, \"{stage_name}\", \"{creator_names}\"))\n")

def generateStackInitFile(filename):
    stage_data = promptStackInitFile()

    try:
        f_check = open(filename)
        comment = f_check.readline()
        f_check.close()

        # check if the header needs to be added or if stages can just be appended
        if (comment != "# initStages()\n"):
            print(f"{filename} header broken. Creating new {filename}")
            writeHeader(filename)
    except:
        print(f"Couldn't open {filename}. Creating new {filename}")
        writeHeader(filename)

    print(f"Appending new stages to end of {filename}")
    appendStages(filename, stage_data)


def main():
    match initialPrompt():
        # append to stack
        case 1:
            append_index = appendStackToFilePrompt();
            if append_index == -1:
                clean_exit(0)

            generateStackInitFile(INIT_FILES[append_index])

        # delete file
        case 2:
            remove_index = deleteInitFilePrompt()
            if remove_index == -1:
                clean_exit(0)
            try:
                os.remove(INIT_FILES[remove_index])
            except:
                print(f"{INIT_FILES[remove_index]} not found.")
                clean_exit(0)

            print(f"Deleted {INIT_FILES[remove_index]}.")
            clean_exit(0)
        case _:
            print("initialPrompt returned a bad value.")
            clean_exit(1)
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
