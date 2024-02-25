# Simple CRUD Todo List
## Overview
I implement simple todo list with CRUD operation.
You can add new item, update and delete it.
This project aims to understand what CRUD is and how to implement it in Flask.
I focus on backend in this project so ignore weird form templates

## How to use
1. Clone this repo
2. Create and activate the virtual environment: ```python -m venv venv```
3. Install dependencies: ```pip install -r requirements.txt```
4. Initialize the database: ```flask --app todo init-db```
   After command executed, you can find the database ```instsance/todo.sqlite```
5. Run ```flask --app todo run``` to start the app
6. Append ```/todo``` in the URL (I'll fix this later)
7. Enjoy