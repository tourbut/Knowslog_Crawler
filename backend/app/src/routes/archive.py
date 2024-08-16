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

async def translate_archive(in_archive:archive_schema.Archive,
                            in_userllm:archive_schema.GetUserLLM,
                            user_id:int):
    
    chain = translate_chain(api_key=in_userllm.api_key,
                            model=in_userllm.name)
    
    response = chain.invoke({"document":in_archive.content})

    refine = archive_schema.Refine(user_id=user_id,
                                   work_cd="01",
                                   content=response.content,
                                   )
    
    usage = archive_schema.Usage(user_llm_id=in_userllm.id,
                                 input_token=response.usage_metadata['input_tokens'],
                                 output_token=response.usage_metadata['output_tokens'])
    
    return refine,usage

async def summarize_archive(in_archive:archive_schema.Archive,
                            in_userllm:archive_schema.GetUserLLM,
                            user_id:int):
    
    chain = summarize_chain(api_key=in_userllm.api_key,
                            model=in_userllm.name)
    
    response = chain.invoke({"document":in_archive.content})

    refine = archive_schema.Refine(user_id=user_id,
                                   work_cd="02",
                                   content=response.content,
                                   )
    
    usage = archive_schema.Usage(user_llm_id=in_userllm.id,
                                 input_token=response.usage_metadata['input_tokens'],
                                 output_token=response.usage_metadata['output_tokens'])
    
    return refine,usage



@router.post("/run_archiving", response_model=archive_schema.ResponseArchive)
async def run_archiving(*, session: SessionDep_async, current_user: CurrentUser,archive_in: archive_schema.ArchiveURL) -> Any:
    
    url = archive_in.url
    html = archive_in.html
    category = ''
    rst_arch = None
    rst_refine_1 = None
    rst_usage_1 = None
    rst_refine_2 = None
    rst_usage_2 = None
    
    try:
        if archive_in.auto_translate or archive_in.auto_summarize:
            userllm = await archive_crud.get_userllm(session=session,user_id=current_user.id)

        if url.find("medium.com") != -1:
            if (url.startswith("https://") or url.startswith("http://"))== False:
                url="https://" + url
            document,dom = get_medium(url=url,txt_html=None)
            category = "Medium"
        elif html:
            document,dom = get_medium(url=url,txt_html=html)
            category = "Medium"
        else :
            document,dom = get_webpage(url=url)
            category = "Webpage"
            
        arch = archive_schema.Archive(category=category,
                                      language="eng",
                                      title=document['title'],
                                      author=document['author'],
                                      content=document['contents'],
                                      url=url,
                                      dom=dom.prettify())
                    
        if archive_in.auto_translate:
            print("Auto Translate")
            rst_refine_1,rst_usage_1 = await translate_archive(in_archive=arch,in_userllm=userllm,user_id=current_user.id)
            
        if archive_in.auto_summarize:
            print("Auto Summarize")
            rst_refine_2,rst_usage_2 = await summarize_archive(in_archive=arch,in_userllm=userllm,user_id=current_user.id)
        
        rst_arch,rst_refine_1,rst_usage_1,rst_refine_2,rst_usage_2 = await archive_crud.create_archive_refine_usage(session=session,
                                                                                                                    archive=arch,
                                                                                                                    refine_1=rst_refine_1,
                                                                                                                    usage_1=rst_usage_1,
                                                                                                                    refine_2=rst_refine_2,
                                                                                                                    usage_2=rst_usage_2,
                                                                                                                    user_id=current_user.id)
        
        response = archive_schema.ResponseArchive(id=rst_arch.id,
                                                  category=rst_arch.category,
                                                  language=rst_arch.language,
                                                  title=rst_arch.title,
                                                  author=rst_arch.author,
                                                  content=rst_arch.content,
                                                  translate_content=rst_refine_1.content if rst_refine_1 else None,
                                                  translate_input_token=rst_usage_1.input_token if rst_usage_1 else None,
                                                  translate_output_token=rst_usage_1.output_token if rst_usage_1 else None,
                                                  summarize_content=rst_refine_2.content if rst_refine_2 else None,
                                                  summarize_input_token=rst_usage_2.input_token if rst_usage_2 else None,
                                                  summarize_output_token=rst_usage_2.output_token if rst_usage_2 else None,
                                                  url=rst_arch.url,
                                                  dom=rst_arch.dom)
        
            
    except RequestException as e:
        raise HTTPException(status_code=404, detail=f"URL 주소를 확인해주세요.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=f"관리자에게 문의하세요. {e}")
    
    return response


@router.get("/get_archive_list", response_model=List[archive_schema.ArchiveList])
async def get_archive_list(*, session: SessionDep_async, current_user: CurrentUser) -> Any:
    
    rst = await archive_crud.get_archive_list(session=session,user_id=current_user.id)
    
    return rst

@router.get("/get_archive/{archive_id}", response_model=archive_schema.Archive)
async def get_archive(*, session: SessionDep_async, current_user: CurrentUser,archive_id:int) -> Any:
    
    rst = await archive_crud.get_archive(session=session,user_id=current_user.id,archive_id=archive_id)
    
    return rst

@router.put("/delete_archive/")
async def delete_archive(*, session: SessionDep_async, current_user: CurrentUser,in_archive:archive_schema.Update_Archive) -> Any:
    
    in_archive.delete_yn = True
    
    rst = await archive_crud.update_archive(session=session,archive=in_archive)
    
    return rst