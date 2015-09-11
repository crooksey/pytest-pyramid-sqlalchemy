from intranet.tests._testbench_setup import *
import pytest
import transaction

# create 10 random dogs
@pytest.fixture
def user_models(db_session_ro):
	with transaction.manager:
		for i in range(10):
			dog = Dog(
				dog_name='dog{0}'.format(i))
			db_session_rw.add(dog)
	return [u.id for u in db_session_ro.query(Dog.id).all()]