    @classmethod
    def sum_reservations(cls, instances):
        """모든 ReservationSystem 인스턴스의 예약 수를 합산합니다."""
        total_reservations = 0
        for instance in instances:
            total_reservations += len(instance.reservlist)
        return total_reservations

