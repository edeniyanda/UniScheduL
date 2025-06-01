class ExamTimeSlot:
    def __init__(self, slot_id, day, week, start_time, end_time):
        self.slot_id = slot_id
        self.day = day
        self.week = week
        self.start_time = start_time  # e.g. "09:00"
        self.end_time = end_time      # e.g. "10:00"

    def __repr__(self):
        return f"Week {self.week} {self.day} {self.start_time}-{self.end_time}"
