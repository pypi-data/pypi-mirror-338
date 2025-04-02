# Single Molecule Simulations - BP
-----------------------------------------

- Author: Baljyot Singh Parmar
- Affiliation at the time of writing: McGill University, Canada. Weber Lab

Please read the [User Guide](User_Guide_MD.md) for details on the features of this project along with some examples.
## 1. Installation
-------------------
### ***Anaconda*** 

1. Make sure you have anaconda installed: <https://www.anaconda.com/download>
2. Download or clone this repository.
3. In the conda prompt, navigate to the folder where you downloaded this repository using : 
```bash
cd "path_to_folder"
```
4. Using the **SMS_BP.yml** file, create a new environment using: 
```bash
conda env create -f SMS_BP.yml
```


- If you get an environment resolve error but you have anaconda installed just skip to step 6. The .yml file is for people who are using miniconda and might not have the packages already installed with the full anaconda install.
- You may want to still have a conda environment so just create a generic one if you want with the name SMS_BP or whatever you want with python>=3.12. Explicitly, 
```bash
conda create -n [my_env_name] python=3.12
```
5. Activate the environment using: 
```bash
conda activate SMS_BP
```
6. Now we will install this package in edit mode.
    - Run the command:
```bash
pip install -e . --config-settings editable_mode=compat
```

### ***Pip***

1. Make sure you have pip installed: <https://pip.pypa.io/en/stable/installing/>
2. Make sure you have python 3.10.13 as the active interpreter (through venv or conda or whatever you want).
3. Make sure pip is also installed.
4. Install from pypi using: 
```bash
pip install SMS-BP
```

### ***Installing the CLI tool using UV***
1. Install UV (https://docs.astral.sh/uv/getting-started/installation/).
2. Run the command:
```bash
uv tool install SMS_BP
```
3. You will have access to two CLI commands (using the uv interface):
    - `run_SMS_BP runsim` : This is the main entry point for the simulation. (see `run_SMS_BP runsim --help` for more details)
    - `run_SMS_BP config` : This is a helper tool to generate a template config file for the simulation. (see `run_SMS_BP config --help` for more details)
    - Note: using `run_SMS_BP --help` will show you all the available commands.
4. You can now use these tools (they are isolated in their own env created by uv, which is cool): 
```bash
run_SMS_BP config [PATH_TO_CONFIG_FILE]
```
```bash
run_SMS_BP runsim [PATH_TO_SAVED_CONFIG_FILE]
```
## 2. Running the Simulation

Having installed the package, make sure the CLI commands are working:
```bash
run_SMS_BP --help
```
If this does not work submit an issue on the github repository. TODO: convert this into tests.

1. This is a note on using the CLI tool properly. In the install (step 6) we also installed a CLI tool to interface with the program from anywhere. The only condition is that you are in the SMS_BP conda environment or similar venv you created and installed to (unless you used uv). 
    - Create a template of the config file with default parameters using 
    ```bash
    run_SMS_BP config [PATH_TO_CONFIG_FILE]
    ```
    This will create a **sim_config.json** file in the current directory. You can add a optional argument (path) to be a **[PATH]** to save the file elsewhere.
    - To run the CLI tool after the install we can type 
    ```bash
    run_SMS_BP runsim [PATH_TO_SAVED_CONFIG_FILE]
    ```
    - If you used 1) then this is just:
    ```bash
    run_SMS_BP runsim sim_config.json
    ```
    from anywhere assuming the path you provide is absolute.
    - In the background all this is doing is running: 
    ```python
    from SMS_BP.run_cell_simulation import typer_app_sms_bp; typer_app_sms_bp()
    ```
    This is the entry point.
    - Do note that the config checker is not robust so if you have prodived the wrong types or excluded some parameters which are required alongside other ones you will get an error. Read the **src/SMS_BP/sim_config.md** for details into the config file parameters.
TODO: create CI tests for this.
2. If you run into any issues please create a Github issue on the repository as it will help me manage different issues with different people and also create a resource for people encountering a solved issue.
