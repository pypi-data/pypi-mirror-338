package com.servicenow.test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import java.time.Duration;

public class SeleniumTest_20250328 {
    private WebDriver driver;
    private WebDriverWait wait;
    private JavascriptExecutor js;

    public void setup() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-debugging-port=9222");
        options.addArguments("--disable-web-security");
        options.addArguments("--disable-site-isolation-trials");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(60));
        js = (JavascriptExecutor) driver;
    }

    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    public void runTest() {
        try {
            setup();
            
            // Navigate to ServiceNow instance
            driver.get("http://localhost:8080");
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("body")));
            
            // Wait for login elements
            WebElement usernameInput = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("user_name")));
            WebElement passwordInput = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("user_password")));
            WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("button[type='submit']")));
            
            // Login
            usernameInput.sendKeys("admin");
            passwordInput.sendKeys("admin");
            submitButton.click();
            
            // Wait for navigation
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("macroponent-f51912f4c700201072b211d4d8c26010")));
            
            // Click All menu
            WebElement allButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("[aria-label='All']")));
            allButton.click();
            
            // Wait for menu to open
            wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("sn-polaris-menu.is-main-menu.is-open")));
            
            // Search for Workflow Studio
            WebElement searchInput = wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("input[placeholder='Filter']")));
            searchInput.sendKeys("Workflow Studio");
            
            // Click Workflow Studio link
            WebElement workflowLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//a[contains(text(), 'Workflow Studio')]")));
            workflowLink.click();
            
            // Wait for Workflow Studio to load
            wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("macroponent-f51912f4c700201072b211d4d8c26010")));
            
            // Add delay to ensure all events are captured
            Thread.sleep(2000);
            
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            tearDown();
        }
    }

    public static void main(String[] args) {
        SeleniumTest_20250328 test = new SeleniumTest_20250328();
        test.runTest();
    }
}
