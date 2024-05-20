import random
from faker import Faker


class UniqueDataGenerator:
    def __init__(self):
        self.faker = Faker()
        self.generated_data = {
            "emails": [],
            "phone_numbers": [],
            "websites": [],
            "names": [],
            "lastnames": [],
            "company_names": [],
            "product_names": [],
            "product_descriptions": [],
            "expense_names": [],
            "expense_descriptions": [],
            "product_references": []
        }

    def generate_unique_name(self):
        name = self.faker.first_name()
        while name in self.generated_data["names"]:
            name = self.faker.first_name()
        self.generated_data["names"].append(name)
        return name

    def generate_unique_lastname(self):
        lastname = self.faker.last_name()
        while lastname in self.generated_data["lastnames"]:
            lastname = self.faker.last_name()
        self.generated_data["lastnames"].append(lastname)
        return lastname

    def generate_unique_email(self):
        email = self.faker.email()
        while email in self.generated_data["emails"]:
            email = self.faker.email()
        self.generated_data["emails"].append(email)
        return email

    def generate_unique_phone_number(self):
        phone_number = "+1" + "".join([str(random.randint(0, 9)) for _ in range(10)])
        while phone_number in self.generated_data["phone_numbers"]:
            phone_number = "+1" + "".join([str(random.randint(0, 9)) for _ in range(10)])
        self.generated_data["phone_numbers"].append(phone_number)
        return phone_number

    def generate_unique_website(self):
        website = self.faker.url()
        while website in self.generated_data["websites"]:
            website = self.faker.url()
        self.generated_data["websites"].append(website)
        return website

    def generate_unique_company_name(self):
        company_name = self.faker.company()
        while company_name in self.generated_data["company_names"]:
            company_name = self.faker.company()
        self.generated_data["company_names"].append(company_name)
        return company_name

    def generate_unique_product_name(self):
        product_name = self.faker.word()
        while product_name in self.generated_data["product_names"]:
            product_name = self.faker.word()
        self.generated_data["product_names"].append(product_name)
        return product_name

    def generate_unique_product_description(self):
        product_description = self.faker.sentence()
        while product_description in self.generated_data["product_descriptions"]:
            product_description = self.faker.sentence()
        self.generated_data["product_descriptions"].append(product_description)
        return product_description

    def generate_unique_expense_name(self):
        expense_name = self.faker.word()
        while expense_name in self.generated_data["expense_names"]:
            expense_name = self.faker.word()
        self.generated_data["expense_names"].append(expense_name)
        return expense_name

    def generate_unique_expense_description(self):
        expense_description = self.faker.sentence()
        while expense_description in self.generated_data["expense_descriptions"]:
            expense_description = self.faker.sentence()
        self.generated_data["expense_descriptions"].append(expense_description)
        return expense_description

    def generate_unique_product_price(self):
        product_price = round(self.faker.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=1.0, max_value=1000.0), 2)
        return product_price

    def generate_unique_product_reference(self):
        product_reference = self.faker.bothify(text='???-########')
        while product_reference in self.generated_data["product_references"]:
            product_reference = self.faker.bothify(text='???-########')
        self.generated_data["product_references"].append(product_reference)  # Use append() instead of add()
        return product_reference
