import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        await page.goto('file:///home/bob/projects/web-designer-portfolio/demo/project-02/index.html')
        await page.wait_for_load_state('networkidle')
        
        await page.screenshot(path='screenshots/project-02-desktop.png', full_page=True)
        print("✅ Desktop screenshot saved")
        
        await page.set_viewport_size({'width': 375, 'height': 667})
        await page.reload()
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path='screenshots/project-02-mobile.png', full_page=True)
        print("✅ Mobile screenshot saved")
        
        await browser.close()

if __name__ == "__main__":
    os.makedirs('screenshots', exist_ok=True)
    asyncio.run(take_screenshots())
