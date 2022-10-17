from terminal.terminal import Terminal

def main():
    instance = Terminal()
    
    while True:
        command, *name = input().split()
        if command == "cd":
            instance.cd(*name)
        elif command == "touch":
            instance.touch(*name)
        elif command == "rm":
            instance.rm(*name)
        elif command == "pwd":
            instance.pwd()
        elif command == "cat":
            instance.cat(*name)
        elif command == "ls":
            instance.ls()


if __name__ == "__main__":
    main()