## AirBnB clone Project

[AirBnB_clone](https://github.com/Jo40000/AirBnB_clone.git)

---
# Table of Contents
---
* About
* Getting Started
* Deployment
* Usage
* Built Using
* Contributing
* Authors
* Acknowledgement

# About
---
This is a Airbnb clone projects that will be build with the aim to learn and apply concepts of high level programming and software engineering in general

# Getting Started
---

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes 

**prerequisites**

python3

**Installing**

Clone this repository

'https://github.com/Jo40000/AirBnB_clone.git
cd AirBnB_clone
./console.py'

#Running the tests
---
This project uses the python unittest model for automated tests 

**Run all unit tests**
 
'python3 -m unit tests'

**Run a test from a specific file**

'python3 -m unittest tests/tespytestt_models/test_base_model.py'

# Usage
---

you can run the shell (in an interactive or non-interactive model) to manipulate your models.you can start it from running the console.py file:

'$ ./console.py'

The following commands are supported:

**create:**

Create a new instance of BaseModel, saves it (to the file) and prints the id. Ex:

'$ create BaseModel'

**Show:**
Prints the string representation of an instance based on the class name and id. Ex:

'$ show BaseModel 1234-1234-1234.'

**destroy:**

Deletes an instance based on the class name and id (save the change into the JSON file). Ex:

'$ destroy BaseModel 1234-1234-1234.'

**all**

Prints all string representation of all instances based or not on the class name. Example to show al instances

'$ all'

Example to show all instances of BaseModel only

'$ all BaseModel'

**update:**

Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex:

'$ update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"'

**quit:**

Quit the shell

# Built Using
---

* Python - Programming language

# Authors

* @jo40000
