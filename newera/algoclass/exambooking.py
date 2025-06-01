class ExamBooking:
    def __init__(self, course, room, time_slot):
        self.course = course
        self.room = room
        self.time_slot = time_slot

    def __repr__(self):
        return f"{self.course.code} → {self.room.name} @ {self.time_slot}"
