from src.Infrastructure.Persistence.db_manager import seedData

if __name__ == "__main__":
    print("Sistem başalatılıyor")
    seedData()
    print("İşlem tamamlandı. Lütfen SQL Server'ı kontrol et.")