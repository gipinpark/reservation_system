    def add_reservation(self, name, date, people):
        reservation = {"예약자명": name, "예약 일시": date, "인원 수": people}
        self.reservlist.append(reservation)
        print(f'{self.branch_name}에 {name}님의 예약이 추가되었습니다. 예약일: {date}, 인원 수: {people}명')
        ## 해당 지점의 리스트에 예약내역 추가 후 문구 출력
