# OOP Todo Application

[cite_start]A Command Line Interface (CLI) application built with Python to manage tasks[cite: 4].

## Features
* [cite_start]**Add Todo**: Create tasks with titles[cite: 16, 18].
* [cite_start]**View Todos**: List task ID, title, and status[cite: 19, 21].
* [cite_start]**Update Todo**: Change title or completion status[cite: 22, 23, 24].
* [cite_start]**Delete Todo**: Remove tasks by ID[cite: 25, 27].
* [cite_start]**Persistence**: Data is saved to `todos.json`[cite: 29, 30].

## How to Run
1. Run the script: `python main.py`
2. Follow the on-screen menu instructions.

## Data Handling (Objects & JSON)
[cite_start]This application uses Object-Oriented Programming (OOP) to manage tasks. 
* [cite_start]**Serialization**: Task objects are converted into dictionaries using the `to_dict()` method to be saved as JSON[cite: 12].
* [cite_start]**Deserialization**: When the app starts, JSON data is parsed and passed into the `Task.from_dict()` static method to recreate live Task objects[cite: 13].
