# kiosk


# 지갑, 장바구니, 결제
# 메뉴 > 커피류, 빵류 (dictionary)

# while > 입력받기
# 주문하기 > 메뉴판 보여주면서 주문받음 > 장바구니로 상품 추가
# 결제하기 > 장바구니에 있는 상품 가격을 sum > 지갑 - 장바구니 상품 가격 sum > 장바구니 초기화

# bills는 밑에 장바구니는 위에

# 오류: 주문 -> 할인쿠폰 적용 -> 결제 -> 주문 -> 장바구니 초기화 시 할인쿠폰이 다시 3장됨.

# 오류2: 충전 -> 할인쿠폰 적용 -> 결제 시 지갑잔액이 충전 전으로 돌아감.

장바구니 = []

running_outside = True
running_order = True
running_basket = True
running_pay = True
running_inside = True
running_wallet = True
running_discount = True
running_first = True
메뉴판 = {
    "커피류" : ["1. 아메리카노1000", "2. 바닐라라떼2000", "3. 달고나라떼3000"],
    "빵류" : ["4. 소금빵1500", "5. 메론빵2500", "6. 도쿄바나나빵3500"],
    "시크릿메뉴" : ["7. 주인장 시크릿 메뉴"]
}
bills = 0
while running_first:
    지갑 = input("지갑에 얼마가 있습니까?(숫자만 입력): ")
    지갑 = int(지갑)
    잔액 = 지갑
    if 지갑 >= 0:
        print("지갑 잔액: " + str(지갑))
        break
    elif 지갑 < 0:
        print("부채는 입력할 수 없습니다.")
        continue
할인쿠폰 = 3
print("1000원 할인 쿠폰 " + str(할인쿠폰) +"장 남음")
while running_outside:
    print("1.주문하기 or 2.장바구니 or 3.결제하기 or 4.충전(인출)하기 or 5.할인쿠폰 조회 or 6.할인쿠폰 사용")
    choose1 = input("번호를 입력하세요 : ")
    if choose1 == "1":
        while running_order:
            print(메뉴판.values())
            choose2 = input("주문할 메뉴의 번호를 입력하세요 : ")
            if choose2 == "1":
                장바구니.append("아메리카노(1000)")
                print("장바구니에 아메리카노가 담겼습니다.")
                continue
            elif choose2 == "2":
                장바구니.append("바닐라라떼(2000)")
                print("장바구니에 바닐라라떼가 담겼습니다.")
                continue
            elif choose2 == "3":
                장바구니.append("달고나라떼(3000)")
                print("장바구니에 달고나라떼가 담겼습니다.")
                continue
            elif choose2 == "4":
                장바구니.append("소금빵(1500)")
                print("장바구니에 소금빵이 담겼습니다.")
                continue
            elif choose2 == "5":
                장바구니.append("메론빵(2500)")
                print("장바구니에 메론빵이 담겼습니다.")
                continue
            elif choose2 == "6":
                장바구니.append("도쿄바나나빵(3500)")
                print("장바구니에 도쿄바나나빵이 담겼습니다.")
                continue
            elif choose2 == "7":
                장바구니.append("나연이의시크릿슈크림라떼(10000)")
                print("축하드립니다! 우리 가게의 시크릿 메뉴가 장바구니에 담겼습니다.")
                continue
            elif choose2 == "나가기":
                break
            else:
                print("잘못 입력하심요.")
                continue
        if "아메리카노(1000)" in 장바구니:
            a = 1000 * 장바구니.count("아메리카노(1000)")
        else:
            a = 0
        if "바닐라라떼(2000)" in 장바구니:
            b = 2000 * 장바구니.count("바닐라라떼(2000)")
        else:
            b = 0
        if "달고나라떼(3000)" in 장바구니:
            c = 3000 * 장바구니.count("달고나라떼(3000)")
        else:
            c = 0
        if "소금빵(1500)" in 장바구니:
            d = 1500 * 장바구니.count("소금빵(1500)")
        else:
            d = 0
        if "메론빵(2500)" in 장바구니:
            e = 2500 * 장바구니.count("메론빵(2500)")
        else:
            e = 0
        if "도쿄바나나빵(3500)" in 장바구니:
            f = 3500 * 장바구니.count("도쿄바나나빵(3500)")
        else:
            f = 0
        if "나연이의시크릿슈크림라떼(10000)" in 장바구니:
            g = 10000 * 장바구니.count("나연이의시크릿슈크림라떼(10000)")
        else:
            g = 0
        bills = a+b+c+d+e+f+g
    elif choose1 == "2":
        print(장바구니)
        print("결제할 금액: " + str(bills) + "원")
        while running_basket:
            choose3 = input("장바구니 초기화? 예(1)/아니오(2): ")
            if choose3 == "1":
                장바구니.clear()
                print("장바구니가 초기화 되었습니다.")
                할인쿠폰 = 결제후할인쿠폰
                if "아메리카노(1000)" in 장바구니:
                    a = 1000 * 장바구니.count("아메리카노(1000)")
                else:
                    a = 0
                if "바닐라라떼(2000)" in 장바구니:
                    b = 2000 * 장바구니.count("바닐라라떼(2000)")
                else:
                    b = 0
                if "달고나라떼(3000)" in 장바구니:
                    c = 3000 * 장바구니.count("달고나라떼(3000)")
                else:
                    c = 0
                if "소금빵(1500)" in 장바구니:
                    d = 1500 * 장바구니.count("소금빵(1500)")
                else:
                    d = 0
                if "메론빵(2500)" in 장바구니:
                    e = 2500 * 장바구니.count("메론빵(2500)")
                else:
                    e = 0
                if "도쿄바나나빵(3500)" in 장바구니:
                    f = 3500 * 장바구니.count("도쿄바나나빵(3500)")
                else:
                    f = 0
                if "나연이의시크릿슈크림라떼(10000)" in 장바구니:
                    g = 10000 * 장바구니.count("나연이의시크릿슈크림라떼(10000)")
                else:
                    g = 0
                bills = a+b+c+d+e+f+g
                break
            elif choose3 == "2":
                break
            else:
                print("잘못 입력하심요.")
                continue
    elif choose1 == "3":
        while running_pay:
            print("결제할 금액: " + str(bills) + "원")
            잔액 = 지갑 - bills
            print("지갑 잔액: " + str(잔액) + "원")
            choose4 = input("결제하실? 예(1)/아니오(2): ")
            if choose4 == "1":
                if 잔액 < 0:
                    print("돈이 " + str(-잔액) + "원 부족합니다")
                    break
                elif bills == 0:
                    print("결제할 금액이 없습니다.")
                    장바구니.clear()
                    break
                else:
                    print(str(장바구니) + " 상품이 결제됩니다.")
                    print(str(bills) + "원 결제 되었습니다.")
                    print("지갑 잔액: " + str(잔액) + "원")
                    지갑 = 잔액
                    결제후할인쿠폰 = 할인쿠폰
                    print("잔여 할인쿠폰 수: " + str(결제후할인쿠폰) + "장")
                    장바구니.clear()
                    break
            elif choose4 == "2":
                break
            else:
                print("잘못 입력하심요.")
                continue
    elif choose1 == "4":
        while running_wallet:
            choose5 = input("얼마를 충전(인출)하시겠습니까?(숫자만 입력): ")
            if choose5 == "나가기":
                break
            elif int(choose5) > 0:
                지갑 = int(choose5) + 지갑
                print("지갑 잔액: " + str(지갑) + "원")
                break
            elif int(choose5) == 0:
                print("충전할 금액을 다시 설정해주세요.")
                continue
            elif int(choose5) < 0:
                if int(choose5) + 지갑 >= 0:
                    지갑 = 지갑 + int(choose5)
                    print("지갑 잔액: " + str(지갑) + "원")
                    break
                elif int(choose5) + 지갑 < 0:
                    print("인출하시려는 금액이 잔액보다 큽니다만?")
                    continue
            else:
                print("잘못 입력하심요.")
                continue
    elif choose1 == "6":
        while running_discount:
            choose6 = input("1000원 할인쿠폰을 몇 장 사용하시겠습니까?")
            if "아메리카노(1000)" in 장바구니:
                a = 1000 * 장바구니.count("아메리카노(1000)")
            else:
                a = 0
            if "바닐라라떼(2000)" in 장바구니:
                b = 2000 * 장바구니.count("바닐라라떼(2000)")
            else:
                b = 0
            if "달고나라떼(3000)" in 장바구니:
                c = 3000 * 장바구니.count("달고나라떼(3000)")
            else:
                c = 0
            if "소금빵(1500)" in 장바구니:
                d = 1500 * 장바구니.count("소금빵(1500)")
            else:
                d = 0
            if "메론빵(2500)" in 장바구니:
                e = 2500 * 장바구니.count("메론빵(2500)")
            else:
                e = 0
            if "도쿄바나나빵(3500)" in 장바구니:
                f = 3500 * 장바구니.count("도쿄바나나빵(3500)")
            else:
                f = 0
            if "나연이의시크릿슈크림라떼(10000)" in 장바구니:
                g = 10000 * 장바구니.count("나연이의시크릿슈크림라떼(10000)")
            else:
                g = 0
            bills = a+b+c+d+e+f+g
            if choose6 == "나가기":
                break
            elif choose6 == str(1):
                if 할인쿠폰 >= 1:
                    if bills < 1000:
                        print("결제 금액보다 할인 금액이 더 큽니다.")
                        continue
                    else:
                        bills = bills - 1000
                        할인쿠폰 = 할인쿠폰 - 1
                        print("할인쿠폰 1장이 적용되었습니다.")
                        print("잔여 할인쿠폰 수: " + str(할인쿠폰) + "장")
                        break
                else:
                    print("할인쿠폰이 부족합니다만?")
                    continue
            elif choose6 == str(2):
                if 할인쿠폰 >= 2:
                    if bills < 2000:
                        print("결제 금액보다 할인 금액이 더 큽니다.")
                        continue
                    else:
                        bills = bills - 2000
                        할인쿠폰 = 할인쿠폰 - 2
                        print("할인쿠폰 2장이 적용되었습니다.")
                        print("잔여 할인쿠폰 수: " + str(할인쿠폰) + "장")
                        break
                else:
                    print("할인쿠폰이 부족합니다만?")
                break
            elif choose6 == str(3):
                if 할인쿠폰 == 3:
                    if bills < 3000:
                        print("결제 금액보다 할인 금액이 더 큽니다.")
                        continue
                    else:
                        bills = bills - 3000
                        할인쿠폰 = 할인쿠폰 - 3
                        print("할인쿠폰 3장이 적용되었습니다.")
                        print("잔여 할인쿠폰 수: " + str(할인쿠폰) + "장")
                        break
                else:
                    print("할인쿠폰이 부족합니다만?")
                    break
            elif int(choose6) >= 4:
                print("할인쿠폰이 부족합니다만?")
                continue
            elif int(choose6) <= 0:
                print("할인쿠폰을 1 이상 입력 바랍니다.")
                continue
            else:
                print("잘못 입력하심요.")
                continue
    elif choose1 == "5":
        print("현재 " + str(할인쿠폰) + "장의 할인쿠폰이 남았습니다.")
        continue
    else:
        print("잘못 입력하심요.")