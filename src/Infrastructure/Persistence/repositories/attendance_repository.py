from sqlalchemy.orm import Session
from src.Infrastructure.Persistence.models import AttendanceModel
from src.Domain.Entities.attendance import Attendance

class AttendanceRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def add(self, attendance: Attendance):
        # Domain nesnesinden gelen veriyi SQL Model'e (AttendanceModel) çeviriyoruz.
        new_attendance = AttendanceModel(
            student_id = attendance.student_id,
            status = attendance.status,
            date = attendance.date
        )
        self.db.add(new_attendance)
        self.db.commit()
        self.db.refresh(new_attendance)
        return new_attendance

    def get_by_student_id(self, student_id: int):
        # Bir öğrenciye ait tüm yoklama geçmişini getirir.
        return self.db.query(AttendanceModel).filter(AttendanceModel.student_id == student_id).all()