from langchain.agents import create_agent
from langchain.tools import tool
import skills.WebSpider as ws



def save_file(filename: str, content: str) -> str:
    """Save content to a file."""
    with open(filename, 'w') as file:
        file.write(content)
    return f"Content saved to {filename}"




@tool
def web_scraper(url: str) -> str:
    """Scrape the content of a webpage."""
    app = ws.WebSpiderInput(url=url)
    print(f"\n\nWeb scraping completed : {app.crawl_data()}")
    return app.crawl_data() or "No content found."
    

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[web_scraper],
    system_prompt="You are a helpful assistant",
)


result = agent.invoke(
    {"messages": [{"role": "user", "content": input("Enter Your message : ")}]}
)
print(result["messages"][-1].content_blocks)

data = result["messages"][-1].content_blocks
text = data[0].text if data else "No content blocks found."

save_file("chat\\output.txt", text)