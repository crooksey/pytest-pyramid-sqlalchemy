import pytest
# Global imports for testbench setup
from _populate_data_rw import *
from _populate_data_ro import *
from _testbench_setup import *

from yourapp.views import list_users

# This is a test in the most basic of forms, simply
# show how to load the test data and dummy request into the test bench

def test_list_users_view(dummy_request, user_models):
	# we have added 10 users, so this should assert perfectly
	users_test = dummy_request.DBSessionRW.query(User).all()
	assert len(users_test) > 4
	# Now try loading the view
	response = yourapp.views.list_users.put_away_queue(dummy_request)