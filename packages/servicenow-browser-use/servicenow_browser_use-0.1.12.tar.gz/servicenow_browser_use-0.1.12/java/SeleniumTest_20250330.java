package com.selenium.test;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import java.time.Duration;
import org.testng.annotations.*;
import java.util.ArrayList;

public class SeleniumTest_20250330 {
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static Actions actions;
    private static JavascriptExecutor js;

    @BeforeClass
    public static void setup() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.addArguments("--disable-web-security");
        options.addArguments("--disable-site-isolation-trials");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        actions = new Actions(driver);
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

    private static void waitForElementToBeClickable(WebElement element) {
        wait.until(ExpectedConditions.elementToBeClickable(element));
    }

    private static void scrollToElement(WebElement element) {
        js.executeScript("arguments[0].scrollIntoView(true);", element);
    }

    @Test
    public void runTest() {
        try {
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}