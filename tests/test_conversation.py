import unittest

import requests_mock

from pycanvas import Canvas
from tests import settings
from tests.util import register_uris


class TestConversation(unittest.TestCase):
    """
    Tests PageView functionality.
    """
    @classmethod
    def setUpClass(self):
        requires = {
            'conversation': [
                'get_by_id',
                "get_by_id_2",
                'edit_conversation',
                'edit_conversation_fail',
                'delete_conversation',
                'delete_conversation_fail'
            ]
        }

        adapter = requests_mock.Adapter()
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY, adapter)
        register_uris(settings.BASE_URL, {'generic': ['not_found']}, adapter)
        register_uris(settings.BASE_URL, requires, adapter)

        self.conversation = self.canvas.get_conversation(1)

    # __str__()
    def test__str__(self):
        string = str(self.conversation)
        assert isinstance(string, str)

    # edit()
    def test_edit(self):
        new_subject = "conversations api example"
        success = self.conversation.edit(subject=new_subject)
        assert success

    def test_edit_fail(self):
        temp_convo = self.canvas.get_conversation(2)
        assert temp_convo.edit() is False

    # delete()
    def test_delete(self):
        success = self.conversation.delete()
        assert success

    def test_delete_fail(self):
        temp_convo = self.canvas.get_conversation(2)
        assert temp_convo.delete() is False
