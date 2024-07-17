from db.crud import *
from db.schemas import ArchiveCreate
from db.deps import SessionDep
from crawler import get_webpage, get_medium
from llms.llm_model import create_chain
from llms.prompt import get_translate_prompt, get_summary_prompt

if __name__ == "__main__":
    
    url="https://medium.com/@nageshmashette32/multi-vector-retriever-for-rag-on-tables-text-and-images-f0cb39ff8d85"
    document = get_medium(url=url,txt_html=None)
    print(document)
    sess = SessionDep()
    
    arch = ArchiveCreate(category="Medium",
                         collect_ymd="20240711",
                         language="kr",
                        title=document['title'],
                        author=document['author'],
                        content=document['contents'],
                        url=document['url'])
    
    #create_archive(session=sess, archive_create=arch)
        
    