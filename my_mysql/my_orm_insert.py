import my_orm
from user import User

session = my_orm.DBSession()
new_user = User(id='8', name='Eric')
session.add(new_user)

session.commit()
session.close()