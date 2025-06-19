import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django
django.setup()

#fake script
import random
from part_two.models import Users
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    
    for entry in range(N):
        fake_name = fakegen.name().split() #split the name with space
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        
        #New entry...
        user = Users.objects.get_or_create(first_name = fake_first_name,
                                           last_name = fake_last_name,
                                           email = fake_email)[0]
        
        

if __name__ == "__main__":
    print("populating data_bases")
    populate(20)
    print("complted !!!!!")
             