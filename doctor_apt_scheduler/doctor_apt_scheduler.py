# Implement a Doctor Appointment Scheduler
from collections import defaultdict

class Scheduler:
    def __init__(self):
        self.work_hours = defaultdict(list) # doctor -> intervals
        self.bookings = defaultdict(list) # doctor -> [(start, end, booking_id), ...]
        self.booking_id_to_doctor_lookup = {}
        self.next_id = 1

    def add_hours(self, doctor, start, end):
        if start >= end: raise ValueError("Invalid availability")
        self.work_hours[doctor].append((start, end))

    def is_available(self, doctor, l, r):
        if l >= r: return False

        # check if within one of the work hours
        avail = False
        for wh in self.work_hours[doctor]:
            if wh[0] <= l and r <= wh[1]:
                avail = True
        if not avail: return False

        # check no overlap with existing bookings
        for booking in self.bookings[doctor]:
            no_overlap = (l >= booking[1] or r <= booking[0])
            if not no_overlap:
                return False
        return True

    def book(self, doctor, l, r):
        if not self.is_available(doctor, l, r): return None
        booking_id = self.next_id
        self.next_id += 1
        self.bookings[doctor].append((l, r, booking_id))
        self.booking_id_to_doctor_lookup[booking_id] = doctor
        print('booked with id', booking_id)
        return booking_id

    def cancel(self, booking_id):
        doctor = self.booking_id_to_doctor_lookup.pop(booking_id, None)
        if doctor is None: return False
        self.bookings[doctor] = [
            booking
            for booking in self.bookings[doctor]
            if booking[2] != booking_id
        ]
        print('booking cancelled', booking_id)
        return True


s = Scheduler()

# add doctor's working hours
s.add_hours("Dr. Smith", 9*60, 17*60) # 9am to 5pm

# book an apt
booking_id1 = s.book("Dr. Smith", 540, 570)
assert booking_id1 == 1

# reject overlapping apt
assert s.book("Dr. Smith", 560, 590) is None

# adjacent apt
booking3 = s.book("Dr. Smith", 570, 600)
assert booking3 == 2

# outside working hours
assert s.book("Dr. Smith", 480, 540) is None

# invalid time range
assert s.book("Dr. Smith", 600, 600) is None

# doctor not found
assert s.book("Dr. Jones", 540, 570) is None

# cancel 
assert s.cancel(booking_id1) is True

# cancel twice
assert s.cancel(booking_id1) is False

# rebook cancelled time slot
booking_id4 = s.book("Dr. Smith", 540, 570)
assert booking_id4 == 3

# different doctors
s.add_hours("Dr. Jones", 540, 720)
assert s.book("Dr. Jones", 540, 570) == 4

