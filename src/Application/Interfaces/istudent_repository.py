from abc import ABC, abstractmethod

class IStudentRepository(ABC):
    """Öğrenci verileri için bir şablon (sözleşme)"""
    
    @abstractmethod
    def add(self, student):
        pass
    
    @abstractmethod
    def get_all_students(self):
        pass