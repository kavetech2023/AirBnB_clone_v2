<h1>HBNB - The Console</h1>
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

<h3>General Use</h3>

<b>1. Commands</b>
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands:

* all - Shows all objects the program has access to, or all objects of a given class

* count - Return number of object instances by class

* show - Shows an object based on class and UUID

* destroy - Destroys an object based on class and UUID

* update - Updates existing attributes an object based on class name and UUID

