import { defineConfig } from '@playwright/test';

export default defineConfig({
    testDir: './tests', // Directorul unde sunt testele
    timeout: 30000, // Timeout global pentru teste (30 sec)
    expect: {
        timeout: 5000, // Timeout pentru `expect()`
    },
    workers: 4, // Playwright va folosi 4 procese în paralel
    retries: 3, // Reîncearcă testele de max. 2 ori dacă eșuează
    // reporter: [['html', { open: 'never' }]], // Raport HTML standard
    reporter: [
        ["line"],
        ['allure-playwright'],
        ['_03Typescript_Playwright/reporters/flaky-reporter.js']
    ],

    use: {
        testIdAttribute: 'id', // Definește atributul implicit pentru testare, se va folosi getByTestId pentru a cauta
        headless: process.env.CI ? true : false, // Rulează testele fără UI (true) sau cu UI vizibil (false)
        viewport: { width: 1280, height: 720 }, // Dimensiunea ferestrei browserului
        ignoreHTTPSErrors: true, // Ignoră erorile SSL
        trace: 'on-first-retry', // Salvează trace doar dacă testul eșuează prima dată
        screenshot: 'only-on-failure', // Fă capturi de ecran doar când un test eșuează
        video: 'retain-on-failure', // Înregistrează video doar dacă testul eșuează
        baseURL: 'https://the-internet.herokuapp.com/secure', // URL implicit pentru testele tale
    },
    projects: [
        {
            name: 'chromium',
            use: { browserName: 'chromium' },
        }
        // ,
        // {
        //     name: 'firefox',
        //     use: { browserName: 'firefox' },
        // },
        // {
        //     name: 'webkit',
        //     use: { browserName: 'webkit' },
        // },
    ],

});