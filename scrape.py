import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        total_sum = 0
        for i in range(1, 11):
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={i}"
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_selector('table')
            
            # get all td elements
            tds = await page.query_selector_all('td')
            for td in tds:
                text = await td.inner_text()
                try:
                    num = float(text.strip())
                    total_sum += num
                except ValueError:
                    pass
        print(f"Total Sum: {total_sum}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
