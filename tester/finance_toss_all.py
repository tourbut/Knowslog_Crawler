'''
# 토스증권 거래내역서 PDF 파일을 읽어서 CSV 파일로 저장하는 코드

# 설치 패키지
pip install jpype1 tabula-py pandas yfinance requests

'''
import tabula
import pandas as pd
import yfinance as yf
import requests


# PDF 파일 읽기
df_2024 = tabula.read_pdf("tester/전체_거래내역서_20240101_20241115.pdf", pages='all')

#페이지 별로 만들어진 df를 합치기
df_2024 = pd.concat(df_2024)

# 2022년, 2023년, 2024년 데이터를 합치기
df = pd.concat([df_2024])

print(df)

# 거래일자	거래구분	종목명(종목코드)	환율	거래수량	거래대금	단가	수수료 컬럼만 남기기
df = df[['거래일자', '거래구분', '종목명(종목코드)', '환율', '거래수량', '거래대금', '단가', '수수료']]

# Nan 값 제거
df = df.dropna()

# 최종 출력 항목 Symbol	Trade Date	Purchase Price	Quantity	Commission	Type

df_final = pd.DataFrame(columns=['Symbol', 'Trade Date', 'Purchase Price', 'Quantity', 'Commission', 'Type'])


def isin_to_ticker(session,isin):
    search_result = yf.Ticker(isin,session=session)
    return search_result.ticker

# SSL 검증을 비활성화한 세션 생성
session = requests.Session()
session.verify = False


for index, row in df.iterrows():
    
    # 종목명과 ISIN코드가 같이 있는 경우 ISIN로 ticker를 조회
    if row['종목명(종목코드)'].find('(') >= 1:
        stock_name, stock_code = row['종목명(종목코드)'].split('(')
        stock_code = stock_code.replace(')', '')
        
        ticker = isin_to_ticker(session,stock_code)
    
    # ISIN코드 없는 경우는 종목명만 저장
    if row['종목명(종목코드)'].find('(') < 1:
        ticker = row['종목명(종목코드)']
    
    # 가격,수수료는 거래대금을 환율로 나눈 값을 소수점 2자리에서 반올림
    # row['거래대금']에 , 지우기
    
    row['단가'] = row['단가'].replace(',', '')
    row['환율'] = row['환율'].replace(',', '')
    row['수수료'] = row['수수료'].replace(',', '')
    
    purchase_price = round(float(row['단가']) / float(row['환율']), 2)    
    commission = round(float(row['수수료']) / float(row['환율']), 2)
    
    # 거래일자를 '-'로 분리 및 내용의 '.' 제거
    trade_date = row['거래일자'].split('-')
    trade_date[0] = trade_date[0].replace('.', '')
    
    
    Type = 'Buy' if row['거래구분'] == '구매' else 'Sell'
    
    quantity = row['거래수량'] if Type == 'Buy' else row['거래수량'] * -1
    
    new_row = pd.DataFrame({
        'Symbol': [ticker],
        'Trade Date': [trade_date[0]],
        'Purchase Price': [purchase_price],
        'Quantity': [quantity],
        'Commission': [commission],
        'Type': [Type]
    })    
    
    df_final = pd.concat([df_final, new_row], ignore_index=True)
    
    
df_final.to_csv('tester/finance.csv', index=False, encoding='utf-8-sig')

# 종목코드가 없는 종목의 티커는 수기로 변경해야함
# 거래구분이 Sell인 경우 야후 파이낸스 트랜잭션에 Short로 입력되어서 Sell로 변경해야함

# 글로벌엑스 DOW30 커버드콜 ETF	DJIA
# 글로벌엑스 S&P500 커버드 콜 ETF	XYLD
# 글로벌엑스 나스닥100 커버드콜 ETF	QYLD
# 프로셰어즈 VIX 단기선물 ETF	VIXY
# JP모건 커버드콜 옵션 ETF	JEPI
# 아이셰어즈 미국 초장기 국채 ETF	TLT
# 디렉시온 20년 미국채 3배 ETF	TMF
# 아이셰어즈 미국 초장기 국채 바이라이트 전략	TLTW
# 아이셰어즈 미국 1~3년 만기 국채 ETF	SHY

