import os
INIT_FILES = ["initStages.msc", "initEvilStages.msc"]

ADMINS = [
    "jasmine476",
    "andrewforreal"
]

MODS = [
    "kittycatelite",
    "egabbac",
    "zhar",
    "facecat1"
]

GREENS = [
    "goomyii",
    "MeddleLyn",
    "hybyrn",
    "ssteppy",
    "JM4s",
    "rypho_",
    "lefty³",
    "noobgamerz",
    "JK_Extreme",
    "Solawr",
    "natcrackers",
    "Heeshh",
    "AgentOtter",
    "Xanthous7",
    "boger704",
    "SobbingGhost"
]
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

def promptStageName(y):
    os.system("cls||clear")
    print(f"Entering name information for the stage at y = {y}")
    print("Please include color codes or other flair.")
    print()

    name = input(f"Enter the name of the stage at y = {y}: ")

    return name

def getPlayerNameWithCode(name):
    if name in ADMINS:
        return "&6" + name

    if name in MODS:
        return "&2" + name

    if name in GREENS:
        return "&a" + name

    return ""

def getCreatorList(player_names):
    if len(player_names) == 1:
        return getPlayerNameWithCode(player_names[0])

    creator_list = ""
    for i, player_name in enumerate(player_names):
        if i == len(player_names) - 1:
            temp = getPlayerNameWithCode(player_name)
            if temp == "":
                return ""
            creator_list += "and " + temp
        elif i == len(player_names) - 2:
            temp = getPlayerNameWithCode(player_name)
            if temp == "":
                return ""
            creator_list += temp + " "
        else:
            temp = getPlayerNameWithCode(player_name)
            if temp == "":
                return ""
            creator_list += temp + ", "
    return creator_list

# TODO multiple names
def promptCreatorNames(y):
    awaiting_input = True
    os.system("cls||clear")
    print(f"Entering name information for the creators of the stage at y = {y}")
    print("Do not enter custom color codes or other flair. Name colors are done automatically.")
    print("Enter names in the order you want them seperated with spaces. (Example: 'Chillers RyGamer1 Heeshh')")
    print()
    while awaiting_input:
        player_names = [
            x for x in input(f"Enter the names of the creators at y = {y}: ").split()
        ]

        creator_list = getCreatorList(player_names)
        if creator_list != "":
            awaiting_input = False
        else:
            print("Name mispelled or not in script player list. Please check again or update the list.")
            
    return creator_list 

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
            append_index = appendStackToFilePrompt()
            if append_index == -1:
                clean_exit(0)

            generateStackInitFile(INIT_FILES[append_index])
            print("Completed.")
            clean_exit(0)

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

if (__name__ == "__main__"):
    main()
