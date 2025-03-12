import {test, expect} from '@playwright/test'
import {gotoHomePage, navigateToPagez} from '../Pages/HomePage'
import {getHeaderText} from '../Pages/ABPage'


test.describe('Testing the A/B page', () => {

    test.beforeEach(async ({page}) => {
        await gotoHomePage(page)
    })

    test('A/B - Check Header', async ({page}) => {
        await test.step("Navigate to A/B page", async () => {
            await navigateToPagez(page, "A/B Testing")
        })

        await test.step("Check Header", async () => {
            expect(await getHeaderText(page)).toContain("A/B Test Variation 1")
        })
    })
})
