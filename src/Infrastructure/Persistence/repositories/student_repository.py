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
    
    def get_all(self):
        return self.db.query(StudentModel).all()
    
    def add_attendance(self, attendance_model:AttendanceModel):
        # burada doğrudan veritabanı modelini alıyoruz çünkü alt yapıyı domaindeki Attendance üzerinden kuracağız.
        self.db.add(attendance_model)
        self.db.commit()
        self.db.refresh(attendance_model)
        return attendance_model
    
