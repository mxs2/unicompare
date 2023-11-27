## UniCompare - Our future is incomparable

<p align="center">
<a href=""><img src="./resources/logo.png" alt="Unicompare Logo." width=350px"></a>
</p>

<p align="center">
<a href="docs/README_EN.md">English</a> | <a href="../README.md">Portuguese</a>
</p>

## Description

UniCompare is a project developed as part of the Information Management course at Cesar School. This system allows users to perform basic CRUD (Create, Read, Update, Delete) operations on university records, such as course names and prices.

## Flowchart

<p align="center" style="border: 1px solid #333; background-color: white;">
  <a href="">
    <img src="./resources/flowchart.svg" alt="Unicompare Flowchart">
  </a>
</p>

## Features

UniCompare offers the following features:

1. **Add Record:** Allows users to add new records, including course names and prices.
2. **Display Records (Ordered by Price):** Shows all existing records, ordered by price in ascending order.
3. **Update Record:** Allows updating an existing record by providing the record's ID and new data.
4. **Delete Record:** Allows deleting an existing record based on the provided ID.

5. **Evaluate Institution:** Allows evaluating an existing institution based on the provided ID.

## How to Run

Make sure you have Python installed on your system. Clone the repository and run the Python script `main.py` in the command prompt.

```bash
python main.py
```

Follow the instructions in the prompt to interact with the system.

## Variables and Types:

- `DATABASE_FILE`: String. Name of the database file (using SQLite3) to store records.
- `data`: List of strings. Stores records loaded into memory during execution.
- `record`, `new_record`: String. New records to be created or updated in the database.
- `record_id`: Integer. ID of the record to be updated or deleted in the database.
- `record_data`: List of strings. Division of the record into name and price.

## Functions:

- `clear_screen() -> None`: Clears the screen for different operating systems.
- `read_records_from_db() -> List[str]`: Reads records from the database and returns a list of records.
- `print_records(records: List[str]) -> None`: Displays formatted records on the screen.
- `evaluate_institution() -> None`: Evaluates an institution present in the database.
- `add_institution() -> None`: Adds a new institution to the database.
- `delete_institution() -> None`: Deletes an institution from the database.
- `print_ascii_pattern() -> None`: Prints the UniCompare ASCII pattern.
- `main() -> None`: Main function of the program controlling the execution flow.

The `DATABASE_FILE` is used as an SQLite3 database file to store and manage UniCompare system records. This allows efficient data manipulation and queries using the Python `sqlite3` library.

## Contributions

Contributions are welcome! If you encounter issues or have suggestions for improvement, please open an issue in this repository.

## Developers

- mxs2@cesar.school
- vrln2@cesar.school
- jhrbfl@cesar.school
- cfcl@cesar.school
- bag@cesar.school
- tmf2@cesar.school
- cjam@cesar.school

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Backlog

- [x] Do first prototype tests
- [x] Do interviews
- [x] Fix database.txt empty line error
- [x] Fix database.txt Y variable error
- [x] Add more data to database.txt
- [x] fix "UTF-8" error.
- [x] Add evaluation function.
- [x] Use a database instead of a text file.
