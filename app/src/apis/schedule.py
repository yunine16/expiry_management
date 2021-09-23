from datetime import datetime
from database import db
from models import User, Food


class a:
    def get(self,mailadress):
        today=datetime.date.today()+datetime.timedelta(days=7)
        id=db.session.query(Users).filter(Users.mailAdress==mailAdress)
        food=db.session.query(Foods).filter(Foods.user_id==user_id,Foods.expirly_date<=today).all()
        return food

        
