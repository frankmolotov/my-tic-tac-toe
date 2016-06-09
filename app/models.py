from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, index=True)
	email = db.Column(db.String, unique=True, index=True)
	password = db.Column(db.String, index=True)
	admin = db.Column(db.SmallInteger, default=ROLE_USER)
	
	def __repr__(self):
		return ('<username:%s, email:%s, password:%s>' % (self.username, self.email, self.password))
