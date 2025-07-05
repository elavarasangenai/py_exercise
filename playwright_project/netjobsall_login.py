import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to login page
    page.goto("https://web.nithrapeople.com/staff/login")
    time.sleep(5)

    # Step 2: Enter mobile number
    page.fill('xpath=//*[@id="email-address"]', '7373*****')
    time.sleep(5)

    # Step 3: Enter password
    page.fill('xpath=//*[@id="current_password"]', '**********')
    time.sleep(5)

    # Click login button (assuming there is a button to click)
    page.click('button[type="submit"]')
    time.sleep(5)

    # Step 4: Check if login is successful by URL
    if page.url == "https://web.nithrapeople.com/staff/myProfile":
        # Click the menu item
        page.click('xpath=//*[@id="aside"]/aside/nav/ul/li[1]/a')
        time.sleep(5)
        # Step 5: Should be on dashboard
        if page.url == "https://web.nithrapeople.com/staff/dashboard":
            print("Successfully navigated to dashboard.")
            # Read the dashboard page content
            dashboard_content = page.content()
            # Save to a text file
            with open("dashboard_content.txt", "w", encoding="utf-8") as f:
                f.write(dashboard_content)
            print("Dashboard content saved to dashboard_content.txt.")
        else:
            print(f"Unexpected URL after clicking menu: {page.url}")
    else:
        print(f"Login failed or unexpected URL: {page.url}")

    browser.close()
