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
        if node.name not in ["script", "style",'html','meta','head','body']:
            parsed_content.append(node.text.replace('\n',' ').strip())
        else:
            for child in node.children:
                child_content = parse_dom(child)
                if child_content:
                    parsed_content.append(child_content)
    
    if parsed_content:
        return '\n'.join(parsed_content)
    else:
        return None
    
url=""
dom = get_dom(url)
contents = get_contents(dom)
print(contents)