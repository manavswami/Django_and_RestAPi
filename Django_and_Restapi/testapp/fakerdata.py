import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Faker.settings')

import django
django.setup()

from  testapp.models import global_database






from faker import Faker

faker = Faker('cz_CZ')

for i in range(3):

    name = faker.name()
    email = faker.faker.internet.email()
    phone = faker.phone_number()
    phone="+91 "+phone+"1"


    global_database.objects.get_or_create(Phone_Number=phone,Name=name,Email_Address=email)

    
