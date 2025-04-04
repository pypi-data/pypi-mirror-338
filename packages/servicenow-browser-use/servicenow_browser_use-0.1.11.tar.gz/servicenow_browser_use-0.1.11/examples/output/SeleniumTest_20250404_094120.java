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

public class SeleniumTest_20250404_094120 {
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

            // Input text into element
            WebElement inputElement = waitForElement(By.id("user_name"));
            inputElement.clear();
            inputElement.sendKeys("admin");

            // Input text into element
            WebElement inputElement = waitForElement(By.id("user_password"));
            inputElement.clear();
            inputElement.sendKeys("admin");

            // Click element
            WebElement clickElement = waitForElementClickable(By.id("sysverb_login"));
            clickElement.click();
            waitForPageLoad();

            // Click shadow DOM element
            WebElement clickElement = findElementWithShadowDOM("macroponent-d469c54f433f61106c4bb0117fb8f267 >>> sn-user-preferences-provider#userPrefProvider >>> sn-aria-live-region >>> now-popover-panel >>> seismic-hoist");
            clickElement.click();
            waitForPageLoad();

        }} catch (Exception e) {{
            System.err.println("Error during test execution: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }}
    }}
}