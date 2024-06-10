import datetime
from sqlalchemy.orm import Session
from database.postgres import get_db
from database.models import User,UserDetail,Archive,Refine
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(username, password, email,
                db: Session=next(get_db())):
    
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username,password=hashed_password,email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_detail(user: User, name, age, interests, json_data,
                       db: Session=next(get_db())):
    
    db_user_detail = UserDetail(user_id=user.id,name=name,age=age,interests=interests,json_data=json_data)
    db.add(db_user_detail)
    db.commit()
    db.refresh(db_user_detail)
    return db_user_detail

def create_archive(category,language,title,author,content,url,
                   db: Session=next(get_db())):
    
    db_archive = Archive(category=category, 
                         collect_ymd=datetime.datetime.now().strftime("%Y%m%d"), 
                         language=language, 
                         title=title, 
                         author=author, 
                         content=content, 
                         url=url,
                         create_date=datetime.datetime.now(),
                         update_date=datetime.datetime.now(),
                         delete_yn=False)
    
    db.add(db_archive)
    db.commit()