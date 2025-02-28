# Typescirpt & Playwright Setup
## 1. Install
1.   npm init -y
2.   npm install --save-dev @playwright/test typescript
3.   npx playwright install


## 2. tsconfig.json
1. Create tsconfig.json at the root path if it doesn't exist
2. Add this code to your json file
```json
    {
    "compilerOptions": {
        "target": "ES2016",
        "lib": ["ES2016", "DOM"],
        "module": "CommonJS",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true
        }
    }
```
## 3. playwright.config.ts
1. Create playwright.config.ts at the root path if it doesn't exist
2. Add this code to your json file
```typescript
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
        testDir: './tests', // Directorul unde sunt testele
        timeout: 30000, // Timeout global pentru teste (30 sec)
        expect: {
            timeout: 5000, // Timeout pentru `expect()`
        },
        workers: 4, // Playwright va folosi 4 procese în paralel
        retries: 2, // Reîncearcă testele de max. 2 ori dacă eșuează
        reporter: [['html', { open: 'never' }]], // Raport HTML standard
        // reporter: [['allure-playwright']], // Integrare cu Allure (necesită instalare)
    
        use: {
            testIdAttribute: 'id', // Definește atributul implicit pentru testare, se va folosi getByTestId pentru a cauta
            headless: false, // Rulează testele fără UI (true) sau cu UI vizibil (false)
            viewport: { width: 1280, height: 720 }, // Dimensiunea ferestrei browserului
            ignoreHTTPSErrors: true, // Ignoră erorile SSL
            trace: 'on-first-retry', // Salvează trace doar dacă testul eșuează prima dată
            screenshot: 'only-on-failure', // Fă capturi de ecran doar când un test eșuează
            video: 'retain-on-failure', // Înregistrează video doar dacă testul eșuează
            baseURL: 'https://playwright.dev', // URL implicit pentru testele tale
        },
        projects: [
            {
                name: 'chromium',
                use: { browserName: 'chromium' },
            },
            {
                name: 'firefox',
                use: { browserName: 'firefox' },
            },
            {
                name: 'webkit',
                use: { browserName: 'webkit' },
            },
        ],
    
    });

```

# 4. Install Allure report locally:
```shell
  npm install --save-dev @playwright/test allure-playwright
```
```shell
  npm install -g allure-commandline
```

# 5. Generate Allure report:
```shell
    npx allure generate allure-results --clean ; npx allure open
```