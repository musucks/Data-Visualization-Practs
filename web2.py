import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_page(url): 
    response = requests.get(url)
    if response.status_code != 200:
        return "Error: ", response.status_code
    soup = BeautifulSoup(response.content, "lxml") 
    
    title = soup.find("h1", id="firstHeading").text 
    paragraphs = soup.find_all("p")
    first_paragraph = paragraphs[0].text if paragraphs else "" 
    second_paragraph = paragraphs[1].text if len(paragraphs) > 1 else "" 
    first_ul = soup.find_all("ul")[0] if soup.find_all("ul") else None 
    bullet_points = []
    
    if first_ul:
        for li in first_ul.find_all("li"): 
            bullet_points.append(li.get_text().strip())
            
        return {"Title": title, 
                "First Paragraph": first_paragraph,
                "Second Paragraph": second_paragraph, 
                "Bullet Points": bullet_points,}
        
url = "https://en.wikipedia.org/wiki/Web_scraping" 
scraped_data = scrape_wikipedia_page(url)

for key, value in scraped_data.items():
    if type(value) == list: print(f"{key}: ") 
for item in value:
    print(f"- {item}")
else:
    print(key, ":", value, end="\n\n")


#pip install beautifulsoup4 requests
#pip install requests beautifulsoup4 lxml#
#python3 -m pip install lxm