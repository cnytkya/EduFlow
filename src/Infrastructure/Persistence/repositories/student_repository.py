from sqlalchemy.orm import Session
from src.Infrastructure.Persistence.models import AttendanceModel, StudentModel
from src.Domain.Entities.student import Student
from src.Application.Interfaces.istudent_repository import IStudentRepository

class StudentRepository(IStudentRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def add(self, student: Student):
        # Domain nesnesini model nesnesine çeviriyoruz.
        new_student = StudentModel(
            first_name = student.first_name,
            last_name = student.last_name,
            student_number = student.student_number,
        )
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)
        return new_student
    
    def get_all_students(self):
        return self.db.query(StudentModel).all()
    
    def get_by_id(self, student_id: int):
    # DB Modelini buluyoruz
        return self.db.query(StudentModel).filter(StudentModel.id == student_id).first()

    def update_absenteeism(self, student_id: int, count: int, is_eligible: bool):
        student_model = self.get_by_id(student_id)
        if student_model:
            student_model.absenteeism_count = count
            student_model.is_eligible_for_certificate = is_eligible
            self.db.commit()
            self.db.refresh(student_model)
        return student_model
    
    def add_attendance_record(self, student_id: int, status: str):
        """Attendance tablosuna yeni bir satır ekler."""
        new_record = AttendanceModel(
            student_id = student_id,
            status = status
            # date default olarak utcnow tanımlı olduğu için model onu otomatik olarak halleder.
        )
        self.db.add(new_record)
        self.db.commit()
        return new_record
    

