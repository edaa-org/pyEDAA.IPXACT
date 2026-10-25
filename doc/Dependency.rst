.. _DEP:

Dependencies
############

.. |img-IPXACT-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyEDAA.IPXACT
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/edaa-org/pyEDAA.IPXACT
.. |img-IPXACT-vul-status| image:: https://img.shields.io/snyk/vulnerabilities/github/edaa-org/pyEDAA.IPXACT
   :alt: Snyk Vulnerabilities for GitHub Repo
   :height: 22
   :target: https://img.shields.io/snyk/vulnerabilities/github/edaa-org/pyEDAA.IPXACT

+------------------------------------------+------------------------------------------+
| `Libraries.io <https://libraries.io/>`_  | Vulnerabilities Summary                  |
+==========================================+==========================================+
| |img-IPXACT-lib-status|                  | |img-IPXACT-vul-status|                  |
+------------------------------------------+------------------------------------------+

.. _DEP/package:

pyEDAA.IPXACT Package (Mandatory)
*********************************

.. rubric:: Manually Installing Package Requirements

Use the :file:`requirements.txt` file to install all dependencies via ``pip3`` or install the package directly from
PyPI (see :ref:`INSTALL`).

.. tab-set::

   .. tab-item:: Linux/macOS
      :sync: Linux

      .. code-block:: bash

         pip3 install -U -r requirements.txt

   .. tab-item:: Windows
      :sync: Windows

      .. code-block:: powershell

         pip install -U -r requirements.txt


.. rubric:: Dependency List

.. dependency-table:: package
   :caption: Mandatory dependencies of the pyEDAA.IPXACT package.

.. _DEP/testing:

Unit Testing (Optional)
***********************

Unit Testing / Coverage / Type Checking (Optional)
==================================================

Additional Python packages needed for testing, code coverage collection and static type checking. These packages are
only needed for developers or on a CI server.


.. rubric:: Manually Installing Test Requirements

Use the :file:`tests/requirements.txt` file to install all dependencies via ``pip3``. The file will recursively install
the mandatory dependencies too.

.. tab-set::

   .. tab-item:: Linux/macOS
      :sync: Linux

      .. code-block:: bash

         pip install -U -r tests/requirements.txt

   .. tab-item:: Windows
      :sync: Windows

      .. code-block:: powershell

         pip3 install -U -r tests\requirements.txt

.. rubric:: Dependency List - Unit Testing

.. dependency-table:: testing
   :caption: Dependencies for unit testing, code coverage and static type checking.



.. _DEP/documentation:

Sphinx Documentation (Optional)
*******************************

Additional Python packages needed for documentation generation. These packages are only needed for developers or on a
CI server.


.. rubric:: Manually Installing Documentation Requirements

Use the :file:`doc/requirements.txt` file to install all dependencies via ``pip3``. The file will recursively install
the mandatory dependencies too.

.. tab-set::

   .. tab-item:: Linux/macOS
      :sync: Linux

      .. code-block:: bash

         pip install -U -r doc/requirements.txt

   .. tab-item:: Windows
      :sync: Windows

      .. code-block:: powershell

         pip3 install -U -r doc\requirements.txt


.. rubric:: Dependency List

.. dependency-table:: documentation
   :caption: Dependencies for building this documentation.

.. _DEP/packaging:

Packaging (Optional)
********************

Additional Python packages needed for installation package generation. These packages are only needed for developers or
on a CI server.

:file:`pyproject.toml` lists them as build requirements, so ``python3 -m build`` installs them itself.

.. ``dependency-table`` reads requirements files and published packages, but not the build requirements in
   'pyproject.toml', so this table stays hand-written.


.. rubric:: Dependency List

+----------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Package**                                                                | **Version**  | **License**                                                                                              | **Dependencies**                                                                                                                                     |
+============================================================================+==============+==========================================================================================================+======================================================================================================================================================+
| `setuptools <https://GitHub.com/pypa/setuptools>`__                        | ≥83.0        | `MIT <https://GitHub.com/pypa/setuptools/blob/main/LICENSE>`__                                           | *None*                                                                                                                                               |
+----------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pyTooling <https://GitHub.com/pyTooling/pyTooling>`__                     | ≥10.0        | `Apache License, 2.0 <https://GitHub.com/pyTooling/pyTooling/blob/main/LICENSE.md>`__                    | *None*                                                                                                                                               |
+----------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _DEP/publishing:

Publishing (CI-Server only)
***************************

Additional Python packages needed for publishing the generated installation package to e.g, PyPI or any equivalent
services. These packages are only needed for maintainers or on a CI server.


.. rubric:: Manually Installing Publishing Requirements

Use the :file:`dist/requirements.txt` file to install all dependencies via ``pip3``. The file will recursively
install the mandatory dependencies too.

.. tab-set::

   .. tab-item:: Linux/macOS
      :sync: Linux

      .. code-block:: bash

         pip install -U -r dist/requirements.txt

   .. tab-item:: Windows
      :sync: Windows

      .. code-block:: powershell

         pip3 install -U -r dist\requirements.txt


.. rubric:: Dependency List

.. dependency-table:: publishing
   :caption: Dependencies for publishing the package.
