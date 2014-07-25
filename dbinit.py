# coding: utf-8
from models import User, Session # ...

for model in (User, Session):
	model.create_table()
