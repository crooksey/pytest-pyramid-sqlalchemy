from intranet.tests._testbench_setup import *
import pytest
import transaction

# create 10 random users 
@pytest.fixture
def user_models(db_session_rw):
	with transaction.manager:
		for i in range(10):
			user = User(
				user_name='user{0}'.format(i), 
				email='user{0}@example.org'.format(i), 
				full_name='firstname{0} lastname{0}'.format(i), 
				phone_number='555 212 1{0}'.format(i),
				job_title='Manager #{0}'.format(i))
			db_session_rw.add(user)
	return [u.id for u in db_session_rw.query(User.id).all()]