Quick Start
===========

In this section, we go over everything you need to know to start building
scripts using Infynipy.

Prerequisites
-------------

:Python Knowledge: You need to know at least a little Python to use Infynipy; it's a Python wrapper
                   after all.

:Infynity: A basic understanding of the Infynity mortgage broker system will help with terminology.

:Infynity API username & Key: These are the two values required to use the Infynity API. If you do not
                              have on of these you can ask their support for access.

Common Tasks
------------

Authenticate with Infynity
~~~~~~~~~~~~~~~~~~~~~~~~~~

To create an Infynity instance you need two pieces of information:

1) Username
2) API key

You will need to provide these by passing them in as two arguments when calling the initializer
of the :class:`Infynity` class: ``username``, ``api_key``. For example:

.. code-block:: python

   from infynipy import Infynity

   client = Infynity("USERNAME", "API_KEY")

Get all individuals under a broker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # assume you have a Infynity instance bound to variable `client`

   broker_id = 3999

   for individual in client.broker(broker_id).individuals:
         print(individual)  # Print the individual model class
         print(individual.to_dict())  # Convert the individual model class into a dictionary

Get an individual's incomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # assume you have a Infynity instance bound to variable `client`

   broker_id = 3999  # Broker ID of who owns the individual
   individual_id = 'x1EvOBG3vZgbrjwd'

   incomes = client.broker(broker_id).individual(individual_id).incomes

   for income in incomes:
         print(income)

Update an individual
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # assume you have a Infynity instance bound to variable `client`

   broker_id = 3999  # Broker ID of who owns the individual
   individual_id = 'x1EvOBG3vZgbrjwd'

   # Get the individual
   individual = client.broker(broker_id).individual(individual_id)

   # Change first name
   individual.first_name = 'James'
   individual.update()  # Send the updates
