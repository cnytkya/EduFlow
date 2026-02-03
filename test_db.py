# from src.Infrastructure.Persistence.db_manager import seedData
from src.Infrastructure.Persistence.db_manager import SessionLocal, seedData
from Infrastructure.Persistence.repositories.student_repository import StudentRepository
from src.Application.services.student_service import StudentService

def run_test():
    db = SessionLocal() # git veritabanının kapısını çal.
    try:
        seedData()
        student_repo = StudentRepository(db)
        student_service = StudentService(student_repo)
        
        print("\n----Yeni Öğrenci Kaydı Başlatılıyor----")
        yeni_ogrenci = student_service.register_new_student(
            first_name="Naziye",
            last_name="Kara",
            student_number="NUM123456"
        )
        print(f"İşlem tamam! {yeni_ogrenci.first_name} veritabanına {yeni_ogrenci.id} ID numarasyla eklendi.")
    except Exception as e:
        print("Bir hata oluştu!", e)

if __name__ == "__main__":
    run_test()