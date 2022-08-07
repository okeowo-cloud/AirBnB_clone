# AirBnB Clone - The Console
The console is the first segment of the AirBnB project that will collectively cover fundamental concepts of higher level programming.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or new Place)
* Retrieve an object from a file, a database etc ...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Contents

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3(version 3.8.5)

## Installation
* Clone this repository: `git clone
"https://github.com/okeowo-cloud/AirBnB_clone.git"`
* Access AirBnB directory: `cd AirBnB_clone`
* Run hbnb (interactively): `./console.py` and enter command
* Run hbnb (non-interactively): `echo "help" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter.
List of commands this console currently supports:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

#### `models/` directory contains classes used for this project
[base_model.py](base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from BaseModel:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user/py)

#### `models/engine` directory contains FileStorage class that handles JSON serialization and deserialization :
[filestorage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` - deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains TestBaseModel class:
* `def test_instantiation(self)` - Test that instantiation of BaseModel works
* `def test_datetime_attr` - Tests that BaseModel instances has different datetime objects when updated
* `def test-uuid` - Test that id is a valid uuid
* `def test_to_dict` - Tests conversion of object attributes to dictionary for json
* `def test_to_dict_values` - Tests that values in dict returned from to_dict are correct
* `def test_str` - Test that the str methods have correct output

## Authors
Tunde Okeowo - [Github](https://github.com/okeowo-cloud) <br/>
Sharon Mboya - [Github](https://github.com/AtienoMboya)

## License
Public Domain. No copywrite protection
