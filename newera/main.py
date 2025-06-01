from algoclass.examroom import ExamRoom
from algoclass.examcourse import ExamCourse
from algoclass.examtimeslot import ExamTimeSlot
from algoclass.exambooking import ExamBooking
from datetime import datetime

room_data = [
    {"Venue": "LR16", "Current Seating": 60},
    {"Venue": "EEE CR 1", "Current Seating": 27},
    {"Venue": "EEE CR 2", "Current Seating": 41},
]

course_data = [
    {"Course Code": "GST 212", "Course Title": "Peace and Conflict Resolution", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 1},
    {"Course Code": "LCU-CCS 211", "Course Title": "Character Code and Service", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 1},
    {"Course Code": "LCU-AST 211", "Course Title": "Agriculture Society and Technology", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 1},
    {"Course Code": "GET 212", "Course Title": "Student Workshop Practice", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 3},
    {"Course Code": "GET 216", "Course Title": "Fundamental of Thermodynamics", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 3},
    {"Course Code": "GET 210", "Course Title": "Engineering Mathematics II", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 3},
    {"Course Code": "EEE 212", "Course Title": "Applied Electricity II", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 3},
    {"Course Code": "LCU-EEE 211", "Course Title": "Skill Acquisition in Electrical Wiring Design and Installation", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 1},
    {"Course Code": "LCU-EEE 213", "Course Title": "Skill Acquisition in Computer Network Design and Installation", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 2},
    {"Course Code": "EEE 214", "Course Title": "Electrical Engineering Materials", "Departments Offering": "EEE & MCE", "Number of Students": 23, "Required Number of Hours": 3},
    {"Course Code": "LCU-ICT 311", "Course Title": "Information Technology III", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 2},
    {"Course Code": "LCU-CCS 311", "Course Title": "Character Code and Service", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 1},
    {"Course Code": "FET 316", "Course Title": "Engineering Mathematics II", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "EEE 311", "Course Title": "Digital Electronic Circuits", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "EEE 312", "Course Title": "Circuit Theory II", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "EEE 313", "Course Title": "Computer Aided Design", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "EEE 315", "Course Title": "Electromechanical Devices and Machines II", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "EEE 316", "Course Title": "Measurements and Instrumentation", "Departments Offering": "EEE", "Number of Students": 31, "Required Number of Hours": 3},
    {"Course Code": "FET 511", "Course Title": "Engineering Law", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 2},
    {"Course Code": "GST 411 / LCU-PCC 411", "Course Title": "Poise, Customer Service and Communication Skills", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 1},
    {"Course Code": "LCU-CCS 511", "Course Title": "Character Code and Service", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 1},
    {"Course Code": "EEE 511", "Course Title": "Microcontroller Applications & Embedded Systems", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3},
    {"Course Code": "EEE 512", "Course Title": "Modern Control Engineering", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3},
    {"Course Code": "EEE 513", "Course Title": "Power Electronics and Devices", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3},
    {"Course Code": "EEE 514", "Course Title": "Use of Engr. Software Packages", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3},
    {"Course Code": "EEE 534", "Course Title": "Power Systems Engineering", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3},
    {"Course Code": "EEE 536", "Course Title": "Renewable Energy Systems", "Departments Offering": "EEE", "Number of Students": 15, "Required Number of Hours": 3}
]

available_time_slot = [
    ExamTimeSlot(1, "Monday", 1, "09:00", "10:00"),
    ExamTimeSlot(2, "Monday", 1, "09:00", "11:00"),
    ExamTimeSlot(3, "Monday", 1, "09:00", "12:00"),
    ExamTimeSlot(4, "Monday", 1, "13:00", "14:00"),
    ExamTimeSlot(5, "Monday", 1, "13:00", "15:00"),
    ExamTimeSlot(6, "Monday", 1, "13:00", "16:00"),
    ExamTimeSlot(7, "Tuesday", 1, "09:00", "10:00"),
    ExamTimeSlot(8, "Tuesday", 1, "09:00", "11:00"),
    ExamTimeSlot(9, "Tuesday", 1, "09:00", "12:00"),
    ExamTimeSlot(10, "Tuesday", 1, "13:00", "14:00"),
    ExamTimeSlot(11, "Tuesday", 1, "13:00", "15:00"),
    ExamTimeSlot(12, "Tuesday", 1, "13:00", "16:00"),
    ExamTimeSlot(13, "Wednesday", 1, "09:00", "10:00"),
    ExamTimeSlot(14, "Wednesday", 1, "09:00", "11:00"),
    ExamTimeSlot(15, "Wednesday", 1, "09:00", "12:00"),
    ExamTimeSlot(16, "Wednesday", 1, "13:00", "14:00"),
    ExamTimeSlot(17, "Wednesday", 1, "13:00", "15:00"),
    ExamTimeSlot(18, "Wednesday", 1, "13:00", "16:00"),
    ExamTimeSlot(19, "Thursday", 1, "09:00", "10:00"),
    ExamTimeSlot(20, "Thursday", 1, "09:00", "11:00"),
    ExamTimeSlot(21, "Thursday", 1, "09:00", "12:00"),
    ExamTimeSlot(22, "Thursday", 1, "13:00", "14:00"),
    ExamTimeSlot(23, "Thursday", 1, "13:00", "15:00"),
    ExamTimeSlot(24, "Thursday", 1, "13:00", "16:00"),
    ExamTimeSlot(25, "Friday", 1, "09:00", "10:00"),
    ExamTimeSlot(26, "Friday", 1, "09:00", "11:00"),
    ExamTimeSlot(27, "Friday", 1, "09:00", "12:00"),
    ExamTimeSlot(28, "Friday", 1, "14:00", "15:00"),
    ExamTimeSlot(29, "Friday", 1, "14:00", "16:00"),
    ExamTimeSlot(30, "Monday", 2, "09:00", "10:00"),
    ExamTimeSlot(31, "Monday", 2, "09:00", "11:00"),
    ExamTimeSlot(32, "Monday", 2, "09:00", "12:00"),
    ExamTimeSlot(33, "Monday", 2, "13:00", "14:00"),
    ExamTimeSlot(34, "Monday", 2, "13:00", "15:00"),
    ExamTimeSlot(35, "Monday", 2, "13:00", "16:00"),
    ExamTimeSlot(36, "Tuesday", 2, "09:00", "10:00"),
    ExamTimeSlot(37, "Tuesday", 2, "09:00", "11:00"),
    ExamTimeSlot(38, "Tuesday", 2, "09:00", "12:00"),
    ExamTimeSlot(39, "Tuesday", 2, "13:00", "14:00"),
    ExamTimeSlot(40, "Tuesday", 2, "13:00", "15:00"),
    ExamTimeSlot(41, "Tuesday", 2, "13:00", "16:00"),
    ExamTimeSlot(42, "Wednesday", 2, "09:00", "10:00"),
    ExamTimeSlot(43, "Wednesday", 2, "09:00", "11:00"),
    ExamTimeSlot(44, "Wednesday", 2, "09:00", "12:00"),
    ExamTimeSlot(45, "Wednesday", 2, "13:00", "14:00"),
    ExamTimeSlot(46, "Wednesday", 2, "13:00", "15:00"),
    ExamTimeSlot(47, "Wednesday", 2, "13:00", "16:00"),
    ExamTimeSlot(48, "Thursday", 2, "09:00", "10:00"),
    ExamTimeSlot(49, "Thursday", 2, "09:00", "11:00"),
    ExamTimeSlot(50, "Thursday", 2, "09:00", "12:00"),
    ExamTimeSlot(51, "Thursday", 2, "13:00", "14:00"),
    ExamTimeSlot(52, "Thursday", 2, "13:00", "15:00"),
    ExamTimeSlot(53, "Thursday", 2, "13:00", "16:00"),
    ExamTimeSlot(54, "Friday", 2, "09:00", "10:00"),
    ExamTimeSlot(55, "Friday", 2, "09:00", "11:00"),
    ExamTimeSlot(56, "Friday", 2, "09:00", "12:00"),
    ExamTimeSlot(57, "Friday", 2, "14:00", "15:00"),
    ExamTimeSlot(58, "Friday", 2, "14:00", "16:00")
]
def load_exam_rooms(data_rows):
    """
    Takes a list of dictionaries or rows representing room data,
    and returns a list of ExamRoom objects.
    """
    rooms = []
    for row in data_rows:
        room = ExamRoom(
            name=row["Venue"],
            capacity=int(row["Current Seating"])
        )
        rooms.append(room)
    return rooms

def load_exam_courses(data_rows):
    """
    Takes a list of dictionaries or rows (e.g., from CSV or manual input),
    and returns a list of ExamCourse objects.
    """
    courses = []
    for row in data_rows:
        course = ExamCourse(
            code=row["Course Code"],
            title=row["Course Title"],
            departments=row["Departments Offering"],
            num_students=int(row["Number of Students"]),
            duration_hours=float(row["Required Number of Hours"])
        )
        courses.append(course)
    return courses



rooms = load_exam_rooms(room_data)
print(rooms)

courses = load_exam_courses(course_data)
print(courses)



def schedule_exams(courses, rooms, time_slots):
    bookings = []
    failed = []
    used_slots = {}  # (room_name, slot_id) => occupied

    for course in courses:
        scheduled = False
        for slot in time_slots:
            # Check if slot duration matches course
            slot_duration = (
                datetime.strptime(slot.end_time, "%H:%M") -
                datetime.strptime(slot.start_time, "%H:%M")
            ).seconds / 3600

            if slot_duration != course.duration_hours:
                continue  # skip mismatched slots

            # Try each room
            for room in rooms:
                if room.capacity >= course.num_students and (room.name, slot.slot_id) not in used_slots:
                    bookings.append(ExamBooking(course, room, slot))
                    used_slots[(room.name, slot.slot_id)] = True
                    scheduled = True
                    break
            if scheduled:
                break

        if not scheduled:
            failed.append(course)

    return bookings, failed


bookings, failed = schedule_exams(courses, rooms, available_time_slot)

for b in bookings:
    print(b)

print("\n❌ Failed to schedule:")
for f in failed:
    print(f"{f.code} ({f.num_students} students, {f.duration_hours}hr)")
