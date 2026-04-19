from models import User, engine
from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session=Session()
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

user=session.query(User).filter_by(id=1).first()

session.delete(user)
session.commit()