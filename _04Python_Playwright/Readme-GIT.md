# Steps for an update:

1. Create a new branch

    ```git checkout -b "branch_name"```

    This will create a new branch ***branch_name*** and will checkout on that branch.

    Equivalent to:
    ```
    git branch branch_name
    git checkout branch_name
    ``` 

    !!! Where we will create a rule for the branch name
   
    a) The branch name must start with the first letter from your firstname + the first from your last name
    
    ``ex: John Doe -> JD``

   b) The next part will be ***-Sugestive-Description-Separated-By-Minus***
    
    ``ex: JD-Added-Python-Test-For-The-Home-Page``

2. Implement the changes
3. Check locally for linter problems:
    a)Run check (verify files with issues):

    `black --check .`

    b)Show problems and possible bugs:
   
    ```flake8 .```
    
    c)Try to manually fix those problems

    d) After you have more experience, you can automatically correct potential warnings using:

    ```flake8 .```