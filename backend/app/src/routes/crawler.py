from typing import Any

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import crawler as crawler_crud
from app.src.schemas import crawler as crawler_schema

from app.core.config import settings
from app.src.engine.crawler import get_medium,get_webpage
from datetime import datetime


router = APIRouter()


@router.post("/run_crawler", response_model=crawler_schema.Archive)
async def run_crawler(*, session: SessionDep_async, current_user: CurrentUser,user_in: crawler_schema.ArchiveURL) -> Any:
    
    url = user_in.url
    category = ''
    collect_ymd = datetime.now().strftime("%Y%m%d")
    print(current_user.username)
    if url.find("medium.com") != -1:
        document = get_medium(url=url,txt_html=None)
        category = "Medium"
    else :
        document = get_webpage(url=url)
        category = "Webpage"
    
    arch = crawler_schema.Archive(category=category,
                                  collect_ymd=collect_ymd,
                                  language="eng",
                                  title=document['title'],
                                  author=document['author'],
                                  content=document['contents'],
                                  url=url)
    
    rst = await crawler_crud.create_archive(session=session, archive=arch)
    return rst
