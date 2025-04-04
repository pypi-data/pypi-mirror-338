package selenium_tests;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class SeleniumTest_20250327_142447 {
    private WebDriver driver;
    private WebDriverWait wait;

    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-debugging-port=9222");
        options.addArguments("--disable-web-security");
        options.addArguments("--disable-site-isolation-trials");
        options.addArguments("--disable-features=IsolateOrigins,site-per-process");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    public void runTest() {
        try {
            setUp();
            driver.get("http://localhost:8080/");
            wait.until(ExpectedConditions.titleContains("Log in | ServiceNow"));
            driver.get("http://localhost:8080/now/nav/ui/home");
            wait.until(ExpectedConditions.titleContains("Unified Navigation App | ServiceNow"));
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            tearDown();
        }
    }

    public static void main(String[] args) {
        SeleniumTest_20250327_142447 test = new SeleniumTest_20250327_142447();
        test.runTest();
    }
}