Installing Infynipy
===================

Infynipy supports python 3.5+. The recommended way to install Infynipy is via ``pip``.

.. code-block:: bash

   pip install infynipy

.. note:: Depending on your system, you may need to use ``pip3`` to install
          packages for python 3.

.. warning:: Avoid using ``sudo`` to install packages. Do you `really` trust
             this package?

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

Updating Infynipy
-----------------

Infynipy can be updated by running:

.. code-block:: bash

   pip install --upgrade infynipy

Installing Older Versions
-------------------------

Older versions of Infynipy can be installed by specifying the version number as
part of the installation command:

.. code-block:: bash

   pip install infynipy==0.1.0

Installing the Latest Development Version
-----------------------------------------

Is there a feature that was recently merged into Infynipy that you cannot wait to
take advantage of? If so, you can install Infynipy directly from github like so:

.. code-block:: bash

   pip install --upgrade https://github.com/beanpuppy/infynipy/archive/master.zip
