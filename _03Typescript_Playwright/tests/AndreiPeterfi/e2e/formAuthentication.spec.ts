import { test, expect } from '@playwright/test';
import { gotoHomePage, navigateToPagez } from '../Pages/HomePage';


test.describe('Testing the For Authentication page', () => {
    const usernameField = "#username"
    const passwordField = "#password"
    const btnSubmit = 'button[type="submit"]'
    const alertArea = "#flash"
    const logoutButton = ".button.secondary.radius"


    test.beforeEach(async ({ page }) => {
        await gotoHomePage(page)
    })




    test('Successful login', async ({ page }) => {
        await navigateToPagez(page,"Form Authentication")
        await page.locator(usernameField).fill("tomsmith")
        await page.locator(passwordField).fill("SuperSecretPassword!")
        await page.locator(btnSubmit).click()
        await expect(page.locator(alertArea)).toContainText("You logged into a secure area!")
        await expect(page.locator(logoutButton)).toBeVisible()

    })


    
    
})
