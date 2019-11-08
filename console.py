#!/usr/bin/python3
""" Console interpreter for the AirBnB clone """

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ commands for the interpreter to execute """
    prompt = "(hbnb) "

    def do_create(self, line):
        """ creates a new instance of base model """
        try:
            if line == "":
                raise SyntaxError
            new_base = eval("{}()".format(line))
            new_base.save()
            print(new_base.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """ exits the program using quit """
        raise SystemExit

    def help_quit(self):
        """ quit usage """
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """ exits the program using EOF """
        return True

    def help_EOF(self):
        """ EOF usage """
        print("EOF command (Ctrl-D) to exit the program\n")

    def emptyline(self):
        """ executes nothing when entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
