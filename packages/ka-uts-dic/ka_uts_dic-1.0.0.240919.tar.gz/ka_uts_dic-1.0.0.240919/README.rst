##########
ka_uts_dic
##########

Overview
********

.. start short_desc

**Dictionary 'Utilities'**

.. end short_desc

Installation
************

.. start installation

Package ``ka_uts_dic`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: shell

	$ python -m pip install ka_uts_dic

To install with ``conda``:

.. code-block:: shell

	$ conda install -c conda-forge ka_uts_dic

.. end installation

This requires that the ``readme`` extra is installed:

.. code-block:: shell

	$ python -m pip install ka_uts_dic[readme]

Configuration
*************

The Configuration of general or tenant specific Package logging is defined in Yaml Configuration Files in the data directory <Package Name>/data of the Package.

  .. logging-configuration-files-label:
  .. table:: *Logging Configuration Files*

   +--------+---------------------------------+-----------------------------------+
   |Logging |Configuration                    |Description                        |
   |Type    +----------------+----------------+-----------------------------------+
   |        |File            |Directory       |                                   |
   +========+================+=========+======+===================================+
   |standard|log.standard.yml|ka_uts_com/data |the Python Logger compatible       |
   |        |                |                |standard Yaml configuraration file |
   |        |                |                |is used to define standard logging |
   +--------+----------------+                +-----------------------------------+
   |personal|log.personal.yml|                |the Python Logger compatible       | 
   |        |                |                |personal Yaml configuration file   |
   |        |                |                |is used to define personal logging |
   +--------+----------------+----------------+-----------------------------------+

Modules
*******

Classification
==============

The Modules of Package ``ka_uts_dic`` could be classified in the follwing module classes:

#. *Dictionary Management Modules*

Dictionary management Modules
-----------------------------

  .. modules-for-dictionary-magement-label:
  .. table:: *Modules for dictionary management*

   +----------------------------+------------------------------------------------+
   |Module                      |Static Classes                                  |
   +-----------+----------------+-----------+------------------------------------+
   |Name       |Type            |Name       |Description                         |
   +===========+================+===========+====================================+
   |d2v        |Array with      |D2V        |                                    |
   |           |2-dimensinal    |           |                                    |
   |           |array as keys   |           |                                    |
   +-----------+----------------+-----------+------------------------------------+
   |d3v        |Array with      |D3V        |                                    |
   |           |3-dimensinal    |           |                                    |
   |           |array as keys   |           |                                    |
   +-----------+----------------+-----------+------------------------------------+
   |dic        |Dictionary      |Dic        |                                    |
   +-----------+----------------+-----------+------------------------------------+
   |doa        |Dictionary of   |DoA        |                                    |
   |           |Arrays          |           |                                    |
   +-----------+----------------+-----------+------------------------------------+
   |dod        |Dictionary of   |AoD        |                                    |
   |           |Dictionaries    |           |                                    |
   +-----------+----------------+-----------+------------------------------------+
   |doo        |Dictionary of   |DoO        |                                    |
   |           |Objects         |           |                                    |
   +-----------+----------------+-----------+------------------------------------+

Appendix
========

.. contents:: **Table of Content**
