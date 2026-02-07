from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from src.Infrastructure.Persistence.models import StudentModel 

# sql server bağlantısı connection string
# sunucu adı olacak
# bir de sql server de boş bir veritabanı oluşturulsun. sonra veritabanına migrate ettiğimiz tabloları gönderelim.

CONNECTION_STR = ( # r "(row string) kullanıyoruz ki ters slaşlar(\) hata vermesin"
    r"mssql+pyodbc://@CUNEYT\CUNEYT/EduFlowDB?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes" 
    #sql server de boş bir veritabanı adı
)

# Engine(motor): Veritabanı ile iletişimi sağlayan ana yapı
engine = create_engine(CONNECTION_STR)

# veritabanı üzerine işlem yapabileceğimiz bir fabrika tanımlayıcısı
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base() # tüm veritabanı modellerimiizin miras alacağı ana sınıf.

def seedData(): # bu metot hazır dataları veritabanına set eder.
    """başlangıç dataları yazıyoruz"""
    from src.Infrastructure.Persistence.models import StudentModel 
    
    db = SessionLocal()
    try:
        if db.query(StudentModel).count() == 0:
            print("Veritabanı boş, data set ekleniyor...")
            sample_studendts = [
                StudentModel(first_name = "Maytap", last_name = "Önder", student_number = "20260118"),
                StudentModel(first_name = "Yiğit", last_name = "Salı", student_number = "20260112"),
                StudentModel(first_name = "Furkan", last_name = "Çarşamba", student_number = "20260113"),
                StudentModel(first_name = "Uğur", last_name = "Perşembe", student_number = "20260114")
            ]
            db.add_all(sample_studendts)
            db.commit()
            print("Örnek öğrenciler başarıyla eklendi...")
        else:
            print("Sistemde zaten data var. Seed işlemi başarısız(atlandı.)")
    except Exception as e:
        db.rollback()
        print(f"Hata: {e}")
    finally:
        db.close()