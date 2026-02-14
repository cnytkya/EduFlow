import webview
from src.Infrastructure.Persistence.repositories.student_repository import StudentRepository
from src.Infrastructure.Persistence.db_manager import SessionLocal
from src.Application.services.student_service import StudentService
from src.Presentation.desktop_app import DesktopApi

def main():
    db = SessionLocal()
    repo = StudentRepository(db)
    service = StudentService(repo)
    api = DesktopApi(service)

    window = webview.create_window(
        'SmartPro Öğrenci Yönetim Sistemi',
        'assets/index.html',
        js_api=api,
        width=900,
        height=600
    )

    webview.start()

if __name__ == "__main__":
    main()