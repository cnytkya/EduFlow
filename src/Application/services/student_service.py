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
        return self.repository.get_all()
    
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
        
        
    