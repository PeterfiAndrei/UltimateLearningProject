import {Page} from '@playwright/test';


// Constants
const listElements: string = "ul li"

export async function gotoHomePage(page: Page) {
    await page.goto('https://the-internet.herokuapp.com/');
}


export async function navigateToPagez(page: Page, whereToGo: string) {
    await page.getByText(whereToGo).click()
}

export async function getNoOfListElements(page: Page): Promise<number> {
    return await page.locator(listElements).count()
}
