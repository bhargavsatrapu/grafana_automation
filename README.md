## Introduction

GRAFANA Automation is a Pytest framework built using Playwright written in Python.

### Prerequisites
#### Installation process
1. **Python Installed**: Ensure that Python is installed on your system. You can download and install Python from the official Python website (https://www.python.org/). Ensure the latest version of Python (Python 3.12.3) is downloaded to your system.
2. **PyCharm Installed**: Download and install PyCharm IDE from JetBrains website (https://www.jetbrains.com/pycharm/). PyCharm comes in two editions: Community (free) and Professional (paid). The Community edition should be fine for most automation frameworks.
3. **Git Installed**: To clone the automation framework from a Git repository, Git needs to be installed on your system. You can download Git from the official website (https://git-scm.com/).
4. **pip installed**: Download the `get-pip.py` script from the official Python website.
   ```
   Run the following command in command prompt or terminal:
       curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
   Then, run the following command to install pip:
       python get-pip.py
   Verify pip is installed using the following command:
       pip --version
   ```

### Cloning Repo
1. **Open Command Prompt as Admin**: Open Command Prompt (Windows) or Terminal (macOS/Linux) on your computer.
2. **Navigate to the Directory Where You Want to Clone the Repository**: Use the `cd` command to navigate to the directory where you want to clone the repository.
   For example:
   ```
   cd C:\Users\MyUser\PyCharmProjects
   ```                              
3. **Clone the Repository**: Navigate to https://github.com/bhargavsatrapu/grafana_automation.git, click on the Clone button, and copy the HTTPS URL. Use the `git clone` command followed by the URL of the repository you want to clone.
   For example:
   ```
   git clone https://github.com/bhargavsatrapu/grafana_automation.git
   ```
4. **Authenticate (if required)**: If the repository is private and requires authentication, Git will prompt you to enter your username and password. You can click on the Generate Git Credentials button to generate a username and password.
5. **Wait for the Clone to Complete**: Git will start cloning the repository to your local machine. Once the clone is complete, you'll see a message indicating that the clone was successful.
6. **Navigate to the Cloned Repository**: After the clone is complete, you can navigate into the cloned repository's directory using the `cd` command.
   For example:
   ```
   cd C:\Users\MyUser\PyCharmProjects\grafana_automation
   ```

### Create a Virtual Environment in Python in the Project Directory
1. **Open Terminal or Command Prompt**: Open the Terminal (macOS/Linux) or Command Prompt (Windows) on your computer.
2. **Navigate to the Directory Where You Want to Create the Virtual Environment**: Use the `cd` command to navigate to the directory where you want to create the virtual environment. For example, if you want to create it in your project directory:
   ```
   cd C:\Users\MyUser\PyCharmProjects\grafana_automation
   ```
3. **Create the Virtual Environment**: Once you're in the desired directory, use the following command to create a virtual environment named `.venv`:
   ```
   python -m venv .venv
   ```
4. **Activate the Virtual Environment**: After creating the virtual environment, you need to activate it. The activation process varies depending on your operating system:
   - **MacOS/Linux**:
     ```
     source .venv/bin/activate
     ```
   - **Windows (Command Prompt)**:
     ```
     .venv\Scripts\activate
     ```
5. **Deactivate the Virtual Environment (Optional)**: To deactivate the virtual environment and return to your global Python environment, simply use the `deactivate` command:
   ```
   deactivate
   ```
### Install All Necessary Libraries and Packages
1. **Open Terminal or Command Prompt**: Open Command Prompt as Admin (from the Start menu using "Run as administrator") or Terminal and navigate to the project directory.
2. **Activate Virtual Environment**: Activate the virtual environment in the automation project directory.
3. **Install All Dependencies**: Install all dependencies using the `pip install` command:
   ```
   pip install -r requirements.txt
   ```
   
### Fill the `config.ini` File with Your Data
1. **Locate the `config.ini` File**: The `config.ini` file is located in the `configurations` folder within the project directory.
2. **Edit the `config.ini` File**: Open the `config.ini` file and fill in the following details based on your system configuration:
   ```
   [common info]
   URL = http://127.0.0.1:3000/login
   USER_NAME = admin
   PASSWORD = grafana_automation1
   DB_HOST = 127.0.0.1
   DB_USER = root
   DB_PASSWORD = Grafana_automation1
   DB_NAME = my_database
   DB_PORT = 3306
   ```
   - **URL**: This is the Grafana URL.
   - **USER_NAME**: Grafana username.
   - **PASSWORD**: Grafana password.
   - **DB_HOST**: The database host configured with the Grafana application.

### Run Test Cases
Open the Command Prompt and run pytest in terminal to run all test cases. you can run any specific test by following command.
```
pytest .\Testcases\test_name.py
```

### Test Execution Report
Once test execution is completed, an HTML report file will be generated and its location will be provided in the terminal logs.

