## 문제 6. 프랜차이즈 레스토랑 관리 클래스
- 실습 설명

  당신은 여러 지점을 가진 레스토랑 체인의 IT 팀에서 일하며, 각 지점의 예약을 관리하고 중앙에서 예약 현황을 파악할 수 있는 시스템을 개발할 임무를 맡았습니다. 이 시스템은 각 지점의 예약 상황을 관리하고, 고객의 예약 요청을 효과적으로 처리할 수 있는 기능을 제공해야 합니다.

  `ReservationSystem` 클래스는 각 레스토랑 지점의 예약을 관리하며, 다음 기능을 제공해야 합니다:
  - **예약 추가**: 고객이 특정 지점, 예약 일시, 인원 수에 대한 예약을 요청하면 시스템에 추가합니다.
  - **예약 취소**: 고객이 예약을 취소할 수 있으며, 해당 예약을 시스템에서 제거합니다.
  - **예약 조회**: 특정 지점의 모든 예약 상황을 확인할 수 있습니다.
  - **예약 집계**: 모든 지점의 예약 수를 합산합니다. 이 메서드는 모든 `ReservationSystem` 인스턴스의 예약 수를 합산하여 보여줍니다.

- 구현해야 할 메소드
  - `__init__`: 레스토랑 지점의 이름을 초기화하고 예약 리스트를 관리합니다.
  - `add_reservation`: 새로운 예약을 추가합니다. 이 메서드는 예약자 이름, 예약 일시, 인원 수를 받아 저장합니다.
  - `cancel_reservation`: 지정된 예약을 취소하고 리스트에서 제거합니다.
  - `list_reservations`: 현재 지점의 모든 예약 상태를 출력합니다.
  - `sum_reservations`: 주어진 `ReservationSystem` 인스턴스 리스트에서 모든 예약 수를 합산합니다.

- 실습 결과 예시
  ```python
  restaurant1 = ReservationSystem("강남점")
  restaurant2 = ReservationSystem("홍대점")

  restaurant1.add_reservation("홍길동", "2024-05-20", 4)
  restaurant2.add_reservation("김철수", "2024-05-21", 2)

  restaurant1.list_reservations()
  restaurant2.list_reservations()

  total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])
  print(f"전체 레스토랑 예약 수: {total_reservations}")
  ```

    - 예상 출력
  ```
  강남점 예약 목록:
  - 홍길동, 2024-05-20, 4명

  홍대점 예약 목록:
  - 김철수, 2024-05-21, 2명

  전체 레스토랑 예약 수: 2
  ```

- 요구 사항
    - 모든 출력 메시지는 한국어로 제공되어야 합니다.
    - 각 메서드는 적절한 입력 검증과 예외 처리를 포함해야 합니다.
    - `sum_reservations` 클래스 메서드는 모든 지점에서의 예약 수를 효과적으로 합산하여 전체 예약 상태를 중앙에서 확인할 수 있게 합니다.

  
