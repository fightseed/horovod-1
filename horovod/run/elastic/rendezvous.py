# Copyright 2019 Uber Technologies, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from __future__ import absolute_import

from horovod.run.http.http_server import RendezvousHandler

# GET methods
GET_RANK_AND_SIZE = 'rank_and_size'


def create_rendezvous_handler(driver):
    class ElasticRendezvousHandler(RendezvousHandler):
        def _get_value(self, scope, key):
            if scope == GET_RANK_AND_SIZE:
                return self._get_rank_and_size(key)

            return super(RendezvousHandler, self)._get_value(scope, key)

        def _get_rank_and_size(self, last_rank):
            return driver.get_rank_and_size(last_rank)
    return ElasticRendezvousHandler
