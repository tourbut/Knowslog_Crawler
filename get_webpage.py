from duckduckgo_search import DDGS
from bs4 import BeautifulSoup, Tag

import requests

def get_dom(url,ssl_verify=False,headers={'User-Agent': 'Mozilla/5.0'}):
    response = requests.get(url, verify=ssl_verify,headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def get_contents(dom):
    parsed_post = []
    
    for node in dom.children:
        content = parse_dom(node)
        if content:
            parsed_post.append(content)
    
    return '\n'.join(parsed_post)

def parse_dom(node):
    parsed_content = []

    if isinstance(node, Tag):
        #print(node.name)
        if node.name in ["script", "style",'html','meta','head','body','div','main','figure','header','article']:
            for child in node.children:
                child_content = parse_dom(child)
                if child_content:
                    parsed_content.append(child_content)
        elif node.name == "link":
            href = node.get('href')
            if href and href.startswith("http"):
                parsed_content.append(f"[Link]({href.strip()})\n")
        elif node.name == "img":
            src = node.get('src')
            if src:
                parsed_content.append(f"![Image]({src.strip()})\n")
        else:
            parsed_content.append(node.text.replace('\n',' ').strip())
    
    if parsed_content:
        return '\n'.join(parsed_content)
    else:
        return None

suggestions = DDGS().suggestions("Latest AI News",region="us-en")
#print(suggestions)
results = DDGS().news(keywords=f"{suggestions[0]['phrase']} -site:msn.com", 
                      region="us-en",
                      safesearch="moderate", 
                      timelimit="d", 
                      max_results=20)

#print(results)
url = 'https://medium.com/towards-artificial-intelligence/extractthinker-ai-document-intelligence-with-llms-72cbce1890ef'
dom = get_dom(url)
contents = get_contents(dom)
print(contents)