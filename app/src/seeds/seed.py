from flask_seeder import Seeder, Faker, generator
from models.user import User
from models.food import Food

# All seeders inherit from Seeder
class DemoSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):

        jack_users = [
            User(mailAddress="mochi@jack.com"),
            User(mailAddress="mono@jack.com"),
            User(mailAddress="nine@jack.com"),
            User(mailAddress="zuo@jack.com"),
            User(mailAddress="wato@jack.com")
        ]
        
        for jack_user in jack_users:
            print("Adding user: %s" % jack_user)
            self.db.session.add(jack_user)

        # Create a new Faker and tell it how to create User objects
        user_faker = Faker(
          cls=User,
          init={
            "mailAddress": generator.Email(),
          }
        )
        
        # Create 5 fake users 
        for user in user_faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)

        sample_foods = [
            Food(name="大根", expiry_date="2021-10-10", user_id=1),
            Food(name="人参", expiry_date="2021-10-10", user_id=1),
            Food(name="秋刀魚", expiry_date="2021-10-10", user_id=2),
            Food(name="こんにゃく", expiry_date="2021-10-10", user_id=2),
            Food(name="ぶどう", expiry_date="2021-10-10", user_id=3)
        ]
        
        for sample_food in sample_foods:
            print("Adding food: %s" % sample_food)
            self.db.session.add(sample_food)

        # Create a new Faker and tell it how to create Food objects
        food_faker = Faker(
          cls=Food,
          init={
            "name": generator.Name(),
            "expiry_date":"2021-10-10",
            "user_id":generator.Integer()
          }
        )
        
        # Create 5 fake foods
        for food in food_faker.create(5):
            print("Adding food: %s" % food)
            self.db.session.add(food)
