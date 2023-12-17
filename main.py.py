from tkinter import *

window = Tk()
window.geometry("500x400")

topWindow = Frame(window)
topWindow.grid(row=0, column=0)  #탑프레임 설정, 초기화 버튼을 눌러도 초기화가 안되는 부분

title = Label(topWindow, text='금융상품 추천 프로그램')  #(https://076923.github.io/posts/Python-tkinter-11/) 위젯을 배치하는 법은 Python tkinter 강좌 : 제 11강 - 위젯 배치 : grid에서 학습
title.grid(row=0, column=0, columnspan = 2) #row: 행 위치, column: 열 위치, rowspan: 행 위치 조정, columnspan: 열 위치 조정을 뜻한다


def clearBot(): #바텀 프레임에 있는 그리드를 모두 지우는 함수 설정 / https://www.crocus.co.kr/943
    global title
    mylist = bottomWindow.grid_slaves()
    for i in mylist:
        i.destroy()

bottomWindow = Frame(window)
bottomWindow.grid(row = 2, column=0)

Button(topWindow, text='다른 상품 알고싶다면 이 버튼누르고 재실행!', command = clearBot).grid(row = 111) # clearBot을 실행하는 버튼



def change(a):      #change 라는 사용자 함수를 새롭게 정의했다. 대출일 때, 예금일 때, 적금일 때 각각 나누어 정보를 입력했다.
    clearBot()  
    if a == '대출':   #아래 변수들을 전역변수 처리해 일일히 재정의하지 않게끔 했다.
        global Bank_list
        global personal_credit
        global personal_limit
        global personal_time
        global personal_bank
        
        #(은행이름, 금융상품명, 최저 신용등급, 최소한도금액(단위: 만원), 최대한도금액, 최소 기간(단위: 월), 최대 기간, 금리, 상환 방법(원금균등 1, 원리금균등 2, 만기일시 3), 하이퍼링크, 최고신용 기본 1등급)

        BankGM1 = banking_loan('국민은행', '새희망 홀씨2', 10, 0, 3000, 12, 84, 6.76, 2, "https://obank1.kbstar.com/quics?page=C019478&cc=b061479:b061589&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=LN000086&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00019&prcode=LN000086#loading",최고신용=6)
        BankGM2 = banking_loan('국민은행', '햇살론17', 10, 70, 700, 36, 60, 17.9, 2, "https://obank1.kbstar.com/quics?page=C019478&cc=b061479:b061589&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=LN000343&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00019&prcode=LN000343", 최고신용=6)
        BankGM3 = banking_loan('국민은행', '대학생청년 햇살론', 10, 0, 111111, 0, 111, 111, 3, "https://obank1.kbstar.com/quics?page=C019478&cc=b061479:b061589&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=LN000140&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00019&prcode=LN000140")
      
        BankWR1 = banking_loan('우리은행', '비상금 대출', 6, 0, 300, 12, 12, 1.41, 3, "https://spot.wooribank.com/pot/Dream?withyou=POLON0052&PRD_CD=P020006123&PRD_YN=Y&cc=c010528%3Ac010531%3Bc012425%3Ac012399")
        BankWR2 = banking_loan('우리은행', '희망드림 소액대출', 8, 100, 1000, 0, 36, 7.54, 2, "https://spot.wooribank.com/pot/Dream?withyou=POLON0052&PRD_CD=P020000056&PRD_YN=Y&cc=c010528%3Ac010531%3Bc012425%3Ac012399")
       
        BankHN1 = banking_loan('하나은행', '이지페이론', 10, 50, 300, 0, 36, 5.154, 2, "https://www.kebhana.com/cont/mall/mall08/mall0802/mall080204/1452023_115200.jsp?_menuNo=98786")
       
        BankKU1 = banking_loan('기업은행', '대학생청년 햇살론', 10, 50, 1200, 0, 180, 5.4, 2, "https://mybank.ibk.co.kr/uib/jsp/guest/ntr/ntr70/ntr7015/PNTR701500_i2.jsp?lncd=02&grcd=21&tmcd=201&pdcd=0165&wvcd=***********&i_trns_biz_kncd=IBK%EB%8C%80%ED%95%99%EC%83%9D%E3%83%BB%EC%B2%AD%EB%85%84%ED%96%87%EC%82%B4%EB%A1%A0")

        BankNH1 = banking_loan('농협은행', '새희망 홀씨2', 10, 100, 3000, 0, 60, 1.2, 2, "https://smartmarket.nonghyup.com/servlet/SFSL0120R.view",최고신용=6)
        
        BankSH1 = banking_loan('수협은행', 'Sh 새희망홀씨2', 10, 100, 3000, 0, 120, 1.59, 2, "https://www.suhyup-bank.com/")
        BankSH2 = banking_loan('수협은행', 'Sh 사잇돌중금리', 7, 0, 2000, 0, 60, 1.59, 1, "https://www.suhyup-bank.com/")

        BankKJ1 = banking_loan('광주은행', 'KJB 새희망홀씨2', 10, 100, 3000, 0, 60, 5.77, 2, "https://pib.kjbank.com/ib20/mnu/BPB0000000001")      
                
        Bank_list = [BankGM1, BankGM2, BankGM3, BankWR1, BankWR2, BankHN1, BankKU1, BankNH1,BankSH1,BankSH2, BankKJ1]
        #대출, 예금, 적금 금융상품 자료조사 2019/11/24 기준


        personal_credit = IntVar()      #정수를 입력해야 하므로 IntVar를 사용
        personal_credit_label = Label(bottomWindow, text='본인의 신용등급 입력 (1등급~10등급): ')
        personal_credit_entry = Entry(bottomWindow, textvariable=personal_credit)
        personal_credit_label.grid(row=2, column=0, columnspan=2) 
        personal_credit_entry.grid(row=2, column=2, columnspan=2)

        personal_limit = IntVar()
        personal_limit_label = Label(bottomWindow, text='대출할 금액 입력 (단위:만원): ') 
        personal_limit_entry = Entry(bottomWindow, textvariable=personal_limit)
        personal_limit_label.grid(row=3, column=0, columnspan=2)
        personal_limit_entry.grid(row=3, column=2, columnspan=2)

        personal_time = IntVar()
        personal_time_label = Label(bottomWindow, text='가능한 상환기간 입력 (단위:개월): ')
        personal_time_entry = Entry(bottomWindow, textvariable=personal_time)
        personal_time_label.grid(row=4, column=0, columnspan=2)
        personal_time_entry.grid(row=4, column=2, columnspan=2)
        
        Calculate_button = Button(bottomWindow, text='본인에게 최적화된 금융상품 찾기!', command= process ) 
        Calculate_button.grid(row=5, column=1, columnspan=3)

    if a == '예금':       #예금도 대출과 유사한 형식으로 진행하였다
        global DBank_list
        global Dpersonal_period
        global Dpersonal_limit
        global Dpersonal_bank
  
        
        #(은행이름, 금융상품명, 예치기간(단위: 월), 최소한도금액(단위: 만원), 최대한도금액(단위: 만원), 금리, 하이퍼링크):       
        #float('inf') 는 최대 한도 금액에 한도가 존재하지 않을 때 무한으로 설정하기 위해 쓴 것이다
        DBankGM1 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 1, 100, float('inf'),  1.10, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM2 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 3, 100, float('inf'),  1.15, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM3 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 6, 100, float('inf'),  1.20, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM4 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 12, 100, float('inf'),  1.25, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM5 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 24, 100, float('inf'),  1.25, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM6 = Dbanking_loan('국민은행', '국민수퍼정기예금(개인)', 36, 100, float('inf'),  1.30, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000029#loading")
        DBankGM7 = Dbanking_loan('국민은행', 'KB Smart★폰 예금', 1, 100, 3000,  1.15, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000340")
        DBankGM8 = Dbanking_loan('국민은행', 'KB Smart★폰 예금', 3, 100, 3000,  1.25, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000340")
        DBankGM9 = Dbanking_loan('국민은행', 'KB Smart★폰 예금', 6, 100, 3000,  1.35, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000340")
        DBankGM10 = Dbanking_loan('국민은행', 'KB Smart★폰 예금', 12, 100, 3000,  1.45, "https://obank1.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000340")
        DBankGM11 = Dbanking_loan('국민은행', '일반정기예금', 1, 10, float('inf'),0.90  , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
        DBankGM12 = Dbanking_loan('국민은행', '일반정기예금', 3, 10, float('inf'), 0.90 , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
        DBankGM13 = Dbanking_loan('국민은행', '일반정기예금', 6, 10, float('inf'), 1.00 , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
        DBankGM14 = Dbanking_loan('국민은행', '일반정기예금', 12, 10, float('inf'),1.10  , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
        DBankGM15 = Dbanking_loan('국민은행', '일반정기예금', 24, 10, float('inf'),1.15  , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
        DBankGM16 = Dbanking_loan('국민은행', '일반정기예금', 36, 10, float('inf'),1.20  , "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&isNew=N&prcode=DP000014")
    
        DBankSH1 = Dbanking_loan('신한은행', '미래설계 크레바스 연금예금',12, 300, float('inf'), 1.65, "https://bank.shinhan.com/index.jsp#020100000000")
        DBankSH2 = Dbanking_loan('신한은행', '미래설계 크레바스 연금예금', 24, 300, float('inf'), 1.75, "https://bank.shinhan.com/index.jsp#020100000000")
        
        DBankWR1 = Dbanking_loan('우리은행', '우리 SUPER주거래 정기예금(확정금리형)', 6, 100, float('inf'), 1.30, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000103&PRD_CD=P010000103&ALL_GB=ALL&depKind=")
        DBankWR2 = Dbanking_loan('우리은행', '우리 SUPER주거래 정기예금(확정금리형)', 12, 100, float('inf'), 1.50, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000103&PRD_CD=P010000103&ALL_GB=ALL&depKind=")
        DBankWR3 = Dbanking_loan('우리은행', 'WON 예금', 1, 100, float('inf'), 0.50, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR4 = Dbanking_loan('우리은행', 'WON 예금', 3, 100, float('inf'), 0.60, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR5 = Dbanking_loan('우리은행', 'WON 예금', 6, 100, float('inf'), 0.75, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR6 = Dbanking_loan('우리은행', 'WON 예금', 12, 100, float('inf'), 0.95, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR7 = Dbanking_loan('우리은행', 'WON 예금', 24, 100, float('inf'), 1.00, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR8 = Dbanking_loan('우리은행', 'WON 예금', 36, 100, float('inf'), 1.05, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010002354&PRD_CD=P010002354&ALL_GB=ALL&depKind=")
        DBankWR9 = Dbanking_loan('우리은행', '키위정기예금', 12, 0, float('inf'), 1.45, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000270&PRD_CD=P010000270&ALL_GB=ALL&depKind=")
        DBankWR10 = Dbanking_loan('우리은행', '키위정기예금', 24, 0, float('inf'), 1.45, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000270&PRD_CD=P010000270&ALL_GB=ALL&depKind=")
        DBankWR11 = Dbanking_loan('우리은행', '키위정기예금', 36, 0, float('inf'), 1.55, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PLM_PDCD=P010000270&PRD_CD=P010000270&ALL_GB=ALL&depKind=")

        DBankHN1 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 1, 1, float('inf'),1.0 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN2 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 3, 1, float('inf'), 1.0, "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN3 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 6, 1, float('inf'),1.2 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN4 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 12, 1, float('inf'),1.35 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN5 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 24, 1, float('inf'),1.4 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN6 = Dbanking_loan('하나은행', 'e-플러스 정기예금', 36, 1, float('inf'),1.5 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419607_115126.jsp#//HanaBank")
        DBankHN7 = Dbanking_loan('하나은행', 'N플러스 정기예금', 6, 1, 3000,1.35 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419658_115126.jsp")
        DBankHN8 = Dbanking_loan('하나은행', 'N플러스 정기예금', 12, 1, 3000,1.5 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419658_115126.jsp")
        DBankHN9 = Dbanking_loan('하나은행', 'N플러스 정기예금', 24, 1, 3000,1.55 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419658_115126.jsp")
        DBankHN10 = Dbanking_loan('하나은행', 'N플러스 정기예금', 36, 1, 3000,1.6 , "https://www.kebhana.com/cont/mall/mall08/mall0801/mall080101/1419658_115126.jsp")
                      
        DBankKU1 = Dbanking_loan('기업은행', 'i-ONE놀이터예금', 3, 100, 3000, 1.20, "https://mybank.ibk.co.kr/uib/jsp/guest/ntr/ntr70/ntr7010/PNTR701000_i2.jsp?lncd=01&grcd=21&tmcd=131&pdcd=0127&wvcd=***********&i_trns_biz_kncd=i-ONE%20%EB%86%80%EC%9D%B4%ED%84%B0%EC%98%88%EA%B8%88#none")
        DBankKU2 = Dbanking_loan('기업은행', 'i-ONE놀이터예금', 6, 100, 3000, 1.25, "https://mybank.ibk.co.kr/uib/jsp/guest/ntr/ntr70/ntr7010/PNTR701000_i2.jsp?lncd=01&grcd=21&tmcd=131&pdcd=0127&wvcd=***********&i_trns_biz_kncd=i-ONE%20%EB%86%80%EC%9D%B4%ED%84%B0%EC%98%88%EA%B8%88#none")
        DBankKU3 = Dbanking_loan('기업은행', 'i-ONE놀이터예금', 12, 100, 3000, 1.40, "https://mybank.ibk.co.kr/uib/jsp/guest/ntr/ntr70/ntr7010/PNTR701000_i2.jsp?lncd=01&grcd=21&tmcd=131&pdcd=0127&wvcd=***********&i_trns_biz_kncd=i-ONE%20%EB%86%80%EC%9D%B4%ED%84%B0%EC%98%88%EA%B8%88#none")

        DBankNH1 = Dbanking_loan('농협은행', '법사랑플러스예금', 1, 100, float('inf'), 1.00, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        DBankNH2 = Dbanking_loan('농협은행', '법사랑플러스예금', 3, 100, float('inf'), 1.05, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        DBankNH3 = Dbanking_loan('농협은행', '법사랑플러스예금', 6, 100, float('inf'), 1.15, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        DBankNH4 = Dbanking_loan('농협은행', '법사랑플러스예금', 12, 100, float('inf'), 1.25, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        DBankNH5 = Dbanking_loan('농협은행', '법사랑플러스예금', 24, 100, float('inf'), 1.30, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        DBankNH6 = Dbanking_loan('농협은행', '법사랑플러스예금', 36, 100, float('inf'), 1.35, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")

        DBankKB1 = Dbanking_loan('케이뱅크', '코드K정기예금', 1, 1, float('inf'), 0.90, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB2 = Dbanking_loan('케이뱅크', '코드K정기예금', 3, 1, float('inf'), 1.00, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB3 = Dbanking_loan('케이뱅크', '코드K정기예금', 6, 1, float('inf'), 1.15, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB4 = Dbanking_loan('케이뱅크', '코드K정기예금', 12, 1, float('inf'), 1.45, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB5 = Dbanking_loan('케이뱅크', '코드K정기예금', 24, 1, float('inf'), 1.50, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB6 = Dbanking_loan('케이뱅크', '코드K정기예금', 36, 1, float('inf'), 1.55, "https://www.kbanknow.com/ib20/mnu/FPMDPT070000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB7 = Dbanking_loan('케이뱅크', '뮤직K정기예금', 12, 300, float('inf'), 1.68, "https://www.kbanknow.com/ib20/mnu/FPMDPT030000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB8 = Dbanking_loan('케이뱅크', '주거래우대 정기예금', 3, 1, float('inf'), 0.80, "https://www.kbanknow.com/ib20/mnu/FPMDPT040000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB9 = Dbanking_loan('케이뱅크', '주거래우대 정기예금', 6, 1, float('inf'), 0.95, "https://www.kbanknow.com/ib20/mnu/FPMDPT040000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB10 = Dbanking_loan('케이뱅크', '주거래우대 정기예금', 12, 1, float('inf'), 1.25, "https://www.kbanknow.com/ib20/mnu/FPMDPT040000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB11 = Dbanking_loan('케이뱅크', '주거래우대 정기예금', 24, 1, float('inf'), 1.30, "https://www.kbanknow.com/ib20/mnu/FPMDPT040000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
        DBankKB12 = Dbanking_loan('케이뱅크', '주거래우대 정기 예금', 36, 1, float('inf'), 1.35, "https://www.kbanknow.com/ib20/mnu/FPMDPT040000?ib20_wc=FPMMAN0000000201V:FPMMAN0000000201V")
   
        DBankBS1 = Dbanking_loan('부산은행', '마이플랜 ISA 정기예금', 3, 1, float('inf'), 1.20, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002#none")
        DBankBS2 = Dbanking_loan('부산은행', '마이플랜 ISA 정기예금', 6, 1, float('inf'), 1.30, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002#none")
        DBankBS3 = Dbanking_loan('부산은행', '마이플랜 ISA 정기예금', 12, 1, float('inf'), 1.52, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002#none")
        DBankBS4 = Dbanking_loan('부산은행', '마이플랜 ISA 정기예금', 24, 1, float('inf'), 1.53, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002#none")
        DBankBS5 = Dbanking_loan('부산은행', '마이플랜 ISA 정기예금', 36, 1, float('inf'), 1.55, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002#none")
        DBankBS6 = Dbanking_loan('부산은행', 'BNK어울림', 12, 300, 100000000, 1.40, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002")
        DBankBS7 = Dbanking_loan('부산은행', 'BNK어울림', 24, 300, 100000000, 1.45, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002")
        DBankBS8 = Dbanking_loan('부산은행', 'BNK어울림', 36, 300, 100000000, 1.50, "https://www.busanbank.co.kr/ib20/mnu/FPMDPO012001002")

        DBankGN1 = Dbanking_loan('경남은행', '투유더정기예금', 6, 100, 300000000, 1.20, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000020177&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        DBankGN2 = Dbanking_loan('경남은행', '투유더정기예금', 12, 100, 300000000, 1.45, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000020177&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        DBankGN3 = Dbanking_loan('경남은행', '투유더정기예금', 24, 100, 300000000, 1.50, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000020177&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        DBankGN4 = Dbanking_loan('경남은행', '마니마니정기예금', 1, 500, float('inf'), 0.70, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000017042&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        DBankGN5 = Dbanking_loan('경남은행', '마니마니정기예금', 3, 500, float('inf'), 0.90, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000017042&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        DBankGN6 = Dbanking_loan('경남은행', '마니마니정기예금', 12, 500, float('inf'), 1.20, "https://www.knbank.co.kr/ib20/mnu/FPMREP020101000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&FNC_PRD_NO=0000017042&FNC_PRD_DIS_CD=01&DUP_CHK=N&ib20_redirect_org_mnu=FPMCOM990000000")
        

        DBank_list=[DBankGM1, DBankGM2, DBankGM3, DBankGM4, DBankGM5, DBankGM6, DBankGM7, DBankGM8, DBankGM9, DBankGM10, DBankGM11, DBankGM12, DBankGM13, DBankGM14, DBankGM15, DBankGM16,
                    DBankSH1, DBankSH2, 
                    DBankWR1, DBankWR2, DBankWR3, DBankWR4, DBankWR5, DBankWR6, DBankWR7, DBankWR8, DBankWR9,DBankWR10, DBankWR11,
                    DBankHN1, DBankHN2, DBankHN3, DBankHN4, DBankHN5, DBankHN6, DBankHN7, DBankHN8, DBankHN9, DBankHN10, 
                    DBankKU1, DBankKU2, DBankKU3,
                    DBankNH1, DBankNH2, DBankNH3, DBankNH4, DBankNH5, DBankNH6, 
                    DBankKB1, DBankKB2, DBankKB3, DBankKB4, DBankKB5,DBankKB6, DBankKB7, DBankKB8, DBankKB9, DBankKB10, DBankKB11, DBankKB12,
                    DBankBS1, DBankBS2, DBankBS3, DBankBS4, DBankBS5, DBankBS6, DBankBS7, DBankBS8, 
                    DBankGN1, DBankGN2, DBankGN3, DBankGN4, DBankGN5, DBankGN6 ]
   

        Dpersonal_period = IntVar() #개월 수 가 정수이므로 IntVar를 사용
        Dpersonal_period_label = Label(bottomWindow, text='원하는 예치기간 입력(1,3,6,12,24,36 개월 中 택): ') #1개월 이상 3개월 미만은 사용자가 1개월로 입력하도록 설정함, 기타 같음.
        Dpersonal_period_entry = Entry(bottomWindow, textvariable=Dpersonal_period)
        Dpersonal_period_label.grid(row=2, column=0, columnspan=2) 
        Dpersonal_period_entry.grid(row=2, column=2, columnspan=2)

        Dpersonal_limit = IntVar()
        Dpersonal_limit_label = Label(bottomWindow, text='원하는 금액 입력 (단위:만원): ') 
        Dpersonal_limit_entry = Entry(bottomWindow, textvariable=Dpersonal_limit)
        Dpersonal_limit_label.grid(row=3, column=0, columnspan=2)
        Dpersonal_limit_entry.grid(row=3, column=2, columnspan=2)

        
        Calculate_button = Button(bottomWindow, text='본인에게 최적화된 금융상품 찾기!', command= Dprocess ) 
        Calculate_button.grid(row=4, column=1, columnspan=3)



    if a == '적금':
        global IBank_list
        global Ipersonal_period
        global Ipersonal_limit
        global Ipersonal_bank
        
       
        #(은행이름, 금융상품명, 최소 금액(단워: 만원), 최대 금액(단위: 만원), 기간(단위: 개월), 금리, 하이퍼링크):
        #정액적립방식, 만기일시지급, 최저금리 적용(우대금리는 하이퍼링크 타고 자세히)
  
        IBankGM1 = Ibanking_loan('국민은행', 'KB내맘대로적금',1, float('inf'), 6, 1.35, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000821&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000821")
        IBankGM2 = Ibanking_loan('국민은행', 'KB내맘대로적금', 1,float('inf'), 12,1.75, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000821&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000821")
        IBankGM3 = Ibanking_loan('국민은행', 'KB내맘대로적금',1, float('inf'), 24, 1.85, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000821&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000821")
        IBankGM4 = Ibanking_loan('국민은행', 'KB내맘대로적금', 1, float('inf'), 36, 2.05, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000821&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000821")
        IBankGM5 = Ibanking_loan('국민은행', 'KB Smart★폰 적금', 0, 100, 6, 1.2, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000339&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000339")
        IBankGM6 = Ibanking_loan('국민은행', 'KB Smart★폰 적금', 0, 100, 12, 1.6, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000339&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000339")
        IBankGM7 = Ibanking_loan('국민은행', 'KB Smart★폰 적금', 0, 100, 36, 1.9, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000339&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000339")
        IBankGM8 = Ibanking_loan('국민은행', 'KB맑은하늘적금',1, float('inf'), 12, 1.65, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000942&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000942")
        IBankGM9 = Ibanking_loan('국민은행', 'KB맑은하늘적금', 1,float('inf'),24, 1.75, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000942&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000942")
        IBankGM10 = Ibanking_loan('국민은행', 'KB맑은하늘적금', 1,float('inf'),36, 1.85, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000942&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000942")
        IBankGM11 = Ibanking_loan('국민은행', 'KB 1코노미 스마트적금',1,float('inf'), 6, 1.5, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000895&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000895")
        IBankGM12 = Ibanking_loan('국민은행', 'KB 1코노미 스마트적금',1,float('inf'), 12,1.9, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000895&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000895")
        IBankGM13 = Ibanking_loan('국민은행', 'KB 1코노미 스마트적금',1,float('inf'), 24, 2, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000895&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000895")
        IBankGM14 = Ibanking_loan('국민은행', 'KB 1코노미 스마트적금', 1,float('inf'),36, 2.2, "https://obank.kbstar.com/quics?page=C016613&cc=b061496:b061645&%EC%9B%B9%EC%83%81%ED%92%88%EC%BD%94%EB%93%9C=DP000895&%EB%85%B8%EB%93%9C%EC%BD%94%EB%93%9C=00007&prcode=DP000895")
        
        IBankWR1 = Ibanking_loan('우리은행', 'WON적금', 0, 50, 12, 2.4,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&PRD_CD=P010002353&PRD_YN=Y&cc=c007095%3Ac009166%3Bc012263%3Ac012399")
        IBankWR2 = Ibanking_loan('우리은행', '위비꾹적금',0, 30, 6, 1.4,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0021&cc=c007095:c009166&PRD_CD=P010000068")
        IBankWR3 = Ibanking_loan('우리은행', '위비꾹적금', 0, 30, 12, 1.9,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0021&cc=c007095:c009166&PRD_CD=P010000068")
        IBankWR4 = Ibanking_loan('우리은행', '올포미 적금', 1, 300, 6, 1.65, "https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PRD_CD=P010000087&PRD_YN=Y")
        IBankWR5 = Ibanking_loan('우리은행', '올포미 적금',1, 300, 12, 1.75,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PRD_CD=P010000087&PRD_YN=Y")
        IBankWR6 = Ibanking_loan('우리은행', '올포미 적금', 1, 300, 24, 1.8,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PRD_CD=P010000087&PRD_YN=Y")
        IBankWR7 = Ibanking_loan('우리은행', '올포미 적금', 1, 300, 36, 1.85,"https://spot.wooribank.com/pot/Dream?withyou=PODEP0019&cc=c007095:c009166;c012263:c012399&PRD_CD=P010000087&PRD_YN=Y")

        IBankNH1 = Ibanking_loan('농협은행', 'e-금리우대적금', 1, 2000, 12, 1.8, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH2 = Ibanking_loan('농협은행', 'e-금리우대적금', 1, 2000, 24, 1.79, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH3 = Ibanking_loan('농협은행', 'e-금리우대적금', 1, 2000, 36, 1.85, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH4 = Ibanking_loan('농협은행', 'NH주거래우대적금',1, 100, 6, 1.45, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH5 = Ibanking_loan('농협은행', 'NH주거래우대적금',1, 100, 12, 1.5, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH6 = Ibanking_loan('농협은행', 'NH주거래우대적금', 1, 100, 24, 1.55, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")
        IBankNH7 = Ibanking_loan('농협은행', 'NH주거래우대적금', 1, 100, 36, 1.65, "https://smartmarket.nonghyup.com/servlet/SFSD0130R.view")

        IBankSH1 = Ibanking_loan('신한저축은행', 'e-정기적금', 1, float('inf'), 12, 2.4, "https://www.shinhansavings.com/acprd_0001A_02.act")
        IBankSH2 = Ibanking_loan('신한저축은행', 'e-정기적금',1, float('inf'), 24, 2.5, "https://www.shinhansavings.com/acprd_0001A_02.act")
        IBankSH3 = Ibanking_loan('신한저축은행', 'e-정기적금', 1, float('inf'), 36, 2.6, "https://www.shinhansavings.com/acprd_0001A_02.act")

        IBankCT1 = Ibanking_loan('한국씨티은행', '원더풀라이프적금',1,1000, 12, 1.5, "https://www.citibank.co.kr/MndMdtrPrdc0400.act")
        IBankCT2 = Ibanking_loan('한국씨티은행', '원더풀라이프적금',1, 1000, 24, 1.6, "https://www.citibank.co.kr/MndMdtrPrdc0400.act")
        IBankCT3 = Ibanking_loan('한국씨티은행', '원더풀라이프적금',1, 1000, 36, 1.7, "https://www.citibank.co.kr/MndMdtrPrdc0400.act")

        IBankGN1 = Ibanking_loan('경남은행', '투유더자유적금',0, 300, 6, 1.25, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000020178")
        IBankGN2 = Ibanking_loan('경남은행', '투유더자유적금',0, 300, 12, 1.55, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000020178")
        IBankGN4 = Ibanking_loan('경남은행', '투유더자유적금', 0,300, 24, 1.65, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000020178")
        IBankGN3 = Ibanking_loan('경남은행', '건강한둘레길적금', 5,float('inf'), 12, 1.35, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000017027")
        IBankGN5 = Ibanking_loan('경남은행', '건강한둘레길적금', 5, float('inf'), 24, 1.45, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000017027")
        IBankGN6 = Ibanking_loan('경남은행', '건강한둘레길적금', 5, float('inf'), 36, 1.6, "https://www.knbank.co.kr/ib20/mnu/FPMDPT020103000?ib20_wc=FPMDPT110LSTV00M:FPMDPT221DETV00M&ib20_cur_mnu=FPMDPT020103000&ib20_cur_wgt=FPMDPT110LSTV00M&fnc_prd_no=0000017027")

        
        IBank_list=[IBankGM1, IBankGM2, IBankGM3, IBankGM4, IBankGM5, IBankGM6, IBankGM7, IBankGM8, IBankGM9, IBankGM10, IBankGM11,IBankGM12,IBankGM13,IBankGM14,
                    IBankWR1,IBankWR2, IBankWR3, IBankWR4, IBankWR5, IBankWR6, IBankWR7,
                    IBankNH1,IBankNH2,IBankNH3,IBankNH4,IBankNH5,IBankNH6,IBankNH7,
                    IBankSH1,IBankSH2, IBankSH3,
                    IBankCT1, IBankCT2, IBankCT3,
                    IBankGN1, IBankGN2, IBankGN3, IBankGN4, IBankGN5, IBankGN6]


        Ipersonal_period = IntVar() 
        Ipersonal_period_label = Label(bottomWindow, text='원하는 기간 입력(6,12,24,36개월中 택): ')
        Ipersonal_period_entry = Entry(bottomWindow, textvariable=Ipersonal_period)
        Ipersonal_period_label.grid(row=2, column=0, columnspan=2)
        Ipersonal_period_entry.grid(row=2, column=2, columnspan=2)

        Ipersonal_limit = IntVar()
        Ipersonal_limit_label = Label(bottomWindow, text='한 달 동안 적금 할 금액 입력 (단위:만원): ') 
        Ipersonal_limit_entry = Entry(bottomWindow, textvariable=Ipersonal_limit)
        Ipersonal_limit_label.grid(row=3, column=0, columnspan=2)
        Ipersonal_limit_entry.grid(row=3, column=2, columnspan=2)

        
        Calculate_button = Button(bottomWindow, text='본인에게 최적화된 금융상품 찾기!', command= Iprocess ) 
        Calculate_button.grid(row=4, column=1, columnspan=2)


        
        
choice_label = Label(topWindow, text="금융상품:")
choice_label.grid(row=1, column=0)
choice = StringVar()
choice.set('사용할 금융상품 선택')
choice_optionmenu = OptionMenu(topWindow, choice, '대출', '예금', '적금', command=change)
choice_optionmenu.grid(row=1, column=1)


#Magic Method는 미리 정의되어 있는 메서드들을 재정의하여 클래스를 활용할 수 있도록 변경해주는 것이다.
#내장 함수들이 처리하는 연산을 변경해 사용자 정의 클래스나 함수 등을 효율적으로 사용할 수 있다.
#class를 사용하기 위해 Python 강좌 : 제 35강 - 매직 메서드 (1) 를 보고 공부했다.

class banking_loan: #대출
    def __init__(self, 은행이름, 금융상품명, 신용, 최소한도금액, 최대한도금액, 최소상환기간, 최대상환기간, 금리, 금리계산방식, 하이퍼링크, 최고신용=1): #__init__ : 초기화 메서드이다.
                                    #새로운 인스턴스를 만들 때 사용될 인자들을 선언하는 메서드이다.
                                    #할당된 인자들을 선언해서 사용하며, 매개변수를 할당받을 때 동일한 이름에 self를 추가해 동일한 명칭으로 사용한다.
        self.name = 은행이름
        self.goods = 금융상품명
        self.credit = 신용
        self.minlimit = 최소한도금액
        self.maxlimit = 최대한도금액
        self.mintime = 최소상환기간
        self.maxtime = 최대상환기간
        self.interest = 금리
        self.calculate = 금리계산방식
        self.hyperlink = 하이퍼링크
        self.mincredit = 최고신용

    def __repr__(self): #__repr__ : 형식적인 문자열 메서드이다. 
                        #repr()을 호출해 형식적인(official) 문자열 표현에 사용됩니다.
                        #명확한 정보를 담아 활용하며, 문자열 형식으로 반환해야합니다.
        return "%s, %s, %s" %(self.name, self.goods, str(self.interest))
    

class Dbanking_loan: #예금
    def __init__(self, 은행이름, 금융상품명, 예치기간, 최소한도금액, 최대한도금액, 금리, 하이퍼링크): 
        self.Dname = 은행이름
        self.Dgoods = 금융상품명
        self.Dperiod = 예치기간
        self.Dminlimit = 최소한도금액
        self.Dmaxlimit = 최대한도금액
        self.Dinterest = 금리
        self.Dhyperlink = 하이퍼링크

    def __repr__(self):
        return "%s, %s, %s" %(self.Dname, self.Dgoods, str(self.Dinterest))



class Ibanking_loan: #적금
    def __init__(self, 은행이름, 금융상품명, 최소한도금액, 최대한도금액, 기간, 금리, 하이퍼링크):
        self.Iname = 은행이름
        self.Igoods = 금융상품명
        self.Iminlimit = 최소한도금액
        self.Imaxlimit = 최대한도금액
        self.Iperiod = 기간
        self.Iinterest = 금리
        self.Ihyperlink = 하이퍼링크

    def __repr__(self):
        return "%s, %s, %s" %(self.Iname, self.Igoods, str(self.Iinterest))



def process(): #대출
    global personal_time, personal_limit 
    personal_bank = []
    for i in Bank_list:
        if i.credit >= personal_credit.get() >= i.mincredit:
            if i.minlimit <= personal_limit.get() <= i.maxlimit: 
                if i.mintime <= personal_time.get() <= i.maxtime:
                    personal_bank.append(i)

    personal_bank.sort(key=lambda x: x.interest) #lamdba를 사용해 금리 순서대로 정렬 / https://wayhome25.github.io/python/2017/03/07/key-function/
    name_menu = [] #리스트 각각을 초기화하기
    goods_menu = []
    interest_menu = []
    loan_result_menu = []
    hyperlink_menu = []

    name_menu.append(Label(bottomWindow, text="은행명"))#리스트에 Label(bottomWindow, text="은행명")을 추가하는 것이다
    goods_menu.append(Label(bottomWindow, text="금융상품"))
    interest_menu.append(Label(bottomWindow, text="금리"))
    loan_result_menu.append(Label(bottomWindow, text="총 상환금액(단위: 원)"))
    hyperlink_menu.append(Label(bottomWindow, text="셸창의 하이퍼링크를 복사해 자세한 정보를 알아보세요!"))

    name_menu[0].grid(row=6, column=0)  # menu들의 0번째 인덱스에 있는 설명들을 위치하게 하는 그리드
    goods_menu[0].grid(row=6, column=1)
    interest_menu[0].grid(row=6, column=2)
    loan_result_menu[0].grid(row=6, column=3)
    hyperlink_menu[0].grid(row=99, column=0, columnspan=4)


    count= 0
    for index, bank in enumerate(personal_bank): # for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 enumerate 함수를 사용
        count += 1
        if count > 4:
            break
        name_menu.append(Label(bottomWindow, text=str(bank.name)))
        goods_menu.append(Label(bottomWindow, text=str(bank.goods)))
        interest_menu.append(Label(bottomWindow, text=str(bank.interest)))
        loan_result_menu.append(Label(bottomWindow, text=loan_result(bank, personal_limit, personal_time)))

        name_menu[index+1].grid(row=index+7, column=0)
        goods_menu[index+1].grid(row=index+7, column=1)
        interest_menu[index+1].grid(row=index+7, column=2)
        loan_result_menu[index+1].grid(row=index+7, column=3)
   
        print(bank.goods, bank.hyperlink)
      
    if count == 0:
        name_menu.append(Label(bottomWindow, text="해당하는 금용상품이 없습니다 ㅠㅠ"))
        name_menu[1].grid(row=6, column=0, columnspan=5)



def Dprocess(): #예금
    global Dpersonal_period, Dpersonal_limit
    Dpersonal_bank = []
    for i in DBank_list:
        if i.Dperiod == Dpersonal_period.get():
            if i.Dminlimit <= Dpersonal_limit.get() <= i.Dmaxlimit: 
                    Dpersonal_bank.append(i)

    Dpersonal_bank.sort(key=lambda x: x.Dinterest,reverse=True)
    Dname_menu = []
    Dgoods_menu = []
    Dinterest_menu = []
    Dloan_result_menu = []
    Dhyperlink_menu = []

    Dname_menu.append(Label(bottomWindow, text="은행명"))
    Dgoods_menu.append(Label(bottomWindow, text="금융상품"))
    Dinterest_menu.append(Label(bottomWindow, text="금리"))
    Dloan_result_menu.append(Label(bottomWindow, text="총 수령액(단위: 원)"))
    Dhyperlink_menu.append(Label(bottomWindow, text="셸창의 하이퍼링크를 복사해 자세한 정보를 알아보세요!"))

    Dname_menu[0].grid(row=5, column=0)
    Dgoods_menu[0].grid(row=5, column=1)
    Dinterest_menu[0].grid(row=5, column=2)
    Dloan_result_menu[0].grid(row=5, column=3)
    Dhyperlink_menu[0].grid(row=99, column=0, columnspan=4)

    count= 0
    for index, Dbank in enumerate(Dpersonal_bank):
        count += 1
        if count > 4:
            break
        Dname_menu.append(Label(bottomWindow, text=str(Dbank.Dname)))
        Dgoods_menu.append(Label(bottomWindow, text=str(Dbank.Dgoods)))
        Dinterest_menu.append(Label(bottomWindow, text=str(Dbank.Dinterest)))
        Dloan_result_menu.append(Label(bottomWindow, text=Dloan_result(Dbank.Dinterest, Dpersonal_limit, Dpersonal_period)))
        
        Dname_menu[index+1].grid(row=index+7, column=0)
        Dgoods_menu[index+1].grid(row=index+7, column=1)
        Dinterest_menu[index+1].grid(row=index+7, column=2)
        Dloan_result_menu[index+1].grid(row=index+7, column=3)

        print(Dbank.Dgoods, Dbank.Dhyperlink)
        

    if count == 0:
        Dname_menu.append(Label(bottomWindow, text="해당하는 금용상품이 없습니다 ㅠㅠ"))
        Dname_menu[1].grid(row=6, column=0, columnspan=5)

    

def Iprocess(): #적금
    global Ipersonal_period, Ipersonal_limit, Ibank
    Ipersonal_bank = []
    for i in IBank_list:
        if i.Iperiod == Ipersonal_period.get():
            if i.Iminlimit <= Ipersonal_limit.get() <= i.Imaxlimit:
                    Ipersonal_bank.append(i)
                    
  
    Ipersonal_bank.sort(key=lambda x: x.Iinterest,reverse=True)
    Iname_menu = []
    Igoods_menu = []
    Iinterest_menu = []
    Iloan_result_menu = []
    Ihyperlink_menu = []

    Iname_menu.append(Label(bottomWindow, text="은행명"))
    Igoods_menu.append(Label(bottomWindow, text="금융상품"))
    Iinterest_menu.append(Label(bottomWindow, text="금리"))
    Iloan_result_menu.append(Label(bottomWindow, text="총 수령액(단위: 원)"))
    Ihyperlink_menu.append(Label(bottomWindow, text="셸창의 하이퍼링크를 복사해 자세한 정보를 알아보세요!"))

    Iname_menu[0].grid(row=5, column=0)
    Igoods_menu[0].grid(row=5, column=1)
    Iinterest_menu[0].grid(row=5, column=2)
    Iloan_result_menu[0].grid(row=5, column=3)
    Ihyperlink_menu[0].grid(row=99, column=0, columnspan=4)



    count= 0
    for index, Ibank in enumerate(Ipersonal_bank):
        count += 1
        if count > 4:
            break
        Iname_menu.append(Label(bottomWindow, text=str(Ibank.Iname)))
        Igoods_menu.append(Label(bottomWindow, text=str(Ibank.Igoods)))
        Iinterest_menu.append(Label(bottomWindow, text=str(Ibank.Iinterest)))
        Iloan_result_menu.append(Label(bottomWindow, text=Iloan_result(Ibank.Iinterest, Ipersonal_limit, Ipersonal_period)))
       
        Iname_menu[index+1].grid(row=index+7, column=0)
        Igoods_menu[index+1].grid(row=index+7, column=1)
        Iinterest_menu[index+1].grid(row=index+7, column=2)
        Iloan_result_menu[index+1].grid(row=index+7, column=3)

        print(Ibank.Igoods, Ibank.Ihyperlink)
        
    if count == 0:
        Iname_menu.append(Label(bottomWindow, text="해당하는 금용상품이 없습니다 ㅠㅠ"))
        Iname_menu[1].grid(row=6, column=0, columnspan=5)



        
def loan_result(은행, 입력한_돈, 기간): #대출일 때, 상환 방식에 따라 계산하는 함수를 정의한 것이다
    if 은행.calculate == 1: #원금일 때
        result = (입력한_돈.get()*(1+((은행.interest/1200)*((기간.get())+1)/2)))*10000
    elif 은행.calculate == 2: #원리금일 때
        result = (입력한_돈.get()*(기간.get())*(((은행.interest/1200)*((1+(은행.interest/1200))**(기간.get())))/(((1+(은행.interest/1200))**(기간.get()))-1)))*10000
    else:                   #만기일 때
        result = (입력한_돈.get()*(1+(은행.interest/1200))**((기간.get())))*10000 
    return int(result)
                  

def Dloan_result(금리, 입력한_돈, 예치기간): #예금일 때, 금리, 사용자 입력 금액, 사용자 입력 예치 기간을 토대로 총 금액을 계산한 함수이다
    return (입력한_돈.get()*(1+(금리*예치기간.get())/1200))*10000


 
def Iloan_result(금리, 입력한_돈, 기간): #적금일 때, 금리, 사용자 입력 금액, 사용자 입력 적금 기간을 토대로 총 금액을 계산한 함수이다.
    return (입력한_돈.get()*기간.get()+입력한_돈.get()*기간.get()*(기간.get()+1)/2*금리/100/12)*10000



window.mainloop()

