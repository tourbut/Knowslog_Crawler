from medium_to_markdown.Parser import MediumParser
from bs4 import BeautifulSoup, Tag

import requests

def _get_dom(url,ssl_verify,headers):
    response = requests.get(url, verify=ssl_verify,headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def _get_contents(dom):
    parsed_post = []
    
    for node in dom.children:
        content = _parse_dom(node)
        if content:
            parsed_post.append(content)
    
    return '\n'.join(parsed_post)

def _parse_dom(node):
    parsed_content = []

    if isinstance(node, Tag):
        #print(node.name)
        if node.name in ["script", "style",'html','meta','head','body','div','main','figure','header','article']:
            for child in node.children:
                child_content = _parse_dom(child)
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

def get_webpage(url,ssl_verify=False,headers={'User-Agent': 'Mozilla/5.0'}):
    dom = _get_dom(url,ssl_verify,headers)
    contents = _get_contents(dom) 
    return contents

def get_medium(url, txt_html):
    
    parser = MediumParser(url=url,
                          is_image_download = False,
                          ssl_verify = False)
    
    _rtn = parser.parse(txt_html=txt_html,is_save=False)
    
    return _rtn