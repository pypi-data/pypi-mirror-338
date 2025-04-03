Remote Policy Checker for Oslo Policy
=====================================

.. warning::

   This project is currently in early development phase and is **NOT** ready for production use.
   The codebase is undergoing active development and significant changes may occur.
   
   Key limitations:
   
   * API interfaces may change without notice
   * Some features are incomplete or experimental
   * Documentation may be outdated
   * Test coverage is not comprehensive
   
   Use at your own risk. For production use, please wait for a stable release.

This package extends Oslo Policy to support remote HTTP-based policy checking,
allowing policy decisions to be made by a remote service.

Installation
------------

.. code-block:: bash

   pip install oslo.policy.remote

Configuration
-------------

Add to your service's configuration file:

.. code-block:: ini

   [remote_policy]
   server_url = http://policy-server:8082
   timeout = 3
   fail_closed = true
   ssl_verify = false

Policy File Example
-------------------

.. code-block:: yaml

   create_instance: remote:create_instance
   delete_instance: rule:admin_or_owner

Generating Sample Policies
--------------------------

.. code-block:: bash

   oslopolicy-remote-policy-generator --namespace nova > /etc/nova/policy.yaml

Development
-----------

To set up a development environment:

.. code-block:: bash

   git clone https://github.com/mehmettopcu/oslo.policy.remote
   cd oslo.policy.remote
   pip install -e .[test]
   pytest tests/

License
-------

Apache 2.0
