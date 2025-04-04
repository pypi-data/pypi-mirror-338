from scraipe.classes import IScraper, ScrapeResult
import requests
from bs4 import BeautifulSoup
from telethon import TelegramClient
import re
from scraipe.async_classes import AsyncScraperBase
from scraipe.async_util import AsyncManager

class TelegramScraper(AsyncScraperBase):
    """A scraper that uses the telethon library to pull the contents of telegram messages."""
    client: TelegramClient
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    def __init__(self, name: str, api_id: str, api_hash: str, phone_number: str):
        self.client = TelegramClient(name, api_id, api_hash)  # Assign to self.client
        self.client.start(phone_number)
        
    async def _get_telegram_content(self, chat_name:str, message_id:int):
        AsyncManager.disable_multithreading()
        await self.client.connect()
        # Search for entity
        try:
            entity = await self.client.get_entity(chat_name)
        except Exception as e:
            raise Exception(f"Failed to get entity for {chat_name}: {e}")
        
        # Check if entity is restricted/unaccessible
        if entity.restricted:
            raise Exception(f"Entity {chat_name} is restricted.")
        
        # Get the message from entity
        try:
            message = await self.client.get_messages(entity, ids=message_id)  # Fix variable name
        except Exception as e:
            raise Exception(f"Failed to get message {message_id} from {chat_name}: {e}")
        return message.message

    async def async_scrape(self, url: str) -> ScrapeResult:  # Make scrape an async method
        if not url.startswith("https://t.me/"):
            return ScrapeResult(link=url, scrape_success=False, scrape_error=f"URL {url} is not a telegram link.")
        # Extract the username and message id
        match = re.match(r"https://t.me/([^/]+)/(\d+)", url)
        if not match:
            error = f"Failed to extract username and message id from {url}"
            return ScrapeResult(link=url, scrape_success=False, scrape_error=error)
        username, message_id = match.groups()
        try:
            message_id = int(message_id)
        except ValueError:
            raise ValueError(f"Failed to convert message id {message_id} to int.")
        # Run async function
        try:
            content = await self._get_telegram_content(username, message_id)
        except Exception as e:
            return ScrapeResult(link=url, scrape_success=False, scrape_error=f"Failed to scrape {url}. Error: {e}")
        
        return ScrapeResult(link=url, content=content, scrape_success=True)
    
    def disconnect(self):
        self.client.disconnect()