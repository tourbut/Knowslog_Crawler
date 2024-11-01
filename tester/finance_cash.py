'''
# 토스증권 거래내역서 PDF 파일을 읽어서 CSV 파일로 저장하는 코드

# 설치 패키지
pip install jpype1 tabula-py pandas

'''
import tabula
import pandas as pd


# 입출금 내역 추가
df_cash_2023 = tabula.read_pdf("tester/토스증권_거래내역_달러_20230101_20231231.pdf", pages='all')
df_cash_2024 = tabula.read_pdf("tester/토스증권_거래내역_달러_20240101_20241231.pdf", pages='all')

#페이지 별로 만들어진 df를 합치기
df_cash_2023 = pd.concat(df_cash_2023)
df_cash_2024 = pd.concat(df_cash_2024)

# 2022년, 2023년, 2024년 데이터를 합치기
df = pd.concat([df_cash_2023, df_cash_2024])

# 거래일자	거래구분	종목명(종목코드)	환율	거래수량	거래대금	단가	수수료 컬럼만 남기기
df = df[['거래일자', '거래구분', '종목명(종목코드)', '환율', '거래수량', '거래대금', '단가', '수수료']]

# 거래구분이 '환전외화입금','환전외화출금' 인 경우 종목명을 $$CASH 로 변경
df.loc[df['거래구분'] == '환전외화입금', '종목명(종목코드)'] = '$$CASH'
df.loc[df['거래구분'] == '환전외화출금', '종목명(종목코드)'] = '$$CASH'
df = df.dropna()

#종목명(종목코드)이 '$$CASH' 인 경우만 가져오기
df = df[df['종목명(종목코드)'] == '$$CASH']


df_final = pd.DataFrame(columns=['Symbol', 'Trade Date', 'Quantity', 'Type'])


for index, row in df.iterrows():
    row['거래대금'] = row['거래대금'].replace(',', '')
    row['환율'] = row['환율'].replace(',', '')
    # 거래일자를 '-'로 분리 및 내용의 '.' 제거
    trade_date = row['거래일자'].split('-')
    trade_date[0] = trade_date[0].replace('.', '')
    
    ticker = row['종목명(종목코드)']
    
    Type = 'Deposit' if row['거래구분'] == '환전외화입금' else 'Withdrawal'
    
    quantity = round((float(row['거래대금']) if Type == 'Deposit' else float(row['거래대금']) * -1) / float(row['환율']),2)
    
    new_row = pd.DataFrame({
        'Symbol': [ticker],
        'Trade Date': [trade_date[0]],
        'Quantity': [quantity],
        'Type': [Type]
    })    
    
    df_final = pd.concat([df_final, new_row], ignore_index=True)
    
df_final.to_csv('tester/finance_cash.csv', index=False)