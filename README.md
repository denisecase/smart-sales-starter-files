# smart-sales-starter-files
Starter files to help initialize the smart sales project.

-----

## Project Setup Guide (Mac/Linux)

Run all commands from a terminal in the root project folder. 

### Step A - Create a Local Project Virtual Environment

```shell
python3 -m venv .venv
```

### Step B - Activate the Virtual Environment

```shell
source .venv/bin/activate
```

### Step C - Install Packages

```shell
python3 -m pip install --upgrade -r requirements.txt
```

### Step D - Optional: Verify .venv Setup

```shell
python3 -m datafun_venv_checker.venv_checker
```

### Step E - Run the initial project script

```shell
python3 scripts/data_prep.py
```
-----

## Project Setup Guide (Windows)

Run all commands from a PowerShell terminal in the root project folder. 

### Step A - Create a Local Project Virtual Environment

```shell
py -m venv .venv
```

### Step B - Activate the Virtual Environment

```shell
.venv\Scripts\activate
```

### Step C - Install Packages

```shell
py -m pip install --upgrade -r requirements.txt
```

### Step D - Optional: Verify .venv Setup

```shell
py -m datafun_venv_checker.venv_checker
```

### Step E - Run the initial project script

```shell
py scripts/data_prep.py
```
-----

## Initial Package List
- pip
- loguru
- ipykernel
- jupyterlab
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- pyspark==4.0.0.dev1
- pyspark[sql]
- git+https://github.com/denisecase/datafun-venv-checker.git#egg=datafun_venv_checker

