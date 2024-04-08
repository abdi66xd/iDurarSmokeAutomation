import random
from faker import Faker


class UniqueDataGenerator:
    def __init__(self):
        self.faker = Faker()
        self.generated_data = {"emails": [], "phone_numbers": [], "websites": [], "names": [], "lastnames": []}

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
