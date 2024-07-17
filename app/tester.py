from db.crud import *
from db.schemas import ArchiveCreate
from db.deps import Session,get_db
from engine.crawler import get_webpage, get_medium
from engine.llms.llm_model import create_chain
from engine.llms.prompt import get_translate_prompt, get_summary_prompt

if __name__ == "__main__":
    
    url="https://medium.com/@raunak-jain/orchestrating-agentic-systems-eb945d305083"
    document = get_medium(url=url,txt_html=None)
    #print(document)
    sess=next(get_db())
    arch = ArchiveCreate(category="Medium",
                         collect_ymd="20240711",
                         language="kr",
                        title=document['title'],
                        author=document['author'],
                        content=document['contents'],
                        url=document['url'])
    
    create_archive(session=sess, archive_create=arch)
        
    