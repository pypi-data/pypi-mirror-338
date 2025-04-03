# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from unittest import mock
from oslo_config import cfg
from oslo_policy_remote import remote
from oslo_policy_remote import opts

@pytest.fixture
def remote_check():
    return remote.RemoteCheck('remote', 'test_rule')

@pytest.fixture
def enforcer():
    conf = cfg.ConfigOpts()
    opts._register(conf)
    enforcer = mock.Mock()
    enforcer.conf = conf
    enforcer.registered_rules = {}
    return enforcer

@pytest.fixture
def target():
    return {'project_id': 'test_project', 'user_id': 'test_user'}

@pytest.fixture
def credentials():
    return {
        'user_id': 'test_user',
        'project_id': 'test_project',
        'roles': ['member']
    }

def test_remote_check_success(remote_check, mock_requests, enforcer, target, credentials):
    mock_requests.post(
        'http://localhost:8000/check/enforce',
        json={'allowed': True}
    )
    assert remote_check(target, credentials, enforcer, 'test_rule') is True

def test_remote_check_failure(remote_check, mock_requests, enforcer, target, credentials):
    mock_requests.post(
        'http://localhost:8000/check/enforce',
        status_code=500
    )
    assert remote_check(target, credentials, enforcer, 'test_rule') is False 