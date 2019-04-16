# import os
# import sys
# import django
# import random
# from faker import Faker
#
# sys.path.append('..')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configurations.settings')
#
# django.setup()
#
# from app_dir.first_app.models import AccessRecord, WebPage, Topic
#
# fake = Faker()
# topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']
#
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
#
#
# def populate(n=5):
#     for entry in range(n):
#         top = add_topic()
#
#         fake_url = fake.url()
#         fake_date = fake.date()
#         fake_name = fake.company()
#
#         webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
#
#         acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)
#
#
# if __name__ == '__main__':
#     print('Populating script')
#     populate(20)
#     print('Populating complete')
