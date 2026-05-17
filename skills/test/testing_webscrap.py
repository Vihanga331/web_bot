import trafilatura


def extract_clean_text(url):
    downloaded = trafilatura.fetch_url(url)

    text = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=False,
        include_images=False,
        include_tables=False
    )

    return text


data = extract_clean_text("https://en.wikipedia.org/wiki/Fish")

print(data)

# Write using UTF-8 encoding
with open("hello.md", "w", encoding="utf-8") as file:
    file.write(data or "")