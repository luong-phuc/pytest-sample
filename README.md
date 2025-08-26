# Cấu trúc thư mục :
my_project/
├── .env
├── .gitignore
├── pytest.ini
├── config/
│   ├── __init__.py
│   └── settings.py
├── src/
│   ├── __init__.py
│   └── my_app.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── frontend/
    │   ├── __init__.py
    │   └── test_login_page.py
    └── backend/
        ├── __init__.py
        └── test_api.py

my_project/: Thư mục gốc của dự án.
- .env: File chứa các biến môi trường nhạy cảm như URL, API keys. File này phải được thêm vào .gitignore.
- pytest.ini: File cấu hình cho pytest. Bạn có thể tùy chỉnh cách pytest tìm kiếm và chạy các bài kiểm thử tại đây.
- config/: Thư mục chứa các thiết lập cấu hình của dự án.
    + settings.py: File đọc các biến từ .env và cung cấp chúng cho ứng dụng.
- src/: Thư mục chứa mã nguồn chính của ứng dụng.
    + tests/: Thư mục chứa tất cả các bài kiểm thử.
    + conftest.py: File chứa các fixtures được chia sẻ cho toàn bộ các bài kiểm thử. Đây là nơi bạn sẽ đặt fixture app_settings và có thể là các fixture khác nếu cần.
    + frontend/: Thư mục dành riêng cho các bài kiểm thử frontend, sử dụng Playwright.
    + backend/: Thư mục dành riêng cho các bài kiểm thử backend, ví dụ như kiểm thử API

# Các bước chạy
python3 -m venv venv // tạo môi trường ảo
source venv/Scripts/activate // connect vào môi trường ảo
pip install -r requirements.txt // install thư viện test
playwright install // install thư viện test FE
pytest // chạy test toàn bộ
pytest tests/frontend/ // chạy test FE
pytest tests/frontend/test_google_page.py // Chạy test file riêng
pytest tests/frontend/test_google_page.py -k "test_google_search_page_title"  // chạy cụ thể 1 function
deactivate // để stop môi trường
