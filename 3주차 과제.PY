
def mija_cut(): 
    try: 
        age = int(input("나이를 입력하세요"))

        if age <=19:
            print("구입할 수 없습니다."), 
        else:
            print("구매 완료") # 
    except ValueError:
        print("Error")

print("저 진짜 성인인데 맥주 한 병 주세요. ")
mija_cut ()
