    def list_reservations(self):
        # 예약 목록 리스트에서 값 꺼내와서 출력
        print(f'{self.branch_name} 예약 목록:')
        for i in self.reservlist:
            print(f'- {i["예약자명"]}, {i["예약 일시"]}, {i["인원 수"]}')

