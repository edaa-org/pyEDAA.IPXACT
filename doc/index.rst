.. include:: shields.inc

.. image:: _static/logo.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/edaa-org/pyEDAA.IPXACT

.. raw:: html

    <br>

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:IPXACT-github| |SHIELD:svg:IPXACT-src-license| |SHIELD:svg:IPXACT-ghp-doc| |SHIELD:svg:IPXACT-doc-license| |SHIELD:svg:IPXACT-gitter|
   |  |SHIELD:svg:IPXACT-pypi-tag| |SHIELD:svg:IPXACT-pypi-status| |SHIELD:svg:IPXACT-pypi-python|
   |  |SHIELD:svg:IPXACT-gha-test| |SHIELD:svg:IPXACT-lib-status| |SHIELD:svg:IPXACT-codacy-quality|

.. Disabled shields: |SHIELD:svg:IPXACT-codacy-coverage| |SHIELD:svg:IPXACT-codecov-coverage| |SHIELD:svg:IPXACT-lib-dep| |SHIELD:svg:IPXACT-req-status| |SHIELD:svg:IPXACT-lib-rank|

.. only:: latex

   |SHIELD:png:IPXACT-github| |SHIELD:png:IPXACT-src-license| |SHIELD:png:IPXACT-ghp-doc| |SHIELD:png:IPXACT-doc-license| |SHIELD:png:IPXACT-gitter|
   |SHIELD:png:IPXACT-pypi-tag| |SHIELD:png:IPXACT-pypi-status| |SHIELD:png:IPXACT-pypi-python|
   |SHIELD:png:IPXACT-gha-test| |SHIELD:png:IPXACT-lib-status| |SHIELD:png:IPXACT-codacy-quality|

.. Disabled shields: |SHIELD:png:IPXACT-codacy-coverage| |SHIELD:png:IPXACT-codecov-coverage| |SHIELD:png:IPXACT-lib-dep| |SHIELD:png:IPXACT-req-status| |SHIELD:png:IPXACT-lib-rank|

pyEDAA.IPXACT Documentation
###########################

pyEDAA.IPXACT - An IP-XACT DOM (Document Object Model) for `IEEE 1685-2014 <https://standards.ieee.org/findstds/standard/1685-2014.html>`__
in Python.


.. _goals:

Main Goals
**********

* Offer a Python-based Document Object Model (DOM) for IP-XACT.


.. _features:

Implemented Features
********************

* Generate IP-XACT files for

  * IP-XACT catalogs

.. #Comment
   .. _usecase:

   Use Cases
   *********

   * Wrap command line interfaces of EDA tools (Electronic Design Automation) in Python classes.


Examples
********

.. todo:: Write an example.


IP-XACT Resources
*****************

* Standards:

  * `IEEE 1685-2009 <https://standards.ieee.org/findstds/standard/1685-2009.html>`__
  * `IEEE 1685-2014 <https://standards.ieee.org/findstds/standard/1685-2014.html>`__

* Schema files:

  * :ghrepo:`IPXACT-Schema <edaa-org/IPXACT-Schema>` at GitHub
  * `IP-XACT <http://accellera.org/downloads/standards/ip-xact>`__ at `Accellera <http://accellera.org>`__

.. #Comment
   Consumers
   *********

   This layer is used by:

   * ✅ `pyEDAA.CLITool <https://github.com/edaa-org/pyEDAA.CLITool>`__


.. _news:

News
****

.. only:: html

   Feb. 2022 - Major Update
   ========================

.. only:: latex

   .. rubric:: Major Update

* Major documentation updates.


.. _contributors:

Contributors
************

* :ghrepo:`Patrick Lehmann <Paebbels>` (Maintainer)
* `Unai Martinez-Corral <https://GitHub.com/umarcor/>`__
* `and more... <https://GitHub.com/edaa-org/pyEDAA.IPXACT/graphs/contributors>`__


.. _license:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.

------------------------------------

.. |docdate| date:: %d.%b %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.


.. toctree::
   :hidden:

   Used as a layer of EDA² ➚ <https://edaa-org.github.io/>

.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency

.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   Tutorial
   FurtherResources

.. raw:: latex

   \part{References}

.. toctree::
   :caption: References
   :hidden:

   pyEDAA.IPXACT/index

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   Coverage Report ➚ <coverage/index>
   Static Type Check Report ➚ <typing/index>
   License
   Doc-License
   Glossary
   genindex
   py-modindex
