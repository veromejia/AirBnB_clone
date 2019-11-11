#!/usr/bin/python3
""" Console interpreter for the AirBnB clone """

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ commands for the interpreter to execute """
    prompt = "(hbnb) "
    classes = ["BaseModel"]

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

    def help_create(self):
        print("Creates a new instance of a given class\n")

    def do_show(self, line):
        """ prints string representation of an instance """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def help_show(self):
        """ show usage """
        print("Prints the string of an instance based on the class and id\n")

    def do_destroy(self, line):
        """ deletes an instances based on class and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def help_destroy(self):
        """ destroy usage """
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, line):
        """ print all string representation of instances """
        if line != "":
            args = line.split(" ")
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            class_insts = [str(o) for k, o in storage.all().items()
                     if type(o).__name__ == args[0]]
            print(class_insts)
        else:
            all_insts = [str(o) for k, o in storage.all().items()]
            print(all_insts)

    def help_all(self):
        """ all usage """
        print("Prints all str instances based or not on the class name\n")

    def do_update(self, line):
        """ updates an instance based on class and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
        if len(args) < 4:
            print("** value missing **")
        val = objs[key]
        try:
            attr = getattr(val, args[2])
            setattr(val, args[2], type(attr)(args[3]))
        except:
            setattr(val, args[2], args[3])
        storage.save()

    def help_update(self):
        """ update usage """
        print("update <class name> <id> <attribute name> <attribute value>\n")

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
