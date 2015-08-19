# -*- coding: utf-8 -*-

from intercom import event
from intercom.api_operations.save import Save
from intercom.service.base_service import BaseService


class Event(BaseService, Save):

    @property
    def collection_class(self):
        return event.Event
