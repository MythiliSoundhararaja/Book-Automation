from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os

def scrape_chapter(url):
    browser = None 
    with sync_playwright() as p:
        try:
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000, wait_until="domcontentloaded")
            page.wait_for_load_state("networkidle")
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")

            content_div = soup.find("div", class_="prp-pages-output")
            if content_div:
                chapter_text = content_div.get_text(separator="\n").strip()
            else:
                chapter_text = "No content found."

            screenshot_path = "chaptertesting.png"
            page.screenshot(path=screenshot_path)

            return {
                "content": chapter_text,
                "screenshot_path": os.path.abspath(screenshot_path)
            }

        except Exception as e:
            return {"error": str(e)}

        finally:
            if browser:
                browser.close()





