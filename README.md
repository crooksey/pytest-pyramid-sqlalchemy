# pytest-pyramid-sqlalchemy

This breif demo shows how to configure a py.test enviroment, when using multiple databases, when 
DBSession is inside the pyramid request. To learn how to bundle DBSession into a pyramid
request, check out this awesome blog post: https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/

This guide also includes testing for Ziggurat Foundations, bundling the request.user into a test

The test folder contains several files:

_testbench_setup.py this configures the global test bench
_populate_data_ro.py this populates one test database
_populate_data_ro.py this populates the other database
example_test.py an example test using the above test bench
run_tests.sh command to run the tests
