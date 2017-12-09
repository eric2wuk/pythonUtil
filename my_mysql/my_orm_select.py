from my_orm import DBSession
from user import User

session = DBSession()

user = session.query(User).filter(User.id=='8').one()

print('type:', type(user))
print('name', user.name)
session.close()
