# test-notepad-online-python
------------------Read me-------------------
1. Setup Environment:
- Python 2.7
- Set up Python and add new environment variable:
    - C:\Python27
    - C:\Python27\Scripts
- Install PyCharm IDE
- Setting Python interpreter and Vituralenv Environment
- Install pip
- Open command line in folder test-notepad-online-python
- Install packages in requirment.txt file with comment : pip install -r requirements.txt

2. Run test with command line:
- steps 1: Change chrome path in file config
- steps 2: Open command line in folder test-notepad-online-python
- steps 3: Run: pytest --html=result.html Steps_define\test_login.py -s
- steps 4: Wait for done and check result.html

2. Run test with Pycharm:
- steps 1: Change chrome path in file config
- steps 2: Add new config runner pytest:
    - Target: Script path and choose file test_login.py
    - Additional Argument: --html=result.html
    - Python Interpreter: Python 2.7
    - Working space: choose folder test-notepad-online-python
- steps 3: Choose button Run and wait for done and check result.html
