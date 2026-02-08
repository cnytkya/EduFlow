from src.Domain.Entities.attendance import Attendance

class AttendanceService:
    def __init__(self, attendance_repo, student_repo):
        # DI: Hem yoklama depocusu hem öğrenci depocusu lazım.
        # Çünkü yoklama alınca öğrencinin devamsızlık sayısını da güncelleyeceğiz.
        self.attendance_repo = attendance_repo
        self.student_repo = student_repo

    def take_attendance(self, student_id: int, status: str):
        """
        Yoklamayı alır ve öğrencinin sertifika durumunu otomatik günceller.
        """
        # 1. Önce öğrenciyi veritabanından bulalım.
        student_model = self.student_repo.get_by_id(student_id)
        if not student_model:
            raise Exception(f"Kanka {student_id} ID'li öğrenci bulunamadı!")

        # 2. Yeni yoklama kaydını Domain kuralına göre oluşturalım.
        new_attendance_domain = Attendance(
            student_id=student_id,
            status=status
        )

        # 3. İŞ MANTIĞI: Eğer öğrenci 'gelmedi' ise devamsızlığını artır.
        if status.lower() == "gelmedi":
            student_model.absenteeism_count += 1
            
            # 4. Domain'deki o meşhur sertifika kontrolünü yapalım.
            # (Modellerinde metodun yoksa burada manuel kontrol yapıyoruz kanka)
            if student_model.absenteeism_count > 5:
                student_model.is_eligible_for_certificate = False
            else:
                student_model.is_eligible_for_certificate = True

        # 5. Kayıtları mühürleyelim (Sırasıyla Yoklama ekle ve Öğrenciyi güncelle)
        self.attendance_repo.add(new_attendance_domain)
        self.student_repo.update(student_model) # student_repo'da update metodu olmalı!

        return student_model