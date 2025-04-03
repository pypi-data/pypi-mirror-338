from abc import ABC, abstractmethod
from typing import final, List, Dict, Generator, Tuple
import tqdm
from pydantic import BaseModel

@final
class ScrapeResult(BaseModel):
    link:str
    content:str = None
    scrape_success:bool
    scrape_error:str = None
    
    def __str__(self):
        return f"ScrapeResult(link={self.link}, content={self.content}, success={self.scrape_success}, error={self.scrape_error})"
    def __repr__(self):
        return str(self)

@final
class AnalysisResult(BaseModel):
    output:dict = None
    analysis_success:bool
    analysis_error:str = None
    
    def __str__(self):
        return f"AnalysisResult(output={self.output}, success={self.analysis_success}, error={self.analysis_error})"
    def __repr__(self):
        return str(self)

class IScraper(ABC):
    @abstractmethod
    def scrape(self, url:str)->ScrapeResult:
        """Get content from the url"""
        raise NotImplementedError()

    def scrape_multiple(self, urls: List[str]) -> Generator[Tuple[str, ScrapeResult], None, None]:
        """Get content from multiple urls."""
        for url in tqdm.tqdm(urls, desc="Scraping URLs"):
            result = self.scrape(url)
            yield url, result

class IAnalyzer(ABC):
    @abstractmethod
    def analyze(self, content: str) -> AnalysisResult:
        """Analyze the content and return the extracted information as a dict."""
        raise NotImplementedError()
    
    def analyze_multiple(self, contents: Dict[str, str]) -> Generator[Tuple[str, AnalysisResult], None, None]:
        """Analyze multiple contents."""
        for link, content in tqdm.tqdm(contents.items(), desc="Analyzing content"):
            result = self.analyze(content)
            yield link, result
