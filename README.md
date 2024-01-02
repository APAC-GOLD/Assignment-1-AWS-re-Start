- [Rules:](#rules)
- [Part 1 (25 marks total)](#part-1-25-marks-total)
  - [Part 1.1. Network (12/25 marks)](#part-11-network-1225-marks)
  - [Part 1.2. Git \& software development (6/25 marks)](#part-12-git--software-development-625-marks)
  - [Part 1.3. Cryptography (7/25 marks)](#part-13-cryptography-725-marks)
- [Part 2 (25 marks total)](#part-2-25-marks-total)
  - [Part 2.1. List (3/25 marks)](#part-21-list-325-marks)
  - [Part 2.2. Dictionaries (3/25 marks)](#part-22-dictionaries-325-marks)
  - [Part 2.3. Flow control (4/25 marks)](#part-23-flow-control-425-marks)
  - [Part 2.4. File handling (4/25 marks)](#part-24-file-handling-425-marks)
  - [Part 2.5. OOP (7/25 marks)](#part-25-oop-725-marks)
  - [Part 2.6. Module (4/25 marks)](#part-26-module-425-marks)
- [Part 3 (30 marks total)](#part-3-30-marks-total)
  - [Part 3.1. POST api (8/25 marks)](#part-31-post-api-825-marks)
  - [Part 3.2. GET all messages api (2/25 marks)](#part-32-get-all-messages-api-225-marks)
  - [Part 3.3. GET single messages api, given a message\_key (3/25 marks)](#part-33-get-single-messages-api-given-a-message_key-325-marks)
  - [Part 3.4. PATCH single messages api, give message\_key and new\_message (4/25 marks)](#part-34-patch-single-messages-api-give-message_key-and-new_message-425-marks)
  - [Part 3.5. DELETE single message given message\_key (3/25 marks)](#part-35-delete-single-message-given-message_key-325-marks)
  - [Part 3.6. Unit testing (10/25 marks)](#part-36-unit-testing-1025-marks)
- [Part 4 (20 marks total)](#part-4-20-marks-total)
  - [Part 4.1. POST /owners/ API (3/20 marks)](#part-41-post-owners-api-320-marks)
  - [Part 4.2. GET /owners-full-details/{owner\_id} (3/20 marks)](#part-42-get-owners-full-detailsowner_id-320-marks)
  - [Part 4.3. POST /cars/ API (3/20 marks)](#part-43-post-cars-api-320-marks)
  - [Part 4.4. GET /cars-full-details/{car\_id} API (3/20 marks)](#part-44-get-cars-full-detailscar_id-api-320-marks)
  - [Part 4.5. PATCH /cars/{car\_id} API (3/20 marks)](#part-45-patch-carscar_id-api-320-marks)
  - [Part 4.6. Unit testing (5/20 marks)](#part-46-unit-testing-520-marks)


# Rules:

- Its ok to discuss strategy/solution between each other, just don't copy work
- Only change code where you were asked with "your code here" in terminal art
- Don't change the template code of the assignment (using Git to ensure this)
- Don't make it obvious that you have copied unmodified contents from the AI tools/Stackoverflow
- Don't ask the tutors to give you the answer, though you may ask for hints/high level how
- Feel free to ask the tutors to get you fix an execution time error/environment setup fault
- Feel free let us know during class if you find something is wrong with the assignment questions
- Be reasonable with the tutors' time, so everyone can have a turn at asking them for help

# Part 1 (25 marks total)

## Part 1.1. Network (12/25 marks)

see file `Part_1/1.Network.md`

## Part 1.2. Git & software development (6/25 marks)

see file `Part_1/2.Development.md`

## Part 1.3. Cryptography (7/25 marks)

see file `Part_1/3. Cryptography.md`

# Part 2 (25 marks total)

## Part 2.1. List (3/25 marks)

Assign the list ['a', 'b', 'c', 'd', 'e'] to a variable.
Reverse the list, then insert ‘z’ at index 3, and finally append ‘o’ to the end.

see file `Part_2/1.List.py`

## Part 2.2. Dictionaries (3/25 marks)

Given 2 lists, 1 each for string keys and int values
Convert and return a single dictionary, 100x the int values.

see file `Part_2/1.Dictionaries.py`

## Part 2.3. Flow control (4/25 marks)

Print out a pattern like this programmatically with n
n = the number of star equivalent to how wide the wing is
there is 1 space in between the \* on each line

```
in this case n = 4

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

in this case n = 1
*
* *
*
```

see file `Part_2/3.FlowControl.py`

## Part 2.4. File handling (4/25 marks)

Write a function which reads a file name, eg. `input.txt`, then print out all the lines in the files
Additionally, display the lines in such a way that does not cause line misalignment
Save all the printout into a separate file called `output.txt`

```
1.  ASDHKJAAS
2.  HNHSAFKSK
...
10. ASFASKFDS
...
```

see file `Part_2/4.FileHandling.py`
the file to run test on is `input.txt`

## Part 2.5. OOP (7/25 marks)

Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.

- Raise a custom exception when the salary is lower than 40,000 which is lower than the minimum wage
- Use 'assign_department' method to change the department of an employee.
- Use 'print_employee_details' method to print the details of an employee.
- Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:

```
overtime = hours_worked – 50
overtime amount = (overtime * (salary / 50))
```

```
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
"KING", "E5698", 20000, "RESEARCH"
```

see file `Part_2/5.OOP.py`

## Part 2.6. Module (4/25 marks)

Given file `Part_2/6.ErrorHandling`

Split the file into a module structure such as below.
Ensure that executing the `main.py` file does not incur any runtime error.

```
app
├── classes
│   ├── __init__.py
│   ├── Contract.py
│   ├── Commission.py
│   ├── ContractCommission.py
│   ├── Employee.py
│   ├── HourlyContract.py
│   └── FreelancerContract.py
└── main.py
```

# Part 3 (30 marks total)

Given file `Part_3/main.py`

## Part 3.1. POST api (8/25 marks)

This intends to create a simple message and save it inside a dictionary

Implement the POST /message API with a query parameter taking in str as message:

- (2/8 marks) Save the message content (value) and message id (key) into dictionary `messages`
- (2/8 marks) The key of the dict should be message\_{index}, eg. `message_1`, `message_2`
- (2/8 marks) Automatically increment the index value somehow
- (2/8 marks) Ensure that you can avoid overwriting and existing key when calling this POST API
- If the message is saved successfully, check to status code 200

```python
@app.post("/message")
def create_message(message: str):
    ...
```

## Part 3.2. GET all messages api (2/25 marks)

Return all saved messages, with code 200
If there is no message, return code 404

```python
@app.get("/")
def get_all_messages() -> dict:
    ...
```

## Part 3.3. GET single messages api, given a message_key (3/25 marks)

Get a message content, given a message key, eg. GET /message/message_1
If a key does not exist, return code 404

```python
@app.get("/message/{message_key}")
def get_message(message_key: str) -> str:
    ...
```

## Part 3.4. PATCH single messages api, give message_key and new_message (4/25 marks)

Update message content, given a message key,

- eg. PATCH /message/message_1 and also provide query string variable `message`
- If a message key does not exist, return code 404
- If a message key indeed exist, override, and return the updated value

```python
@app.patch("/message/{message_key}")
def update_message(message_key: str, new_message: str) -> str:
    ...
```

## Part 3.5. DELETE single message given message_key (3/25 marks)

Delete message key and value, given a message_key,

- eg. DELETE /message/message_1
- If a message key does not exist, return code 404
- If a message key indeed exist, delete, and return the message value (similar to pop)

```python
@app.delete("/message/{message_key}")
def delete_message(message_key: str) -> str:
    ...
```

## Part 3.6. Unit testing (10/25 marks)

See file `Part_3/test_main.py`

Perform Unit testing on the API you created and provide some screenshot of the test evidence:

- (2/10 marks) POST api
- (2/10 marks) GET all api
- (2/10 marks) GET by message_key api
- (2/10 marks) PATCH by message_key api
- (2/10 marks) DELETE by messge_key api

You are welcome to provide robust testing of your APIs, considering different edge cases or ways it can fail. For the extra effort spent for testing, **you may earn up to 5 addition marks** (if you really need them). Consider this a "performance bonus", which you will encounter in real life somewhat often. I recommend investing in your test suite after you have completed the assignment though.

# Part 4 (20 marks total)

1. See file `Part_4/main.py`

2. Change directory in your Bash/Unix terminal to `cd Part_4`

3. Activate your virtual environment

![Alt text](image.png)

4. Run `pip install sqlmodel fastapi[all]` while inside your virtual environment

5. Study the existing code carefully

## Part 4.1. POST /owners/ API (3/20 marks)

Implement an API to create `owner`, given the `OwnerCreate` DTO definition as input type

```python
@app.post("/owners/", response_model=OwnerRead)
def create_owner(*, session: Session = Depends(get_session), owner: OwnerCreate):
    ...
```

## Part 4.2. GET /owners-full-details/{owner_id} (3/20 marks)

Implement an API to get details of `owner`, given the `owner_id` number
The response payload body may also include details of all the owned cars (if linked via `car.owner_id`)

```python
@app.get("/owners-full-details/{owner_id}", response_model=OwnerReadWithCars)
def read_owner_full_details(*, session: Session = Depends(get_session), owner_id: int):
    ...
```

## Part 4.3. POST /cars/ API (3/20 marks)

Implement an API to create `car`, given the `CarCreate` DTO definition as input type

```python
@app.post("/cars/", response_model=CarRead)
def create_car(*, session: Session = Depends(get_session), car: CarCreate):
    ...
```

## Part 4.4. GET /cars-full-details/{car_id} API (3/20 marks)

Implement an API to get details of `car`, given the `car_id` number
The response payload body may also include details of owner (if linked via `car.owner_id`)

```python
@app.get("/cars-full-details/{car_id}", response_model=CarReadWithOwner)
def read_car_full_details(*, session: Session = Depends(get_session), car_id: int):
    ...
```

## Part 4.5. PATCH /cars/{car_id} API (3/20 marks)

Implement an API that allow updating of either the owner `owner_id` or the plate number `plate_number` of that car

```python
@app.patch("/cars/{car_id}", response_model=CarRead)
def update_car(
    *, session: Session = Depends(get_session), car_id: int, car: CarUpdate
):
    ...
```

## Part 4.6. Unit testing (5/20 marks)

See file `Part_4/test_main.py`

Perform Unit testing on the API you created and provide some screenshot of the test evidence:

- (1/5 marks) POST owner
- (1/5 marks) GET owner
- (1/5 marks) POST car
- (1/5 marks) GET car with owner info
- (1/5 marks) PATCH car

You are welcome to provide robust testing of your APIs, considering different edge cases or ways it can fail. For the extra effort spent for testing, **you may earn up to 5 addition marks** (if you really need them). Consider this a "performance bonus", which you will encounter in real life somewhat often. I recommend investing in your test suite after you have completed the assignment though.Perform Unit testing on the API you created and provide some screenshot of the test evidence
