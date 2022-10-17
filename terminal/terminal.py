from os import getcwd, path, remove, listdir


class Terminal:
    def __init__(self):
        self.current_path = getcwd()
        
    def pwd(self):
        print(self.current_path)
    
    def cat(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    print(line)
        except OSError as err:
            print(f"cat: {err.filename}: {err.strerror}")
            
            

    def cd(self, where):
        try:
            new_path = path.join(self.current_path, where)
            if (not path.exists(new_path)):
                raise FileNotFoundError(f"cd: no such file or a directory: {where}")
            
            self.current_path = path.join(self.current_path, where)
        except FileNotFoundError as err:
            print(err)
    
    def touch(self, file_name):
        try:
            with open(path.join(self.current_path, file_name), "w") as file:
                pass
        except OSError as err:
            print(err)
            
    def rm(self, file_name):
        try:
            remove(path.join(self.current_path, file_name))
        except OSError as err:
            print(f"rm: cannot remove '{file_name}': {err.strerror}")
        
    def ls(self):
        print(*list(filter(lambda s: not s.startswith('.'), listdir(self.current_path))))