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
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

public class SeleniumTest_20250404_092553 {
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static JavascriptExecutor js;
    private static Properties config;

    @BeforeClass
    public static void setup() throws IOException {{
        // Load configuration from properties file
        config = new Properties();
        try (FileInputStream fis = new FileInputStream("config.properties")) {{
            config.load(fis);
        }}

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
    }}

    @AfterClass
    public static void tearDown() {{
        if (driver != null) {{
            driver.quit();
        }}
    }}

    private static WebElement findElementWithShadowDOM(String shadowPath) {{
        String[] selectors = shadowPath.split(" >>> ");
        WebElement element = null;
        
        for (String selector : selectors) {{
            if (element == null) {{
                element = driver.findElement(By.cssSelector(selector));
            }} else {{
                element = (WebElement) js.executeScript("return arguments[0].shadowRoot", element);
                element = element.findElement(By.cssSelector(selector));
            }}
        }}
        return element;
    }}

    private static WebElement waitForElement(By locator) {{
        return wait.until(ExpectedConditions.presenceOfElementLocated(locator));
    }}

    private static WebElement waitForElementClickable(By locator) {{
        return wait.until(ExpectedConditions.elementToBeClickable(locator));
    }}

    private static void waitForPageLoad() {{
        wait.until(webDriver -> ((JavascriptExecutor) webDriver).executeScript("return document.readyState").equals("complete"));
    }}

    @Test
    public void testServiceNowAutomation() {{
        try {{
            // Navigate to ServiceNow instance
            String servicenowUrl = config.getProperty("servicenow.url", "https://your-instance.service-now.com");
            driver.get(servicenowUrl);
            waitForPageLoad();

            // Navigate to login page
            driver.get("http://localhost:8080/login.do");
            waitForPageLoad();

            // Input username
            WebElement usernameInput = waitForElement(By.id("user_name"));
            usernameInput.clear();
            usernameInput.sendKeys("admin");

            // Input password
            WebElement passwordInput = waitForElement(By.id("user_password"));
            passwordInput.clear();
            passwordInput.sendKeys("admin");

            // Click login button
            WebElement loginButton = waitForElementClickable(By.id("sysverb_login"));
            loginButton.click();
            waitForPageLoad();

            // Scroll down to reveal elements
            js.executeScript("window.scrollBy(0, 200)");

            // Click New button
            WebElement newButton = waitForElementClickable(By.xpath("//button[contains(text(), 'New')]"));
            newButton.click();
            waitForPageLoad();

            // Click Flow tab
            WebElement flowTab = waitForElementClickable(By.xpath("//span[contains(text(), 'Flow')]"));
            flowTab.click();
            waitForPageLoad();

        }} catch (Exception e) {{
            System.err.println("Error during test execution: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }}
    }}
}