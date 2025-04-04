package com.example.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import java.time.Duration;
import org.testng.annotations.*;

public class SeleniumTest_20250403_162831 {
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static JavascriptExecutor js;

    @BeforeClass
    public static void setup() {
        // Set up Chrome options
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.addArguments("--disable-web-security");
        options.addArguments("--disable-site-isolation-trials");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--remote-debugging-port=9222");
        
        // Initialize WebDriver
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(30));
        
        // Initialize WebDriverWait and JavascriptExecutor
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        js = (JavascriptExecutor) driver;
    }

    @AfterClass
    public static void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    private static WebElement findElementWithShadowDOM(String shadowPath) {
        String[] selectors = shadowPath.split(" >>> ");
        WebElement element = null;
        
        for (String selector : selectors) {
            if (element == null) {
                element = driver.findElement(By.cssSelector(selector));
            } else {
                element = (WebElement) js.executeScript("return arguments[0].shadowRoot", element);
                element = element.findElement(By.cssSelector(selector));
            }
        }
        return element;
    }

    private void handleLogin() throws InterruptedException {
        // Wait for username field and enter credentials
        WebElement usernameField = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("user_name")));
        usernameField.clear();
        usernameField.sendKeys("admin");
        Thread.sleep(500);

        // Enter password
        WebElement passwordField = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("user_password")));
        passwordField.clear();
        passwordField.sendKeys("admin");
        Thread.sleep(500);

        // Click login button
        WebElement loginButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("sysverb_login")));
        loginButton.click();
        Thread.sleep(2000);  // Wait for login to complete
    }

    @Test
    public void runTest() {
        try {
            // Navigate to the target website
            driver.get("https://k8s0722360-node1.thunder.devsnc.com/now/workflow-studio/home/process");
            Thread.sleep(2000);  // Wait for initial page load

            // Handle login if redirected
            if (driver.getCurrentUrl().contains("login.do")) {
                handleLogin();
            }

            // Wait for page to load after login
            Thread.sleep(2000);

            // Click on New button
            WebElement newButton = wait.until(ExpectedConditions.elementToBeClickable(
                By.cssSelector("button[data-testid='new-button']")))
            newButton.click();
            Thread.sleep(1000);

            // Verify Flow tab is present
            WebElement flowTab = wait.until(ExpectedConditions.presenceOfElementLocated(
                By.cssSelector("div[data-testid='flow-tab']")))
            assert flowTab.isDisplayed() : "Flow tab is not visible";

        } catch (Exception e) {
            System.err.println("Test failed with error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            tearDown();
        }
    }

    public static void main(String[] args) {
        SeleniumTest_20250403_162831 test = new SeleniumTest_20250403_162831();
        test.runTest();
    }
}