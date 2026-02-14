import webview
from src.Application.services.student_service import StudentService

class DesktopApi:
    def __init__(self, student_service: StudentService):
        self.service = student_service
    
    def get_students(self):
        # service'ten iğrencileri al ve JS'in anlayacağı liste formatına çevir.
        students = self.service.get_all_students() # db'den bütün öğrenciler students listesine gömer.
        return [
            {
                "id":student.id,
                "name": f"{student.first_name} {student.last_name}", #db den firstname ve lastname'i alır birleştirir.
                "absenteeism":student.absenteeism_count,
                "eligible": student.is_eligible_for_certificate
            } for student in students
        ]
    
    def mark_attendance(self, student_id):
        # bütün sonuçları göster.
        result = self.service.mark_attendance_and_check_certificate(student_id)
        if isinstance(result, str):
            return {"success":False, "message": result}
        return {
            "success": True,
            "absenteeism":result.absenteeism_count,
            "eligible": result.is_eligible_for_certificate
        }