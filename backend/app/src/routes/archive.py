from typing import Any,List

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import archive as archive_crud
from app.src.schemas import archive as archive_schema

from app.core.config import settings
from app.src.engine.crawler import get_medium,get_webpage
from app.src.engine.llms.chain import translate_chain,summarize_chain
from datetime import datetime
from requests.exceptions import RequestException

router = APIRouter()


@router.post("/run_archiving", response_model=archive_schema.ResponseArchive)
async def run_crawler(*, session: SessionDep_async, current_user: CurrentUser,archive_in: archive_schema.ArchiveURL) -> Any:
    
    url = archive_in.url
    html = archive_in.html
    category = ''
    
    try:
        if url.find("medium.com") != -1:
            if (url.startswith("https://") or url.startswith("http://"))== False:
                url="https://"+url
            document,dom = get_medium(url=url,txt_html=None)
            category = "Medium"
        elif html:
            document,dom = get_medium(url=url,txt_html=html)
            category = "Webpage"
        else :
            document,dom = get_webpage(url=url)
            category = "Webpage"
            
    except RequestException as e:
        raise HTTPException(status_code=404, detail=f"URL 주소를 확인해주세요.")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"관리자에게 문의하세요. {e}")
    
    arch = archive_schema.Archive(category=category,
                                  language="eng",
                                  title=document['title'],
                                  author=document['author'],
                                  content=document['contents'],
                                  url=url,
                                  dom=dom.prettify())
    
    if archive_in.auto_translate or archive_in.auto_summarize:
        userllm = await archive_crud.get_userllm(session=session,user_id=current_user.id)
    
        
    rst = await archive_crud.create_archive(session=session, archive=arch,user_id=current_user.id)
    
    if archive_in.auto_translate:
        print("Auto Translate")
        chain = translate_chain(api_key=userllm.api_key,
                                model=userllm.name,)
        response = chain.invoke({"document":arch.content})
        print('content: ',response.content)
        print('usage: ',response.usage_metadata)
        print(response)
        
    if archive_in.auto_summarize:
        print("Auto Summarize")
    
    return rst


@router.get("/get_archive_list", response_model=List[archive_schema.ArchiveList])
async def get_archive_list(*, session: SessionDep_async, current_user: CurrentUser) -> Any:
    
    rst = await archive_crud.get_archive_list(session=session,user_id=current_user.id)
    
    return rst

@router.get("/get_archive/{archive_id}", response_model=archive_schema.Archive)
async def get_archive(*, session: SessionDep_async, current_user: CurrentUser,archive_id:int) -> Any:
    
    rst = await archive_crud.get_archive(session=session,user_id=current_user.id,archive_id=archive_id)
    
    return rst