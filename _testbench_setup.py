import pytest
from pyramid import testing
from yourapp.ro_models import *
from yourapp.rw_models import *
from pyramid.security import unauthenticated_userid

# This guide assumes you are using two databases, bundled inside
# the pyramid request... request.DBSessionRW and request.DBSessionRO
# You may connect to two databases, one for read and write, one for read
# only access


@pytest.yield_fixture
def app_config():
	# Setup two temp sqlite databases for testing, it is best to use
	# the same database that your application uses in production
    settings = {'dbwrite.url': 'sqlite:///:memory:', 
    			'dbread.url': 'sqlite:///:memory:'}
    config = testing.setUp(settings=settings)
    # Then icnlude the "includeme" settings from each model file
    config.include('yourapp.rw_models')
    config.include('yourapp.ro_models')
    yield config
    testing.tearDown()

# Now the app is setup, we can configure each instance of Session, for each
# database the application connects to
@pytest.fixture
def db_session_rw(app_config):
	# This is as it is setup in the models file
    session = app_config.registry['db_sessionmaker_rw']()
    engine = session.bind
    Base.metadata.create_all(engine)
    # Return session instance
    return session


@pytest.fixture
def db_session_ro(app_config):
	# This is as it is setup in the models file
	session = app_config.registry['db_sessionmaker_ro']()
	engine = session.bind
	BaseRO.metadata.create_all(engine)
	# Return session instance
	return session

# Bundle a dummy request.user for Ziggurat Foundations
@pytest.fixture
def user(dummy_request):
    userid = unauthenticated_userid(dummy_request)
    if userid is not None:
        # this should return None if the user doesn't exist
        # in the database
        return request.DBSessionRW.query(User).\
            filter(User.id == userid).first()

# Now we can create a dummy request and modify it for how we use it inside
# our application.
@pytest.fixture
def dummy_request(db_session_ro, db_session_rw):
    # Because we're using DummyRequest here, we need to manually add both
    # instances of the DBSession to the request, as we cannot do
    # config.add as we would inside a normal instance of pyramids main()
    # note here I also add user, as my app relys on request.user
    # As my application views call "request.user" or "request.DBSEssion(X)"
    # this is how we modify these to add them to the request
    return testing.DummyRequest(DBSessionRW=db_session_rw, 
    							DBSessionRO=db_session_ro,
    							user=user)


