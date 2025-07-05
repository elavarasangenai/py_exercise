import asyncio
from playwright.async_api import async_playwright

async def read_first_email():
    # Step 1: Start Playwright
    async with async_playwright() as p:
        # Step 2: Open browser in incognito mode
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        # Step 3: Go to Gmail
        print("Opening Gmail...")
        await page.goto("https://mail.google.com")

        # Step 4: Check if already logged in
        try:
            await page.wait_for_selector('tr.zA', timeout=5000)
            print("Already logged in!")
        except:
            print("Need to login...")
            # Login process
            await page.fill('input[type="email"]', "****")
            await page.click('#identifierNext')

            await page.wait_for_selector('input[type="******"]')
            await page.fill('input[type="password"]', "your-password")
            await page.click('#passwordNext')

        # Step 5: Wait for inbox to load
        print("Loading inbox...")
        await page.wait_for_selector('tr.zA', timeout=30000)

        # Step 6: Click first email
        print("Opening first email...")
        await page.click('tr.zA')

        # Step 7: Wait for email to load and get content
        await page.wait_for_timeout(3000)

        try:
            subject = await page.text_content('h2')
            sender = await page.text_content('span[email]')
            body = await page.text_content('div[dir="ltr"]')

            # Step 8: Print results
            print("\n=== EMAIL CONTENT ===")
            print("Subject:", subject)
            print("From:", sender)
            print("Body:", body[:200] + "..." if body else "No body content")

        except Exception as e:
            print("Error reading email:", e)

        # Step 9: Close browser
        print("\nClosing browser...")
        await browser.close()

# Run the program

def main():
    asyncio.run(read_first_email())

if __name__ == "__main__":
    main()