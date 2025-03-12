import { test, expect } from '@playwright/test';
import {getNoOfListElements, gotoHomePage} from '../Pages/HomePage';

test.describe('Testing the Home Page', () => {
  
  test.beforeEach(async ({ page }) => {
    await gotoHomePage(page)
  })


  test('Check HomePage Title', async ({ page }) => {
    await expect(page).toHaveTitle("The Internet")
    await expect(page).toHaveURL("https://the-internet.herokuapp.com/")
    await expect(page.locator("h1")).toHaveText("Welcome to the-internet")
  });

  test('Check HomePage no of list elements', async ({ page }) => {
    await expect(page).toHaveTitle("The In1ternet")
    expect(await getNoOfListElements(page)).toBe(44)
  });


})
