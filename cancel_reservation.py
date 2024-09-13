    def cancel_reservation(self, name, date):
        # 예약 리스트와 입력된 값을 대조 후, 리스트에 있을 경우 삭제
        # 리스트에 없으면 예약 내역이 확인되지 않습니다 출력
        for r in self.reservlist:
            if r["예약자명"] == name and r["예약 일시"] == date:
                self.reservlist.remove(r)
                print(f'{self.branch_name} 예약이 취소되었습니다.')
            else:
                print('예약 내역이 확인되지 않습니다.')

