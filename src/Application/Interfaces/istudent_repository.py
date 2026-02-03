from abc import ABC, abstractmethod
from src.Domain.Entities.student import Student

class IStudentRepository(ABC):
    @abstractmethod
    def add(self, student: Student):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    