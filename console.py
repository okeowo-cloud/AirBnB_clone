#!/usr/bin/python3
"""console module for entry into the command interpreter"""
import cmd
import sys
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    class_dict = {
            "BaseModel": BaseModel,
            "User": User
            }

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
        """
        Create a new instance of a class, saves it to Json file
        Usage: create <class name>
        """
        arg_list = shlex.split(arg)
        if len(arg_list) < 1:
            print("** class name missing **")
            return

        if (arg_list[0] in HBNBCommand.class_dict.keys()):
            obj = HBNBCommand.class_dict[arg_list[0]]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ 
        Prints all string representation of all instances
        based or not on the class name.
        Ex: all BaseModel or all

        Usage:(1) all
              (2) all <class name>
        """
        storage.reload()
        obj_list = []
        objects = storage.all()
        if arg == "":
            for key, value in objects.items():
                obj_list.append(str(value))
            print(json.dumps(obj_list))
            return
        arg_list = shlex.split(arg)
        if (arg_list[0] not in HBNBCommand.class_dict.keys()):
            print("** class doesn't exist **")
            return
        for key, value in objects.items():
            if arg_list[0] in key:
                obj_list.append(str(value))
            print(json.dumps(obj_list))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com

        update <class name> <id> <attribute name> "<attribute value>"

        """
        arg_list = shlex.split(arg)
        arg_len = len(arg_list)
        if arg_len < 1:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return
        if arg_len == 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = arg_list[0] + "." + arg_list[1]
        try:
            objects[key]
        except KeyError:
            print("** no instance found **")
            return
        if arg_len == 2:
            print("** attribute name missing **")
            return
        if arg_len == 3:
            print("** value missing **")
            return
        obj_dict = objects[key].__dict__
        if arg_list[2] in obj_dict.keys():
            obj_dict[arg_list[2]] = type(obj_dict[arg_list[2]])(arg_list[3])
        else:
            obj_dict[arg_list[2]] = arg_list[3]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
