package _01AndreiPeterfi.tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.util.List;

public class DemoTheInternetTest extends BaseTest{

    @BeforeMethod
    public void beforeEach() {
        driver.get("https://the-internet.herokuapp.com/");
    }

    @Test(priority = 2)
    public void testNumberOfHomePageListElemets() {
        /** Get elements*/
        List<WebElement> allLinks = driver.findElements(By.cssSelector("ul li"));
        Assert.assertEquals(allLinks.size(), 44);
    }


}
