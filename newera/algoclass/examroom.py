class ExamRoom:
    def __init__(self, name, capacity):
        """
        Represents an exam venue (room or hall).

        :param name: Room name or code (e.g., 'LR16', 'EEE CR 1')
        :param capacity: Number of seats available for exam candidates
        """
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"ExamRoom(name='{self.name}', capacity={self.capacity})"
