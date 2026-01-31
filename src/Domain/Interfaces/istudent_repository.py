from abc import ABC, abstractmethod

class IstudentRepository(ABC):
    """Öğrenci verileri için bir şablon (sözleşme)"""
    
    @abstractmethod
    def add_student(self, student):
        pass
    
    @abstractmethod
    def get_all_students(self):
        pass
    
    @abstractmethod
    def update_attendance(self, student_id, count):
        pass