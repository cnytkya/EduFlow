from datetime import datetime

class Attendance:
    def __init__(self, student_id, status, date = None):
        self.student_id = student_id
        self.status = status # durum: geldi-gelmedi-izinli-hasta
        self.date = date if date else datetime.now().strftime("%Y-%m-%d") # Tarih girilmesze o anki günü otomatik al.
        
    def __repr__(self):
        return f"<{self.date} - Öğrenci ID: {self.student_id} - Durum: {self.status}>"
        