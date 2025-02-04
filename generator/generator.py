from faker import Faker

from data.data_classes import YourInformation

faker_ru = Faker('ru_RU')
faker_en = Faker('EN')
Faker.seed()


def generated_your_information():
    yield YourInformation(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        post_code=faker_ru.postcode()
    )
