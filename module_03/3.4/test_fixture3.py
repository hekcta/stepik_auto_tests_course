# import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# # link = "http://selenium1py.pythonanywhere.com/"
# #
# #
# # @pytest.fixture
# # def browser():
# #     print("\nstart browser for test..")
# #     browser = webdriver.Chrome()
# #     yield browser
# #     # этот код выполнится после завершения теста
# #     print("\nquit browser..")
# #     browser.quit()
# #
# #
# # class TestMainPage1():
# #     # вызываем фикстуру в тесте, передав ее как параметр
# #     def test_guest_should_see_login_link(self, browser):
# #         browser.get(link)
# #         browser.find_element(By.CSS_SELECTOR, "#login_link")
# #
# #     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
# #         browser.get(link)
# #         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass