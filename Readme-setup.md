# I. Selenium + Java setup
	1. From IntelliJ create a new project in the desired location
		->Set java 11 & maven
	2. In pom.xml add Selenium, Junit and WebdriverManager (search them on https://mvnrepository.com/ )

# II.  Python + Playwright setup
	1. Make sure Python is installed on your device:
		a) python --version
		b) If it is not installed: download it from https://www.python.org/downloads/
		✔️ IMPORTANT: during installation, on the FIRST step check "Add Python to PATH"!
	2. Check if 'py' is working
		py -m venv venv
	
	3. If it doesn't work you might need to manually add Python to PATH	
		->Open 'Environment Variables'
			->Under System Variables, edit the 'Path' Variable and add:
				C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python311\
				C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python311\Scripts\
		->Restart the shell and check again if python is installed: python --version
	4. Navigate to your project location (using shell) and type:
		a) python -m venv venv
		b) .\venv\Scripts\Activate
		c) pip install playwright pytest
		d) playwright install

# III. Typescript + Playwright setup
	1. Navigate to the Typescript package
	2. Using shell send:(you might need to install npm)
		a) npm init -y
		b) npm install playwright @playwright/test typescript --save-dev
		c) npx playwright install
	3. Run a test: npx playwright test formAuthentication.spec.ts --headed

# IV. Java + Cucumber
	1. From IntelliJ create a new project in the desired location
		->Set java 11 & maven
	2. In pom.xml add Selenium, Cucumber and WebdriverManager (search them on https://mvnrepository.com/ )

# V. Programming
	1. For Python, cd to _05Programming/PythonProgramming and install python if needed(google it)
	2. Instal Python plugins
    3. After cloning the project, you'll need to open only the Specific python package as a project