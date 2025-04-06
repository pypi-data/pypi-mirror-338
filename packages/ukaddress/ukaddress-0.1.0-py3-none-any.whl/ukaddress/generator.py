from faker import Faker

fake = Faker("en_GB")  # British locale

def generate_address():
    return fake.address().replace("\n", ", ")
