# öğrenci nesnesi oluşturulacak.

class Student:
    def __init__(self, id, first_name, last_name, student_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        
        #Takip alanları(mantık katmanı için)
        self.absenteeism_count = 0 #Toplam devamsızlık.
        self.is_eligible_for_certificate = False # Sertifika durumu: default false(başlangıçta durum belli değil)
        self.instructor_override = False # eğitmen müdahale etti mi?
        self.status_note = "" #Eğitmen notu
        
    def check_certificate_status(self, max_absenteeism=5):
            """
            sertifika durumunu otomatik kontrol edecek. Eğer eğitmen müdahale etmediyse sistem karar verecek.
            """
            if not self.instructor_override: # eğitmenin müdahelesi olmadan, tüm aşamaları öğrenci başarıyla geçtiyse sertifika alabilsin.
                if self.absenteeism_count <= max_absenteeism: # eğer öğrencinin devamsılık count'u 5 veya 5 e eşit ise sertifika alabilsin.
                    self.is_eligible_for_certificate = True
                else:
                   self.is_eligible_for_certificate = False
            return self.is_eligible_for_certificate
        
    def add_attendance(self, max_absenteeism=5):
        """Devamsızlığı bir artırır ve sertifika durumunu günceller."""
        self.absenteeism_count += 1
        self.check_certificate_status(max_absenteeism)    
                    
        
        
        