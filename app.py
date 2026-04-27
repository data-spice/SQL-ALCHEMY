# from models import User, engine
# from sqlalchemy.orm import sessionmaker

# Session=sessionmaker(bind=engine)
# session=Session()
# user=User(name="John Doe",age=30)
# user_2=User(name="Victor Mwaniki",age=45)
# user_3=User(name="Shantel Wanjiku",age=28)
# session.add_all([user,user_2,user_3])
# session.commit()

# users=session.query(User).all()

# user=users[0]
# print(user)
# print(user.id)
# print(user.name)
# print(user.age)

# for user in users:
#     print(user.id,user.name,user.age)

# user=session.query(User).filter_by(age=10).one_or_none()

# user=session.query(User).filter_by(id=1).first()

# session.delete(user)
# session.commit()

# ==========================================================
#                     LESSON 3
# ==========================================================
import random
from sqlalchemy.orm import sessionmaker
from models import User,engine

Session=sessionmaker(bind=engine)
session=Session()

# names=["Victor","Mwaniki","Alvin", "Kipchumba","Zenin" ,"Rocho","Frida" ,"Mohammed"]
# ages=[21,34,21,34,67,43,61,52,34,10]

# for x in range(20):
#     user=User(name=random.choice(names),age=random.choice(ages))
#     session.add(user)

# session.commit()

users=session.query(User).order_by(User.age).all()
for user in users:
    print(f"User age: {user.age}, name: {user.name}, id: {user.id}")