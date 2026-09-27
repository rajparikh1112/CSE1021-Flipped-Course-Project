# CSE1021-Flipped-Course-Project
# ATM Management System

## Project Title

**ATM Management System**

## About the Project

I made this ATM Management System using Python for my **Python Essentials / VITyarthi course project**.

The idea was to make a simple ATM program where different users can log in with their username and PIN. After logging in, they can check their balance, withdraw money, deposit money, change their PIN, or exit the program.

I have used three sample accounts in the program so I can test the different options.

## Features

The program has these main features:

* Login with username and PIN
* Check balance
* Withdraw money
* Deposit money
* Change PIN
* Check insufficient balance
* Handle wrong menu choices
* Three different user accounts
* ATM menu
* Exit option

### Accounts Used for Testing

| Username |    PIN |  Balance |
| -------- | -----: | -------: |
| Raj      | 121007 | ₹150,000 |
| Kritika  | 123456 | ₹120,000 |
| Nidish   | 141926 | ₹900,000 |

These are just sample accounts for testing the program.

## Technologies and Tools

For making this project, I used:

* Python 3
* VS Code
* Terminal
* Git
* GitHub

I also used basic Python topics that I learned during the course, including variables, lists, input/output, conditions, loops, operators, type conversion, and menu-based programming.

## How to Install and Run

### 1. Install Python

First, Python 3 needs to be installed on the computer.

To check it, open the terminal and type:

```text id="m8nq3c"
python --version
```

### 2. Download the Project

Download the project from GitHub and open the project folder.

### 3. Open the File

Open the folder in VS Code.

The Python file is:

```text id="j1h5qk"
CSEVITYARTHIPROJECTsem1.py
```

### 4. Run the Program

Open the terminal in the same folder and enter:

```text id="c2r7vx"
python CSEVITYARTHIPROJECTsem1.py
```

The ATM program will start.

### 5. Login

Enter a username and its PIN.

For example:

text id="a8x2pd"
Username: Raj
PIN: 121007
```

If the details are correct, the ATM menu will open.

## ATM Menu

After login, the program shows:

```text id="n0v7sy"
********ATM MENU********
select 1 to check balance
select 2 to withdraw money
select 3 to Deposite money
select 4 to change PIN
select 5 to EXIT
```

I can enter the number of the option I want to use.

## Testing

I tested the program with different inputs to make sure the options were working.

For example:

| What I tested              | What should happen                |
| -------------------------- | --------------------------------- |
| Correct username           | PIN is asked                      |
| Wrong username             | Invalid username is displayed     |
| Correct PIN                | ATM menu opens                    |
| Option `1`                 | Balance is displayed              |
| Option `2`                 | Money can be withdrawn            |
| Withdraw more than balance | Insufficient balance is displayed |
| Option `3`                 | Money can be deposited            |
| Invalid deposit            | Invalid input is displayed        |
| Option `4`                 | PIN can be changed                |
| Option `5`                 | Program closes                    |
| Wrong menu number          | Invalid choice is displayed       |

I also tested the program with Raj, Kritika, and Nidish to check the different accounts.

## Screenshots

I will add screenshots of the program here.

The screenshots can include:

* Login screen
* ATM menu
* Balance
* Withdrawal
* Deposit
* PIN change
* Exit message

## Project Files

```text id="v5r8kc"
ATM-Management-System/
│
├── CSEVITYARTHIPROJECTsem1.py
└── README.md
```

## Author

**Raj Parikh**
**Registration No.: 26BCE10880**
**1st Year, CSE Core**
**VIT Bhopal University**

**Python Essentials / VITyarthi Course Project**
