# UniCompare - University Records Comparison System

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

1. **Add Record:** Enables users to add new records, including the course name and price.

2. **Display Records (Sorted by Price):** Presents all existing records, sorted by price in ascending order.

3. **Update Record:** Allows the update of an existing record by providing the record's ID and the new data.

4. **Delete Record:** Permits the deletion of an existing record based on the provided ID.

## How to Run

Ensure you have Python installed on your system. Clone the repository and execute the `main.py` Python script in the command prompt.

```bash
python main.py
```

Follow the instructions in the prompt to interact with the system.

## Variables and Types:

- `DATABASE_FILE`: String. File name to store records.
- `data`: List of strings. Stores the records.
- `record`, `new_record`: String. New records to be created or updated.
- `record_id`: Integer. ID of the record to be updated or deleted.
- `record_data`: List of strings. Division of the record into name and price.

## Functions:

- `create_record(data: List[str], record: str) -> None`: Creates a new record based on the input.
- `read_records(data: List[str]) -> None`: Displays all records sorted by price.
- `update_record(data: List[str], record_id: int, new_record: str) -> None`: Updates an existing record.
- `delete_record(data: List[str], record_id: int) -> None`: Deletes an existing record.
- `save_to_file(data: List[str]) -> None`: Saves the records to a file.
- `load_from_file() -> List[str]`: Loads the records from a file.

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
- [ ] Do interviews
- [x] Fix database.txt empty line error
- [x] Fix database.txt Y variable error
- [x] Add more data to database.txt
- [ ] fix "ã" error.
