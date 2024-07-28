class SeatsNotExist(Exception):
    """Jeśli na seans nie ma już miejsc, zgłoś wyjątek."""
    def __init__(self, message="Miejsce nie istnieje!"):
        self.message = message
        super().__init__(self.message)


class SeatTaken(Exception):
    """Jeśli użytkownik próbuje zarezerwować miejsce, które już jest zarezerwowane, zgłoś wyjątek."""
    def __init__(self, message="Miejsce zarezerwowane, wybierz inne!"):
        self.message = message
        super().__init__(self.message)


class NoSeatsLeft(Exception):
    """Jeśli nie ma już wolnych miejsc, zgłoś wyjątek."""
    def __init__(self, message="Nie ma już wolnych miejsc!"):
        self.message = message
        super().__init__(self.message)


class SameReserv(Exception):
    """Jeśli ten sam użytkownik próbuje ponownie zarezerwować miejsce, zgłoś wyjątek."""
    def __init__(self, message="Możesz zarezerwować tylko jedno miejsce."):
        self.message = message
        super().__init__(self.message)


class ReservationMismatch(Exception):
    """Jeśli próba anulowania rezerwacji nie zgadza się z użytkownikiem, zgłoś wyjątek."""
    def __init__(self, message="Nie można anulować rezerwacji, użytkownik nie zgadza się!"):
        self.message = message
        super().__init__(self.message)


class Cinema:
    def __init__(self, rzad, kolumna):
        self.rzad = rzad
        self.kolumna = kolumna
        self.room = {i: {j: None for j in range(rzad)} for i in range(kolumna)}

    def reserve(self, row, col, guy):
        try:
            if not (0 <= row < self.kolumna and 0 <= col < self.rzad):
                raise SeatsNotExist()
            if self.room[row][col] is not None:
                raise SeatTaken()
            
            # Sprawdź, czy użytkownik nie zarezerwował już miejsca
            if any(guy in rows.values() for rows in self.room.values()):
                raise SameReserv()
            
            self.room[row][col] = guy
            print(f"Miejsce {row}{col} zostało zarezerwowane przez {guy}.")
        
        except (SeatsNotExist, SeatTaken, NoSeatsLeft, SameReserv) as e:
            print(f"Błąd: {e}")

    def cancel_reservation(self, row, col, guy):
        try:
            if not (0 <= row < self.kolumna and 0 <= col < self.rzad):
                raise SeatsNotExist()
            if self.room[row][col] != guy:
                raise ReservationMismatch()
            
            self.room[row][col] = None
            print(f"Rezerwacja miejsca {row}{col} przez {guy} została anulowana.")
        
        except (SeatsNotExist, ReservationMismatch) as e:
            print(f"Błąd: {e}")

    def print_seating(self):
        for row in range(self.rzad):
            for col in range(self.kolumna):
                seat = self.room[col][row]
                if seat is None:
                    print("[wolne]", end=" ")
                else:
                    print(f"[{seat}]", end=" ")
            print()

# Przykładowe użycie
sala = Cinema(3, 3)
sala.reserve(0, 0, 'Trojan')
sala.reserve(1, 0, 'Sc00ra')
sala.reserve(0, 0, 'Sc00ra')
sala.reserve(1, 1, 'Sc00ra')
sala.reserve(2, 0, 'Sc00ra')
sala.reserve(2, 0, 'Lukii')
sala.reserve(1, 2, 'Suto')
sala.reserve(2, 2, 'Salvini')
sala.reserve(2, 2, 'Gruszka')
sala.reserve(3, 0, 'Kubica') # Przykład błędnego miejsca, kolumna 3 nie istnieje

sala.print_seating()

# Anulowanie rezerwacji
sala.cancel_reservation(0, 0, 'Trojan')
sala.cancel_reservation(1, 1, 'Sc00ra')
sala.cancel_reservation(1, 2, 'Suto')
sala.cancel_reservation(2, 2, 'Gruszka') # Przykład błędnej anulacji, inny użytkownik

# Wyświetl miejsca
sala.print_seating()