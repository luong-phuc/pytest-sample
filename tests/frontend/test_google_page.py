from playwright.sync_api import Page

def test_google_search_page_title(page: Page, app_settings):
    """
    Kiểm tra tiêu đề trang Google sử dụng BASE_URL từ biến môi trường.
    """
    # Sử dụng BASE_URL từ fixture
    base_url = app_settings.BASE_URL
    page.goto(base_url)

    # Xác minh rằng tiêu đề trang là "Google"
    assert page.title() == "Google"

def test_search_for_something(page: Page, app_settings):
    """
    Kiểm tra chức năng tìm kiếm trên Google sử dụng BASE_URL.
    """
    # Sử dụng BASE_URL từ fixture
    base_url = app_settings.BASE_URL
    page.goto(base_url)

    # Tìm kiếm trường nhập liệu tìm kiếm (search input)
    search_box = page.locator('textarea[name="q"]')

    # Nhập từ khóa tìm kiếm
    search_box.fill("Playwright Pytest tutorial")

    # Nhấn Enter để bắt đầu tìm kiếm
    search_box.press("Enter")

    # Chờ cho page load xong
    page.wait_for_url("**/search?q=Playwright*")

    # Tìm trong body có chữ Playwright
    body_text = page.locator('body').inner_text()
    assert "Playwright" in body_text
