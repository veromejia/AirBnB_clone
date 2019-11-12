# AirBnB_clone

---
##Description
The Airbnb clone is a copy of the Airbnb. Only some features will be implemented, The goal of the project is to deploy on our own server a simple copy of the AirBnB website.

## The command interpreter will be used in subsequent AirBnb projects to manage objects and clases. in our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
  
##Usage
The console can be run in interactive and non-interactive mode.

##Non-Interactive Mode

To run a command in non-interactive mode, echo the desired command and pipe it into the console like so:
```
echo "<command>" | ./console.py
```
## Examples
```
echo "create BaseModel" | ./console.py
```

```
echo "show BaseModel id-here" | ./console.py
```

### Interactive Mode

To run in interactive mode:

```
./console.py
```
Then type the desired commands inside of the program.

##Examples

```
(hbnb) create BaseModel
```

```
(hbnhb) show BaseModel id-here"
```

## Commands

Command | Description
--- | ---
`help` | display the documented command
`quit` | Exit the program
`EOF` | Exit the program
`create <class>` | Create an instance of a class
`show <class> <id>` | Print the string representation of an instance of a class
`destroy <class> <id>` | Delete instance of a class
`all` | Print all string representations of all instances
`updated` | Updates an instance based on the class name and id by adding or updating attribute

