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

from oslo_config import cfg
import logging
import contextlib
import copy
import os
import requests
from urllib.parse import urljoin

from oslo_policy import _checks
from oslo_policy._i18n import _
from oslo_policy_remote import exceptions, opts


LOG = logging.getLogger(__name__)
CONF = cfg.CONF
opts._register(CONF)


class ConnectionPoolManager:
    """Manages connection pooling for Remote Policy server requests."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionPoolManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.session = None
            self.initialized = True

    def get_session(self, maxsize=10, retries=3, timeout=30):
        """Get or create a session with connection pooling."""
        if self.session is None:
            adapter = requests.adapters.HTTPAdapter(
                max_retries=retries, pool_connections=maxsize, pool_maxsize=maxsize
            )
            self.session = requests.Session()
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)
            self.session.timeout = timeout
        return self.session

    def close(self):
        """Close the session and its connection pool."""
        if self.session is not None:
            self.session.close()
            self.session = None


class RemoteCheck(_checks.Check):
    """Check ``remote:`` rules by calling to an Open Policy Agent instance.

    This implementation simply verifies that the response
    is exactly ``{"result": True}``.
    """

    def __init__(self, kind, match):
        super().__init__(kind, match)
        self.endpoint = "enforce"
        self.opts_registered = False

    def __call__(self, target, credentials, enforcer, current_rule=None):
        if not self.opts_registered:
            opts._register(enforcer.conf)
            self.opts_registered = True

        self.service = enforcer.conf.remote_policy.service
        self.request_kwargs = {"timeout": enforcer.conf.remote_policy.timeout}
        if not enforcer.conf.remote_policy.server_url:
            raise exceptions.RemotePolicyConfigError(
                "Remote policy server URL is not configured"
            )
        
        # Configure SSL if needed
        if enforcer.conf.remote_policy.ssl_verify:
            self._configure_ssl(enforcer.conf.remote_policy)

        payload = self._construct_payload(
            self.service, credentials, current_rule, enforcer, target
        )

        try:
            with contextlib.closing(
                self.session.post(
                    url=urljoin(
                        enforcer.conf.remote_policy.server_url + "/", 
                        self.endpoint
                    ), 
                    json=payload, 
                    **self.request_kwargs,
                )
            ) as response:
                response.raise_for_status()
                result = response.json()
            if not isinstance(result, dict) or "allowed" not in result:
                raise exceptions.RemotePolicyServerError(
                    "Invalid response format from policy server"
                )
            return result["allowed"]
        except (
            requests.exceptions.Timeout,
            requests.exceptions.RequestException,
            exceptions.RemotePolicyServerError,
        ) as e:
            LOG.error(f"Remote policy check failed: {e}")

            # TODO: This is a temporary fallback mechanism that will be improved in future versions.
            # Currently, when remote policy check fails (timeout, connection error, or server error),
            # we fallback to the default rule if it exists. This behavior might change in future releases
            # to provide more configurable fallback strategies.
            default_rule = enforcer.registered_rules.get(current_rule)
            if default_rule:
                LOG.info(f"Falling back to default rule for {current_rule}")
                return _checks._check(
                    rule=default_rule._check,
                    target=target,
                    creds=credentials,
                    enforcer=enforcer,
                    current_rule=current_rule,
                )

            if CONF.remote_policy.fail_closed:
                return False
            raise exceptions.RemotePolicyServerError(f"Policy check failed: {str(e)}")

    def _configure_ssl(self, remote_policy_conf):
        """Configure SSL settings for the request.
        
        This method extracts SSL configuration logic from the __call__ method
        to reduce complexity.
        """
        cert_file = remote_policy_conf.client_crt_file
        key_file = remote_policy_conf.client_key_file
        ca_crt_file = remote_policy_conf.ca_crt_file
        verify_server = remote_policy_conf.verify_server_crt
        
        if cert_file:
            if not os.path.exists(cert_file):
                raise RuntimeError(
                    _("Unable to find ssl cert_file  : %s") % cert_file
                )
            if not os.access(cert_file, os.R_OK):
                raise RuntimeError(
                    _("Unable to access ssl cert_file  : %s") % cert_file
                )
        if key_file:
            if not os.path.exists(key_file):
                raise RuntimeError(_("Unable to find ssl key_file : %s") % key_file)
            if not os.access(key_file, os.R_OK):
                raise RuntimeError(
                    _("Unable to access ssl key_file  : %s") % key_file
                )
        cert = (cert_file, key_file)
        if verify_server and ca_crt_file:
            if not os.path.exists(ca_crt_file):
                raise RuntimeError(
                    _("Unable to find ca cert_file  : %s") % ca_crt_file
                )
            verify_server = ca_crt_file
        self.request_kwargs["cert"] = cert
        self.request_kwargs["verify"] = verify_server

    @property
    def session(self):
        pool_manager = ConnectionPoolManager()
        return pool_manager.get_session(maxsize=10, retries=1)

    @staticmethod
    def _construct_payload(service_id, creds, current_rule, enforcer, target):
        # Convert instances of object() in target temporarily to
        # empty dict to avoid circular reference detection
        # errors in jsonutils.dumps().
        temp_target = copy.deepcopy(target)
        for key in target.keys():
            element = target.get(key)
            if type(element) is object:
                temp_target[key] = {}
        return {
            "service": service_id,
            "rule": current_rule,
            "target": temp_target,
            "credentials": creds,
        }
