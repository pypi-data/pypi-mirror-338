package scripts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class GeneratedSeleniumScript {
    private WebDriver driver;
    private WebDriverWait wait;

    public GeneratedSeleniumScript() {
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.manage().window().maximize();
    }

    public void execute() {
        try {

            // Navigation action
            driver.get("Logged in with username 'admin' and password 'admin', then navigated to Workflow Studio successfully.");

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }

    public static void main(String[] args) {
        new GeneratedSeleniumScript().execute();
    }
}
