# Contact Book (Python)

The Contact Book (Python) is a simple, zero-dependency Python application designed to help users manage their contacts efficiently. It allows users to add, update, delete, search, and view contact information.

> [!NOTE]
> This project is part of a leveling course in Programming Logic at [FIAP](https://github.com/fiap). The course aims to introduce foundational concepts and skills in programming, which are applied in this project. This application serves as a practical exercise to reinforce learning outcomes related to basic data management and programming.

## Goals

- **Provide a simple interface for managing contacts**
- **Support essential CRUD operations: Create, Read, Update, and Delete**
- **Enable searching for contacts by name, phone, or email**

## Scope

This project includes the following features:

- **Add new contacts**: Input contact details such as name, phone number, and email.
- **Update existing contacts**: Modify the details of an existing contact.
- **Delete contacts**: Remove contacts from the list.
- **View all contacts**: Display a list of all stored contacts.
- **Search for a contact**: Locate a contact by name, phone number, or email address.
- **Save contacts**: Store and retrieve contacts from a JSON file, ensuring data persistence between application runs.

The project does not include:

- **Data validation**: There is no validation for names, phone numbers, or email addresses. Ensure input correctness manually.
- **Navigation handling**: This application does not include advanced navigation or routing features.

## User Guide

### Requirements

To use this project effectively, you need:

- **Python 3.x**: Ensure Python 3 is installed on your system.

### Installation

To install and run the Contact Book application, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/luisfuturist/exercise-contact-book-py.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd exercise-contact-book-py
    ```
3. **(Optional) Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

### Usage

To start the Contact Book application, run the following command:

```sh
python main.py
```

Follow the on-screen prompts to manage your contacts. The application will automatically save changes to a `contacts.json` file, which will be loaded the next time you start the application.

### Additional Information

- **Troubleshooting**: For common issues, check the `README.md` file or contact a project maintainer.
