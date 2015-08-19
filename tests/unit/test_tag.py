# -*- coding: utf-8 -*-

import unittest

from intercom.client import Client
from mock import patch
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_tag


class TagTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_gets_a_tag(self):
        with patch.object(Client, 'get', return_value=test_tag) as mock_method:  # noqa
            tag = self.client.tags.find(name="Test Tag")
            eq_(tag.name, "Test Tag")
            mock_method.assert_called_once_with('/tags', {'name': "Test Tag"})

    @istest
    def it_creates_a_tag(self):
        with patch.object(Client, 'post', return_value=test_tag) as mock_method:  # noqa
            tag = self.client.tags.create(name="Test Tag")
            eq_(tag.name, "Test Tag")
            mock_method.assert_called_once_with('/tags/', {'name': "Test Tag"})

    @istest
    def it_tags_users(self):
        params = {
            'name': 'Test Tag',
            'user_ids': ['abc123', 'def456'],
            'tag_or_untag': 'tag'
        }
        with patch.object(Client, 'post', return_value=test_tag) as mock_method:  # noqa
            tag = self.client.tags.create(**params)
            eq_(tag.name, "Test Tag")
            eq_(tag.tagged_user_count, 2)
            mock_method.assert_called_once_with('/tags/', params)
