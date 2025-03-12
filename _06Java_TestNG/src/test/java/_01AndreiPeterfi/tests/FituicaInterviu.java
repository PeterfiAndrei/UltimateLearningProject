package _01AndreiPeterfi.tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.time.Duration;
import java.util.List;

public class FituicaInterviu {
    WebDriver driver;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        ChromeOptions chromeOptions = new ChromeOptions();
        chromeOptions.addArguments("--incognito");
//        chromeOptions.addArguments("--headless");
        driver = new ChromeDriver(chromeOptions);
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));//Implicit
        driver.get("https://www.google.ro/");
    }

    @Test(priority = 0)
    public void testNumeTest() {
        String currentUrl = driver.getCurrentUrl();
        String currentPageTabTitle = driver.getTitle();
        Assert.assertEquals(currentUrl, "https://www.google.ro/");
        Assert.assertEquals(currentPageTabTitle, "Google");
        By btnAcceptAllCookies = By.id("L2AGLb");
        /** Explicit wait */
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
        wait.until(ExpectedConditions.visibilityOfElementLocated(btnAcceptAllCookies));
        driver.findElement(btnAcceptAllCookies).click();

        boolean isInvisible = wait.until(ExpectedConditions.invisibilityOfElementLocated(By.id("myElement")));
        Assert.assertTrue(isInvisible);

        driver.get("https://the-internet.herokuapp.com/");
        /** Get elements*/
        List<WebElement> allLinks = driver.findElements(By.cssSelector("ul li"));
        Assert.assertEquals(allLinks.size(), 44);
    }
    @AfterMethod
    public void tearDown(){
        if(driver!=null){
            driver.quit();
        }
    }

}
