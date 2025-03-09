import {test, expect} from '@playwright/test';
import {gotoHomePage, navigateToPagez} from '../Pages/HomePage';


test.describe('Testing the For Authentication page', () => {
    const usernameField = "#username"
    const passwordField = "#password"
    const btnSubmit = 'button[type="submit"]'
    const alertArea = "#flash"
    const logoutButton = ".button.secondary.radius"


    test.beforeEach(async ({page}) => {
        await gotoHomePage(page)
    })

    test('Successful login', async ({page}) => {
        await test.step("Navigate to Form Authentication page", async () => {
            await navigateToPagez(page, "Form Authentication")
        })
        await test.step("Login", async () => {
            await page.locator(usernameField).fill("tomsmith")
            await page.locator(passwordField).fill("SuperSecretPassword!")
            await page.locator(btnSubmit).click()
        })
        await test.step("Verify successful login", async () => {
            await expect(page.locator(alertArea)).toContainText("You logged into a secure area!")
            await expect(page.locator(logoutButton)).toBeVisible()
        })
        await test.step("Verify Page title", async () => {
            await expect(page).toHaveTitle("The Internet")
            await expect(page).toHaveURL("https://the-internet.herokuapp.com/secure")
        })
    })

    const credentials = [
        {username: "tomsmith", password: "SuperSecretPassword!", shouldPass: true},
        {username: "tomsmith", password: "SuperSecretPassword", shouldPass: false},
        {username: "tomsmit", password: "SuperSecretPassword!", shouldPass: false},
        {username: "tomsmith", password: "", shouldPass: false},
        {username: "", password: "SuperSecretPassword!", shouldPass: false}
    ];
    test.describe('Login tests', () => {
        test.beforeEach(async ({page}) => {
            await test.step("Navigate to Form Authentication page", async () => {
                await navigateToPagez(page, "Form Authentication")
            })
        })
        credentials.forEach(({username, password, shouldPass}) =>
            test(`Login with username "${username}" and password "${password}"`, async ({page}) => {

                await test.step("Login", async () => {
                    await page.locator(usernameField).fill(username)
                    await page.locator(passwordField).fill(password)
                    await page.locator(btnSubmit).click()
                })

                await test.step("Verify login", async () => {
                    if (shouldPass) {
                        await expect(page.locator(alertArea)).toContainText("You logged into a secure area!")
                        await expect(page.locator(logoutButton)).toBeVisible()
                        await expect(page).toHaveURL("/secure")
                        await expect(page).toHaveTitle("The Internet")
                    } else {
                        await expect(page.locator(alertArea)).toContainText(/Your username is invalid!|Your password is invalid!/)
                    }
                })
            }))
    })

})
