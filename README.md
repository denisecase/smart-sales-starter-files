# smart-sales-starter-files

Starter files to initialize the smart sales project.

Since we use external packages, follow these steps carefully:

1. Pull any recent changes from GitHub.
2. Create a virtual environment.
3. Activate the `.venv`.
4. Install base tools.
5. Install external packages from `requirements.txt`.
6. Run `scripts/data_prep.py`.

## Before You Start

- Your **raw data files** must be in the `data/raw` directory. See Module 1 for more.
- See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01) for detailed instructions on professional Python projects workflow.
- For a complete setup guide, visit [pro-analytics-01](https://github.com/denisecase/pro-analytics-01).
- See `requirements.txt` for a concise version of the professional setup workflow.

## Important 

- Run all commands from a terminal in the root project folder. 
- Run each command one at a time and wait for it to finish before continuing. 

## Mac/Linux Commands

Open your smart sales repository in VS Code. 
Run all commands from a terminal in the root project folder. 

```shell
git pull
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt --timeout 100
python3 scripts/data_prep.py
```


## Windows PowerShell Commands

Open your smart sales repository in VS Code. 
Run all commands from a PowerShell terminal in the root project folder.

```shell
git pull
py -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
py scripts/data_prep.py
```


## After Making Progress

Once you’ve verified the script ran successfully, 
git add, commit, and push changes to your GitHub repository.

```shell
git add .
git commit -m "ran initial data_prep.py"
git push -u origin main
```

For best results, git add-commit-push frequently after making any useful progress. 
