# -*- encoding: utf-8 -*-
#
# Copyright © 2013 Red Hat, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ironicclient.common import base


class Chassis(base.Resource):
    def __repr__(self):
        return "<Chassis %s>" % self._info


class ChassisManager(base.Manager):
    resource_class = Chassis

    @staticmethod
    def _path(id=None):
        return '/v1/chassis/%s' % id if id else '/v1/chassis'

    def list(self):
        return self._list(self._path(), "chassis")

    def get(self, chassis_id):
        try:
            return self._list(self._path(chassis_id))[0]
        except IndexError:
            return None
