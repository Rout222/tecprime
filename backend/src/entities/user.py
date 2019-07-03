# coding=utf-8
from marshmallow import Schema, fields # para manusear os JSON
from tinydb import Query

class User(object):
	"""docstring for User"""
	def __init__(self, email, first_name, last_name, avatar):
		super(User, self).__init__()
		self.email 		= email
		self.first_name = first_name
		self.last_name 	= last_name
		self.avatar 	= avatar

	def save(self): # função apenas para usar o tinyDB
		return {
			"email"			: self.email,
			"first_name"	: self.first_name,
			"last_name"		: self.last_name,
			"avatar"		: self.avatar		
		}

class UserSchema(Schema): # pra cuidar da transformação JSON
	email 		= fields.Str()
	first_name	= fields.Str()
	last_name	= fields.Str()
	avatar		= fields.Str()