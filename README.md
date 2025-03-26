# Desktop Application

This is a simple **Tkinter-based desktop application** that performs **CRUD (Create, Read, Update, Delete)** operations on a MySQL database.

## Features
- **Insert Data**: Add new records to the database.
- **Search Data**: Retrieve and display details based on the ID.
- **Update Data**: Modify existing records.
- **Delete Data**: Remove records from the database.

## Technologies Used
- **Python** (Tkinter for GUI)
- **MySQL** (Database for storing records)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **Python** (>=3.7)
- **MySQL Server**
- Required Python libraries:
  ```sh
  pip install mysql-connector-python
  ```

### Database Setup
1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE tkinter;
   ```
2. Switch to the database:
   ```sql
   USE tkinter;
   ```
3. Create the table:
   ```sql
   CREATE TABLE class (
       id INT AUTO_INCREMENT PRIMARY KEY,
       fname VARCHAR(50),
       lname VARCHAR(50),
       email VARCHAR(100),
       mobile VARCHAR(15)
   );
   ```

### Running the Application
1. Clone this repository:
   ```sh
   git clone https://github.com/khushbunaz/Desktop-Application.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Desktop-Application
   ```
3. Run the script:
   ```sh
   python app.py
   ```

## Future Enhancements
- Add a **search result table** instead of filling entry fields.
- Improve the UI using **Tkinter's ttk** module.
- Implement **input validation** for email and mobile number formats.

## Author
**Khushbunaz Dalal**

---

Feel free to contribute and improve this project!

