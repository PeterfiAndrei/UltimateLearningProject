package _01AndreiPeterfi.tests;

import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class DemoHowToCheckIfFleakyTest extends BaseTest {
    @BeforeMethod
    public void beforeEach() {
        driver.get("http://www.google.ro");
    }

    @Test(invocationCount = 5) // Run the test 5 times
    public void testUrlAndTitleAgain() {
        String currentUrl = driver.getCurrentUrl();
        String currentPageTabTitle = driver.getTitle();
        Assert.assertEquals(currentUrl, "https://www.google.ro/");
        Assert.assertEquals(currentPageTabTitle, "Google");
    }
}
