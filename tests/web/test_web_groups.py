# -*- coding: utf-8 -*-
u"""
Copyright 2016 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from nose.tools import assert_equal, assert_is_not_none

from toolium_examples.pageobjects.web.tables import TablesPageObject
from toolium_examples.test_cases import SeleniumTestCase


class Tables(SeleniumTestCase):
    def test_search_user(self):
        # Expected user
        user = {'last_name': 'Doe', 'first_name': 'Jason', 'email': 'jdoe@hotmail.com', 'due': '$100.00',
                'web': 'http://www.jdoe.com'}

        # Open url
        self.driver.get('http://the-internet.herokuapp.com/tables')

        # Search user in first table
        found_row = None
        for row in TablesPageObject().table1.rows.page_elements:
            if row.last_name.text == user['last_name']:
                found_row = row
                break

        # Check user data
        assert_is_not_none(found_row, 'User {} not found'.format(user['last_name']))
        assert_equal(found_row.last_name.text, user['last_name'])
        assert_equal(found_row.first_name.text, user['first_name'])
        assert_equal(found_row.email.text, user['email'])
        assert_equal(found_row.due.text, user['due'])
        assert_equal(found_row.web.text, user['web'])
