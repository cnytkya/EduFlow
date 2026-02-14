from src.Infrastructure.Persistence.db_manager import SessionLocal
from src.Infrastructure.Persistence.repositories.student_repository import StudentRepository
from src.Application.services.student_service import StudentService

def run_attendance_test():
    db = SessionLocal()
    try:
        student_repo = StudentRepository(db)
        student_service = StudentService(student_repo)
        
        student_id = 6
        print(f"\n--- ID: {student_id} için yoklama işleniyor ---")
        
        updated_student = student_service.mark_attendance_and_check_certificate(student_id)
        
        if isinstance(updated_student, str):
            print(updated_student)
        else:
            print(f"Öğrenci: {updated_student.first_name} {updated_student.last_name}")
            print(f"Yeni Devamsızlık: {updated_student.absenteeism_count}")
            print(f"Sertifika Durumu: {'ALABİLİR' if updated_student.is_eligible_for_certificate else 'ALAMAZ'}")
            
    finally:
        db.close()

if __name__ == "__main__":
    run_attendance_test()