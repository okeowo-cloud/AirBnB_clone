#!/usr/bin/python3
"""console module for entry into the command interpreter"""
import cmd
import sys
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Ensure empty line does nothing"""
        pass

    def do_EOF(self, arg):
        """EOF to exit program"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to Json file"""
        class_dict = {
                "BaseModel": BaseModel
                }
        arg_list = shlex.split(arg)
        if len(arg_list) < 1:
            print("** class name missing **")
            return

        if (arg_list[0] in class_dict.keys()):
            obj = class_dict[arg_list[0]]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
