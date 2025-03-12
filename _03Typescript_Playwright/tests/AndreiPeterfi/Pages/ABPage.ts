import {Page} from '@playwright/test';


// Constants
const headerLocator: string = "#content h3"

export async function getHeaderText(page: Page): Promise<string> {
    return page.locator(headerLocator).innerText()
}
