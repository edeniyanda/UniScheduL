class ExamBooking:
    def __init__(self, course, room, time_slot):
        self.course = course
        self.room = room
        self.time_slot = time_slot

    def __repr__(self):
        return (
            f"📘 {self.course.code} – {self.course.title}\n"
            f"   👥 Students: {self.course.num_students} | 🕒 Duration: {self.course.duration_hours}hr\n"
            f"   🏫 Room: {self.room.name} (Capacity: {self.room.capacity})\n"
            f"   📅 Slot: Week {self.time_slot.week} – {self.time_slot.day}, "
            f"{self.time_slot.start_time} to {self.time_slot.end_time}\n"
        )
