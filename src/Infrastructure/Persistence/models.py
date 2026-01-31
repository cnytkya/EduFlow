from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.Infrastructure.Persistence.db_manager import Base
import datetime

class StudentModel(Base):
    __tablename__ = "students" # sql server daki tablonun ismi olacak.
    id = Column(Integer,primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    student_number = Column(String(20), unique=True, nullable=False)
    
    # Takip alanları
    #Takip alanları(mantık katmanı için)
    absenteeism_count = Column(Integer,default=0)
    is_eligible_for_certificate = Column(Boolean,default=False)
    instructor_override = Column(Boolean,default=False) # eğitmen müdahale etti mi?
    
    # İlişki: Bir öğrencinin birden çok yoklaması olabilir.
    attendance = relationship("AttendanceModel", back_populates="student")
    
class AttendanceModel(Base):
    __tablename__ = "attendance"
    id = Column(Integer,primary_key=True, index = True)
    student_id = Column(Integer,ForeignKey("students.id"))
    status = Column(String(20), nullable=False) # Geldi, Gelmedi
    date = Column(DateTime, default=datetime.datetime.utcnow)
    
    #ilişki: bu yoklama kaydı hangi öğrenciye ait?
    student = relationship("StudentModel", back_populates="attendance")