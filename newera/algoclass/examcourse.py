class ExamCourse:
    def __init__(self, code, title, departments, num_students, duration_hours):
        """
        Represents a single course to be scheduled for exams.

        :param code: Course Code (e.g., 'EEE 311')
        :param title: Course Title
        :param departments: Departments Offering the Course (e.g., 'EEE & MCE')
        :param num_students: Total number of students taking the course
        :param duration_hours: Duration of the exam in hours (integer or float)
        """
        self.code = code
        self.title = title
        self.departments = departments
        self.num_students = num_students
        self.duration_hours = duration_hours

    def __repr__(self):
        return (
            f"ExamCourse(code='{self.code}', title='{self.title}', "
            f"departments='{self.departments}', num_students={self.num_students}, "
            f"duration_hours={self.duration_hours})"
        )
