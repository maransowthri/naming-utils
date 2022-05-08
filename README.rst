naming-utils
============

Simple utility for generating unique names with timestamps.

Installation
------------

.. code:: bash

   pip install naming-utils

Usage
-----

.. code:: bash

   >>> from naming_utils import unique_name_with_ts
   >>> unique_name_with_ts()

   '20220508_085805_173693933'
   
   >>> unique_name_with_ts(path='log/', extension='log')
   
   'log/20220508_085837_602718269.log'
   
   >>> from naming_utils import unique_names_with_ts
   >>> unique_names_with_ts(count=5, path='log/', extension='log')
   
   ['log/20220508_085901_689713589.log', 'log/20220508_085901_689713339.log', 'log/20220508_085901_68971329.log', 'log/20220508_085901_689713292.log', 'log/20220508_085901_688709138.log']
