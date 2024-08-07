from typing import Any

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import archive as archive_crud
from app.src.schemas import archive as archive_schema

from app.core.config import settings
from app.src.engine.crawler import get_medium,get_webpage
from datetime import datetime
from requests.exceptions import RequestException

router = APIRouter()


@router.post("/run_archiving", response_model=archive_schema.Archive)
async def run_crawler(*, session: SessionDep_async, current_user: CurrentUser,archive_in: archive_schema.ArchiveURL) -> Any:
    
    url = archive_in.url
    category = ''
    
    try:
        if url.find("medium.com") != -1:
            if (url.startswith("https://") or url.startswith("http://"))== False:
                url="https://"+url
            document,dom = get_medium(url=url,txt_html=None)
            category = "Medium"
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
    
    rst = await archive_crud.create_archive(session=session, archive=arch,user_id=current_user.id)
    
    return rst
