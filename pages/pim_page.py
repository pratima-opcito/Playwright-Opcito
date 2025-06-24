import os.path
import random


from utils.data_generator import generate_random_emp_id



class PimPage:
    def __init__(self,page):
        self.page = page


    def employee_information(self):
        self.page.locator("a", has_text="Add Employee").first.click()

        self.page.get_by_placeholder("First Name").fill("Pratima1")
        self.page.get_by_placeholder("Middle Name").fill("Mahesh")
        self.page.get_by_placeholder("Last Name").fill("Jadhav")
        #random id geerator
        emp_id = generate_random_emp_id()
        print(emp_id)
        self.page.locator("//label[text()='Employee Id']/following::input[1]").fill(emp_id)
        self.page.locator("//div//img[@alt='profile picture']/following::button[@role='none']").click()
     #   filepath=os.path.abspath("C:\Users\PratimaJadhav\OPCITOPLAYWRIGHTFRAMEWORK\test_data\BUG04.PNG")

        self.page.get_by_role("button",name="Save")

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)

    def click_upload(self):
        self.upload_button.click()