# project/tests/test_trip.py

import unittest
from datetime import date

from project.server.models import Trip
from project.server import db
from base import BaseTestCase




class TestTripBlueprint(BaseTestCase):


    def test_trip_add(self):

	with self.client:
	    self.client.post(
		'/login',
		data=dict(email="ad@min.com", password="admin_user"),
		follow_redirects=True
	    )
	    self.client.post(
		'/trips',
		data=dict(name='Test', location='TestLol', 
			start_date='01/01/2000', end_date='01/01/2001'),
		follow_redirects=True
	    )
	    trip = Trip.query.filter_by(name='Test', location='TestLol',
				start_date='01/01/2000', end_date='01/01/2001')
	    self.assertIsNotNone(trip)


    def test_valid_dates(self):

	with self.client:
	    self.client.post(
		'/login',
		data=dict(email="ad@min.com", password="admin_user"),
		follow_redirects=True
	    )
	    self.client.post(
		'/trips',
		data=dict(name='Test_Dates', location='Test', 
			start_date='01/01/2001', end_date='01/01/2000'),
		follow_redirects=True
	    )
	    trip = Trip.query.filter_by(name='Test_Dates', location='Test',
				start_date='01/01/2001', end_date='01/01/2000')
	    self.assertIsNone(trip)


    # this section was attempted before realizing that the database handles
    # a null User in its own processes
'''
    def test_valid_owner(self):

	startdate = date(2000, 1, 1)
	enddate = date(2001, 1, 1)
	trip = Trip(name='Test_Owner', location='Test',
			start_date=startdate, end_date=enddate, user=None)
	db.session.add(trip)
	db.session.commit()
	test = Trip.query.filter_by(name='Test_Owner', location='Test',
			start_date='01/01/2000', end_date='01/01/2001')
	self.assertIsNone(test)
'''


