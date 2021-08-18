from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

vvd = User(first_name = "Virjil", last_name = "Van Djik", position="CD", c_of_origin="Neitherland", image_url = "https://technosports.co.in/wp-content/uploads/2020/04/vvd.jpg")
dj = User(first_name = "Diego", last_name = "Jota", position="LWF", c_of_origin="Portugal", image_url = "https://www.coachesvoice.com/wp-content/uploads/2020/09/JotaMobile.png")
fab = User(first_name = "Fabinho", position="DMF", c_of_origin="Brasil", image_url = "https://images.daznservices.com/di/library/GOAL/e2/9d/fabinho-liverpool_5vqvpvvtfh1714lzlo39jcdrl.jpg?t=-1464135580&quality=100")


db.session.add_all([vvd, dj, fab])
db.session.commit()

fir = Post(title = "first post", content="Yesssssssss! i enjoyrd the game", user_id="1")
thi = Post(title = "happy", content="cool to have scored in today's game game", user_id="1")
fou = Post(title = "praise", content="nice defence from us", user_id="1")
sec = Post(title = "first post", content="Yesssssssss! i enjoyrd the game", user_id="2")

db.session.add_all([fir, thi, fou, sec])
db.session.commit()