# To-Do Flask App with MongoDB

This is a simple and functional To-Do application built using the Flask framework with MongoDB as the backend database. The app provides a user-friendly interface to manage tasks efficiently and supports basic CRUD operations (Create, Read, Update, Delete).

## Features

1. **Add Tasks**  
   - Users can add new tasks to their to-do list with a description.

2. **View Tasks**  
   - All tasks are displayed, showing their current status (completed or not).

3. **Edit Tasks**  
   - Modify the description of an existing task.

4. **Mark Tasks as Complete**  
   - Update the status of a task to "completed."

5. **Delete Tasks**  
   - Remove tasks from the list permanently.

---

## Technologies Used

- **Frontend**: HTML, CSS, and Flask templates (Jinja2)
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Forms**: Flask-WTF for form handling
- **Dependencies**: Flask-PyMongo for MongoDB integration

---

## Installation

### Prerequisites
- Python 3.x installed
- MongoDB installed and running locally or accessible via a remote server
- `pip` for Python package management

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**:
   - Ensure your MongoDB server is running.
   - Configure your MongoDB connection string in the `config.py` or `.env` file as needed:
     ```
     MONGO_URI=mongodb://localhost:27017/todo_db
     ```

5. **Run the Application**:
   ```bash
   python run.py
   ```

6. **Access the App**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. **Add Tasks**:
   - Navigate to the home page and use the "Add Task" form to create a new task.

2. **View Tasks**:
   - The list of tasks is displayed on the home page with their status.

3. **Edit Tasks**:
   - Click the "Edit" button next to a task, modify its description, and save changes.

4. **Mark Tasks as Complete**:
   - Click the "Mark as Complete" button to update the task's status.

5. **Delete Tasks**:
   - Use the "Delete" button to permanently remove a task.

---


## Future Enhancements

- Add user authentication to make tasks private to individual users.
- Implement due dates and reminders for tasks.
- Add search and filter functionality for better task management.
- Create a mobile-friendly UI using responsive design.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and use it for your projects.

---

Enjoy managing your tasks with the Flask To-Do app! 😊


## Project Structure

```
project_root_dir
│
|
|
|__ application
|    |
|    |__ templates
|    |__ __init__.py
|    |__ routes.py
|    |__ forms.py
|
|
|__ venv
|
|
|
|__ README.md
|
|
|__ run.py
```
