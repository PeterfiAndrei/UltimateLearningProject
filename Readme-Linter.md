# 1. Python
1. Install black (checker for python):
   `pip install flake8 black`
2. Run check (verify files with issues):
   `black --check .`
3. Show problems and possible bugs:
    `flake8 .`

    You can use the above commands for specific files too. Instead of point, use the file path, ex:
  
    `black _16EcuatieGradul2.py`
4. Auto-fix problems:
    `black .`
    Try running this program for specific files to see your mistakes(check the changes made to that file)
    


# 2. Typescript
1. Install eslint:

    `npm install -g eslint`

    `npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin`
2. Check all files (.ts and .js):

    `npx eslint . --max-warnings=0`

3. Fix errors:

    `npx eslint . --fix`

# 3. Python + Typescript
1. Check everything with one command:
    `flake8 . && black --check . && npx eslint . --max-warnings=0`