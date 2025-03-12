package _01AndreiPeterfi.tests;

import org.testng.Assert;
import org.testng.annotations.*;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class DemoGoogleTest extends BaseTest {

    @BeforeMethod
    public void beforeEach() {
        driver.get("http://www.google.ro");
    }

    @Test(priority = 0)
    public void testUrlAndTitle() {
        String currentUrl = driver.getCurrentUrl();
        String currentPageTabTitle = driver.getTitle();
        Assert.assertEquals(currentUrl, "https://www.google.ro/");
        Assert.assertEquals(currentPageTabTitle, "Google");
    }

    @Test(priority = 2)
    public void testAcceptCookies() {
        By btnAcceptAllCookies = By.id("L2AGLb");
        /** Explicit wait */
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
        wait.until(ExpectedConditions.visibilityOfElementLocated(btnAcceptAllCookies));
        driver.findElement(btnAcceptAllCookies).click();

        boolean isInvisible = wait.until(ExpectedConditions.invisibilityOfElementLocated(By.id("myElement")));
        Assert.assertTrue(isInvisible);
    }

}
