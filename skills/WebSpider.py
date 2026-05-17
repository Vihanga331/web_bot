import trafilatura
from pydantic import BaseModel

class WebSpiderInput(BaseModel):
    url: str

    def crawl_data(self):
        downloaded = trafilatura.fetch_url(self.url)

        text = trafilatura.extract(
            downloaded,
            include_links=False,
            include_images=False,
            include_tables=False
        )

        return text

