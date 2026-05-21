import asyncio
from playwright.async_api import async_playwright
import os

async def take_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Load the page
        await page.goto('file:///home/bob/projects/web-designer-portfolio/demo/project-01/index.html')
        await page.wait_for_load_state('networkidle')
        
        # Take full page screenshot
        await page.screenshot(path='screenshots/hero-desktop.png', full_page=True)
        print("✅ Desktop screenshot saved")
        
        # Mobile viewport
        await page.set_viewport_size({'width': 375, 'height': 667})
        await page.reload()
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path='screenshots/hero-mobile.png', full_page=True)
        print("✅ Mobile screenshot saved")
        
        # Tablet viewport
        await page.set_viewport_size({'width': 768, 'height': 1024})
        await page.reload()
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path='screenshots/hero-tablet.png', full_page=True)
        print("✅ Tablet screenshot saved")
        
        await browser.close()

if __name__ == "__main__":
    os.makedirs('screenshots', exist_ok=True)
    asyncio.run(take_screenshots())
