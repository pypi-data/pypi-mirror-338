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
from oslo_config import cfg
from oslo_policy_remote import opts

@pytest.fixture
def conf():
    conf = cfg.ConfigOpts()
    opts._register(conf)
    return conf

def test_default_config_values(conf):
    assert conf.remote_policy.server_url == 'http://localhost:8000/check'
    assert conf.remote_policy.timeout == 2
    assert conf.remote_policy.fail_closed is True
    assert conf.remote_policy.ssl_verify is False  # Default is False according to opts.py

def test_custom_config_values(conf):
    conf.set_override('server_url', 'http://custom-server:8080/check',
                      group='remote_policy')
    conf.set_override('timeout', 5, group='remote_policy')
    conf.set_override('fail_closed', False, group='remote_policy')
    conf.set_override('ssl_verify', True, group='remote_policy')

    assert conf.remote_policy.server_url == 'http://custom-server:8080/check'
    assert conf.remote_policy.timeout == 5
    assert conf.remote_policy.fail_closed is False
    assert conf.remote_policy.ssl_verify is True 