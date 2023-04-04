from enum import IntEnum, auto
from typing import List


class EntityType(IntEnum):
    Directory = auto()
    File = auto()

class Entry:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Directory(Entry):
    def __init__(self, name):
        super().__init__(name, EntityType.Directory)
        self.entries = {}

    def resolve(self, path):
        if not path:
            return self
        entry = self.entries[path[0]]
        entry.resolve(path[1:])

class File(Entry):
    # magic or dunder-method
    # Double UNDERscore method
    def __init__(self, name):
        super().__init__(name, EntityType.File)




commands = {}

def command(func):
    commands[func.__name__] = func
    return func

class Shell:
    def __init__(self):
        self.vfs = Directory('/')
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            try:
                line = input('> ')
                cmd = line.split()
                command_itself = cmd[0]
                func = commands[command_itself]
                func(self, *cmd[1:])
                # f([3, 4]) => f(arg0 = [3, 4])
                # f(*[3, 4]) => f(arg0 = 3, arg1 = 4)
                # func(cmd..)
            except KeyboardInterrupt:
                self.running = False

    def split_path(self, path):
        path = path.split('/')
        # bool([]) = False
        # bool([3, 3]) = True
        # bool('') = False
        # bool('a') = True
        if not path[0]:
            path.pop(0)
        if not path[-1]:
            path.pop(-1)
        return path

    # ls = command(ls)
    @command
    def exit(self):
        self.running = False

    @command
    def ls(self, path: str):
        path = self.split_path(path)
        # 1. resolve entry
        entry = self.vfs.resolve(path)
        # 2. is a dir
        if entry.type != EntityType.Directory:
            raise Exception()
        # 3. iter over them print
        print()

    @command
    def mkdir(self, args):
        pass

    @command
    def mkfile(self, args):
        pass

    @command
    def rm(self, args):
        pass


shell = Shell()
shell.run()

# mkdir path
# mkfile path
# ls path
# exit
# def parse_int(a):
#     try:
#         x = int(a)
#     except ValueError as ex:
#         print(ex)
#         return None
#
#     return x
# print(parse_int('a'))