# gerekli malzemeleri tezgahın üzerine koyalım.
from src.Infrastructure.Persistence.repositories.student_repository import StudentRepository
from src.Domain.Entities.student import Student

class StudentService:
    def __init__(self, repository: StudentRepository):
        # DI: Dependency Injection
        # Service veritabanına kendi gitmez, eline bir "repository"(depocu) veririz.
        # o işini depocu üzerinden görür, Böylece yarın depocuyu değiştirsek de service bozulmaz.
        self.repository = repository
    
    def get_all_students(self):
        # Bana bütün öğrencileri getir. ama gelen kayıtlar veritabanı modelidir, dikkat et, biz bu kayıtları UI tarafına temiz bir şekilde gönderelim.
        return self.repository.get_all_students()
    
    def register_new_student(self, first_name: str, last_name:str,student_number:str):
        # register_new_student() method kod bloğu
        # UI'den yeni bir kayıt mı oluşturuldu?
        # Hemen Domain klasöründeki "Student" kuralımıza göre bir nesne oluşturalım. Domain bizim promizin çekirdeği olduğu için ve içindeki her bir model aslında projenin temel yapı taşıdır ve her şeyin üstündedir. Orda yazılan kurallara göre yeni bir nesne üretilebilir. orda yazılan kural haricinde başka bir işlem yapılamaz.
        
        new_student_domain = Student(
            id=None, # ID'yi SQL Server kendi otomatik verecek, biz buna karışamayız.
            first_name = first_name,
            last_name=last_name,
            student_number=student_number
        )
        
        # üretilen nesne hazırsa, depocuya "al bunu güvenli bir şekilde rafa kaldır" diyoruz.
        return self.repository.add(new_student_domain)
    

    def mark_attendance_and_check_certificate(self, student_id: int):
        # 1. Veritabanından modeli çek
        student_model = self.repository.get_by_id(student_id)
        if not student_model:
            return "Öğrenci bulunamadı!"

        # 2. Domain Nesnesine Çevir (İş mantığını çalıştırmak için)
        student_domain = Student(
            id=student_model.id,
            first_name=student_model.first_name,
            last_name=student_model.last_name,
            student_number=student_model.student_number
        )
        student_domain.absenteeism_count = student_model.absenteeism_count
        student_domain.instructor_override = student_model.instructor_override

        # 3. Domain içindeki mantığı çalıştır (DRY)
        student_domain.add_attendance()

        # 4. Güncellenen veriyi DB'ye geri yaz
        return self.repository.update_absenteeism(
            student_id, 
            student_domain.absenteeism_count, 
            student_domain.is_eligible_for_certificate
        )
        
        
    