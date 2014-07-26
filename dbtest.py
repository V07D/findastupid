# coding: utf-8
from peewee import *

db = SqliteDatabase('test.db')

class BaseModel(Model):
	class Meta:
		database = db


class Human(BaseModel):
	name = CharField()

class Pet(BaseModel):
	name = CharField()

class HumanPet(BaseModel):
	human = ForeignKeyField(Human)
	pet = ForeignKeyField(Pet)

if __name__ == '__main__':
	try:
		Human.create_table()
		Pet.create_table()
		HumanPet.create_table()
	except Exception as e:
		pass
	me = Human.create(name='Alex')
	busya = Pet.create(name='Busya', owner=me)
	frosya = Pet.create(name='Frosya', owner=me)
	HumanPet.create(human=me, pet=busya)
	HumanPet.create(human=me, pet=frosya)
	for pet in Pet.select().join(HumanPet).join(Human).where(Human.id == me.id):
		print(pet.name)
