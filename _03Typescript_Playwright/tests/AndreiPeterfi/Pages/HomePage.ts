import { Page } from '@playwright/test';


export async function gotoHomePage (page: Page){
    await page.goto('https://the-internet.herokuapp.com/');
}
  


export async function navigateToPagez(page: Page, whereToGo:string){
    await page.getByText(whereToGo).click()
}


