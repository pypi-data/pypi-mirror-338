##########
ka_uts_com
##########

Overview
********

.. start short_desc

**Communication Utilities**

.. end short_desc

Installation
************

.. start installation

The package ``ka_uts_com`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: shell

	$ python -m pip install ka_uts_com

To install with ``conda``:

.. code-block:: shell

	$ conda install -c conda-forge ka_uts_com

.. end installation

This requires that the ``readme`` extra is installed:

.. code-block:: bash

	$ python -m pip install ka_uts_com[readme]

Package logging
***************

Standard or user specific Package logging of application package is defined
in the static logging class **Log_** of Base module log\_.py of the Communication
Package **ka_uts_com**.
The default Logging configuration is defined by the yaml files **log.std.yml**
for standard Logging or **log.user.yml** for user Logging in the data directory
**/ka_uts_com/data** of the Communication package.
The Logging configuration could be overriden by yaml files with the same names in the
data directory **<application>/data** of the application packages.

Logging defines log file paths for the following log message types: .

#. *debug*
#. *error*
#. *info*
#. *log*

  .. Naming-conventions-for-logging-files-label:
  .. table:: *Naming conventions for logging file*

   +-----+--------------------------------------------+-------------------+
   |Type |Directory                                   |File               |
   +=====+============================================+===================+
   |debug|/data/<tenant>/RUN/<package>/<function>/debs|debs_<pid>_<ts>.log|
   +-----+--------------------------------------------+-------------------+
   |error|/data/<tenant>/RUN/<package>/<function>/errs|errs_<pid>_<ts>.log|
   +-----+--------------------------------------------+-------------------+
   |info |/data/<tenant>/RUN/<package>/<function>/logs|info_<pid>_<ts>.log|
   +-----+--------------------------------------------+-------------------+
   |log  |/data/<tenant>/RUN/<package>/<function>/logs|logs_<pid>_<ts>.log|
   +-----+--------------------------------------------+-------------------+

  .. Naming examples-of-logging-files-label:
  .. table:: *Naming examples of logging file*

   +-----+-------------------------------+------------------------+
   |Type |Directory                      |File                    |
   +=====+===============================+========================+
   |debug|/data/umh/RUN/umh_otec/srr/debs|debs_9470_1737118199.log|
   +-----+-------------------------------+------------------------+
   |error|/data/umh/RUN/umh_otec/srr/errs|errs_9470_1737118199.log|
   +-----+-------------------------------+------------------------+
   |info |/data/umh/RUN/umh_otec/srr/logs|info_9470_1737118199.log|
   +-----+-------------------------------+------------------------+
   |log  |/data/umh/RUN/umh_otec/srr/logs|logs_9470_1737118199.log|
   +-----+-------------------------------+------------------------+

Package files
*************

Classification
==============

The Files of Package ``ka_uts_com`` could be classified into the follwing file types:

#. *Special files*
#. *Dunder modules*
#. *Decorator modules*
#. *Data files*
#. *Package modules*

Special files
*************

  .. Special-file-label:
  .. table:: *Special-file*

   +--------+--------+---------------------------------------------------+
   |Name    |Type    |Description                                        |
   +========+========+===================================================+
   |py.typed|Type    |The py.typed file is a marker file used in Python  |
   |        |checking|packages to indicate that the package supports type|
   |        |marker  |checking. This file is a part of the PEP 561       |
   |        |file    |standard, which provides a standardized way to     |
   |        |        |package and distribute type information in Python. |
   +--------+--------+---------------------------------------------------+

Dunder Modules
**************

  .. Dunder-modules-label:
  .. table:: *Dunder-Modules*

   +--------------+---------+----------------------------------------------------+
   |Name          |Type     |Description                                         |
   +==============+=========+====================================================+
   |__init__.py   |Package  |The module is used to execute initialisation code or|
   |              |directory|mark the directory it contains as a package. The    | 
   |              |marker   |Module enforces explicit imports and thus clear     |
   |              |file     |namespace use and call them with the dot notation.  |
   +--------------+---------+----------------------------------------------------+
   |__version__.py|Version  |The module consist of Assignment Statements for     |
   |              |file     |system Variables used in Versioning.                |
   +--------------+---------+----------------------------------------------------+

Decorator Modules
*****************

Overview
========

  .. Decorator Modules-label:
  .. table:: **Decorator Modules**

   +------+-----------------+
   |Name  |Decription       |
   +======+=================+
   |dec.py|Decorators module|
   +------+-----------------+

Data Files
**********

  .. Data-Files-label:
  .. table:: **Data Files**

   +-----------+-----------------------------------------+
   |Name       |Description                              |
   +===========+=========================================+
   |log.std.yml|Yaml definition file for standard logging|
   +-----------+-----------------------------------------+
   |log.usr.yml|Yaml definition file for user logging    |
   +-----------+-----------------------------------------+

Package Modules
***************

Classification
==============

The Modules of Package ``ka_uts_com`` could be classified into the following module types:

#. **Communication Modules**
#. **Base Modules**
#. **Utility Modules**
#. **I/O Control Modules**

Communication Modules
=====================

Overview
--------

  .. Communication Modules-label:
  .. table:: **Communication Modules**

   +--------+-----------------------------+
   |Name    |Decription                   |
   +========+=============================+
   |com.py  |Communication handling module|
   +--------+-----------------------------+
   |fnc.py  |Function Management module   |
   +--------+-----------------------------+
   |log.py  |Logging management module    |
   +--------+-----------------------------+
   |timer.py|Timer management module      |
   +--------+-----------------------------+

Communication module: com.py
============================

The Communication handling Module ``com.py`` contains the single static class ``Com``.

Com (static class of com.py)
----------------------------

The static Class ``Com`` contains the subsequent variables and methods.

Com Variables
^^^^^^^^^^^^^

  .. Variables-of-class-Com-label:
  .. table:: **Variables of class Com**

   +--------+-----------+-------+-----------------------------------+
   |Name    |Type       |Default|Description                        |
   +========+===========+=======+===================================+
   |cfg     |TyDic      |None   |Configuration dictionary           |
   +--------+-----------+-------+-----------------------------------+
   |d_pacmod|TyDic      |{}     |pacmod dictionary                  |
   +--------+-----------+-------+-----------------------------------+
   |pid     |TyInt      |None   |Process id                         |
   +--------+-----------+-------+-----------------------------------+
   |sw_init |TyBool     |None   |Initialisation switch              |
   +--------+-----------+-------+-----------------------------------+
   |ts      |TnTimeStamp|None   |Timestamp                          |
   +--------+-----------+-------+-----------------------------------+
   |ts_start|TnDateTime |None   |start timestamp in date time format|
   +--------+-----------+-------+-----------------------------------+
   |ts_end  |TnDateTime |None   |end timestamp in date time format  |
   +--------+-----------+-------+-----------------------------------+
   |ts_etime|TnDateTime |None   |elapse Time                        |
   +--------+-----------+-------+-----------------------------------+
   |d_timer |TyDic      |False  |Timer dictionary                   |
   +--------+-----------+-------+-----------------------------------+
   |Log     |TyLogger   |False  |Log class                          |
   +--------+-----------+-------+-----------------------------------+
   |App     |TyAny      |False  |Application class                  |
   +--------+-----------+-------+-----------------------------------+
   |Exit    |TyAny      |False  |Exit class                         |
   +--------+-----------+-------+-----------------------------------+

Com Methods
^^^^^^^^^^^

  .. Methods-of-class-Com-label:
  .. table:: **Methods of class Com**

   +---------+-------------------------------------------------------+
   |Name     |Description                                            |
   +=========+=======================================================+
   |init     |initialise static variables if they are not initialized|
   +---------+-------------------------------------------------------+
   |sh_kwargs|show keyword arguments                                 |
   +---------+-------------------------------------------------------+

Com Method: init
^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-Com-method-init-label:
  .. table:: **Parameter of Com method init**

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|keyword arguments|
   +---------+-----+-----------------+

Com Method: sh_kwargs
^^^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Paramter-of-Com-method-sh_kwargs-label:
  .. table:: **Parameter of Com method sh_kwargs**

   +--------+-----+--------------------+
   |Name    |Type |Description         |
   +========+=====+====================+
   |cls     |class|current class       |
   +--------+-----+--------------------+
   |root_cls|class|root lass           |
   +--------+-----+--------------------+
   |d_parms |TyDic|parameter dictionary|
   +--------+-----+--------------------+
   |\*args  |list |arguments array     |
   +--------+-----+--------------------+

Function Module: fnc.py
=======================

The Module ``fnc.py`` contains one static class ``Fnc`` with I/O Control methods for log files;

fnc.py Class: Fnc
-----------------

The static Class ``Fnc`` contains the subsequent methods

Fnc Methods
^^^^^^^^^^^

  .. Methods-of-Fnc-class-label:
  .. table:: Methods of Fnc class*

   +--------+------+------------------------------------------------------------+
   |Name    |Type  |Description                                                 |
   +========+======+============================================================+
   |identity|static|Identity function for objects                               |       
   +--------+------+------------------------------------------------------------+
   |sh      |static|Show function localised in the given dictionary of functions|       
   |        |      |by the given key                                            |       
   +--------+------+------------------------------------------------------------+
   |ex      |class |Execute the function localised by the show function of class|       
   |        |      |Fnc using the given key and dictionary of functions         |       
   +--------+------+------------------------------------------------------------+

Fnc Method: identity
^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-identity-method-label:
  .. table:: Parameter of identity method*

   +----+-----+-----------+
   |Name|Type |Description|
   +====+=====+===========+
   |obj |TyAny|object     |
   +----+-----+-----------+

Return Value
""""""""""""

  .. Return values-of-identity-method-label:
  .. table:: **Return values of identity-method**

   +----+-----+-----------+
   |Name|Type |Description|
   +====+=====+===========+
   |obj |TyAny|object     |
   +----+-----+-----------+

Fnc Method: ex
^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-ex-method-label:
  .. table:: Parameter of ex method*

   +-----------+--------+------------------------------+
   |Name       |Type    |Description                   |
   +===========+========+==============================+
   |cls        |class   |current class                 |
   +-----------+--------+------------------------------+
   |doc        |TnDoC   |Dictionary of Callables       |
   +-----------+--------+------------------------------+
   |key        |TnDoc   |key                           |
   +-----------+--------+------------------------------+
   |args_kwargs|TnArrDoc|arguments or keyword arguments|
   +-----------+--------+------------------------------+

Return Value
""""""""""""

  .. Return value-of-ex-method-label:
  .. table:: *Return value of ex method*

   +----+----------+------------------------------------------+
   |Name|Type      |Description                               |
   +====+==========+==========================================+
   |    |TyCallable|Value of Function for argument args_kwargs|
   +----+----------+------------------------------------------+

Fnc Method: sh
^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-sh-method-label:
  .. table:: Parameter of sh method*

   +----+-----+------------------------------+
   |Name|Type |Description                   |
   +====+=====+==============================+
   |cls |class|current class                 |
   +----+-----+------------------------------+
   |doc |TnDoC|Dictionary of Callables       |
   +----+-----+------------------------------+
   |key |TnDoc|key                           |
   +----+-----+------------------------------+

Return Value
""""""""""""

  .. Return value-of-sh-method-label:
  .. table:: *Return value of sh method*

   +----+----------+-----------+
   |Name|Type      |Description|
   +====+==========+===========+
   |fnc |TyCallable|Function   |
   +----+----------+-----------+

Communicstion Module: log.py
============================

The Module ``log.py`` contains one static class ``Log`` with I/O Control methods for log files;

log.py Class: Log
-----------------

The static Class ``Log`` contains the subsequent sub classes and methods

Sub-Classes
^^^^^^^^^^^

The Class ``Log`` contains the following static sub-classes.

  .. Static-Log-sub-classes-label:
  .. table:: *Static Log sub classes*

   +----+----------------------------------------------------+
   |Name|Description                                         |
   +====+====================================================+
   |Eq  |Log generated Equate messages                       |
   +----+----------------------------------------------------+
   |Dic |Log generated Equate messages for dictionary entries|
   +----+----------------------------------------------------+

Log Sub-Class: Eq
^^^^^^^^^^^^^^^^^

Log-Eq Methods
""""""""""""""

  .. Methods-of-Log-Eq-subclass-label:
  .. table:: *Methods of Log.Eq subclass*

   +-----+----------------------------------------------+
   |Name |Description                                   |
   +=====+==============================================+
   |debug|Log generated equate message "<key> = <value>"|       
   |     |to the debug destination                      |       
   +-----+----------------------------------------------+
   |error|Log generated equate message "<key> = <value>"|       
   |     |to the error destination                      |       
   +-----+----------------------------------------------+
   |info |Log generated equate message "<key> = <value>"|       
   |     |to the info destination                       |       
   +-----+----------------------------------------------+
   |debug|Log generated equate message "<key> = <value>"|       
   |     |to the warning destination                    |       
   +-----+----------------------------------------------+

All Methods use the following Parameter:

Parameter
"""""""""

  .. Parameter-of-Log-Eq-methods-label:
  .. table:: *Parameter of Log.Eq methods*

   +-----+-----+-------------+
   |Name |Type |Description  |
   +=====+=====+=============+
   |cls  |class|current class|
   +-----+-----+-------------+
   |key  |TyAny|Key          |
   +-----+-----+-------------+
   |value|TyAny|Value        |
   +-----+-----+-------------+

Log Sub-Class: Dic
^^^^^^^^^^^^^^^^^^

Log-Dic Methods
"""""""""""""""

  .. Methods-of-Log-Dic-methods-label:
  .. table:: *Methods of Log.Dic methods*

   +-------+------------------------------------------------+
   |Name   |Description                                     |
   +=======+================================================+
   |debug  |Log generated equate messages for all dictionary|       
   |       |entries to the debug destination                |      
   +-------+------------------------------------------------+
   |error  |Log generated equate messages for all dictionary|       
   |       |entries to the error destination                |       
   +-------+------------------------------------------------+
   |info   |Log generated equate messages for all dictionary|       
   |       |entries to the info destination                 |       
   +-------+------------------------------------------------+
   |warning|Log generated equate messages for all dictionary|       
   |       |entries to the warning destination              |       
   +-------+------------------------------------------------+

All Log-Dic Methods use the following Parameters:

Parameter
"""""""""

  .. Parameter-of-Com-Eq-methods-label:
  .. table:: *Parameter of Com.Eq methods*

   +----+-----+-------------+
   |Name|Type |Description  |
   +====+=====+=============+
   |cls |class|current class|
   +----+-----+-------------+
   |dic |TyDic|Dictionary   |
   +----+-----+-------------+

Methods
^^^^^^^

  .. Methods-of-Log-class-label:
  .. table:: *Methods of Log class*

   +-------+-----------------------------------------------------------+
   |Name   |Description                                                |
   +=======+===========================================================+
   |debug  |Setup stacklevel and log message to the debug destination  |      
   +-------+-----------------------------------------------------------+
   |error  |Setup stacklevel and log message to the error destination  |      
   +-------+-----------------------------------------------------------+
   |info   |Setup stacklevel and log message to the info destination   |      
   +-------+-----------------------------------------------------------+
   |warning|Setup stacklevel and log message to the warning destination|      
   +-------+-----------------------------------------------------------+

Parameter
"""""""""

  .. Parameter-of-Com-methods-label:
  .. table:: *Parameter of Com methods*

   +----+-----+-------------+
   |Name|Type |Description  |
   +====+=====+=============+
   |cls |class|current class|
   +----+-----+-------------+
   |dic |TyDic|Dictionary   |
   +----+-----+-------------+

timer.py
========

Static classes
--------------

The Module ``timer.py`` contains the following classes


  .. Static-classes-of-module-timer-label:
  .. table:: *Static classes of module timer.py*

   +---------+---------------+
   |Name     |Description    |
   +=========+===============+
   |Timestamp|Timestamp class|
   +---------+---------------+
   |Timer    |Timer class    |
   +---------+---------------+


timer.py Class: Timer
---------------------

Timer Methods
^^^^^^^^^^^^^

  .. Methods-of-Timer-label:
  .. table:: *Methods of Timer*

   +----------+-------------------------------------------+
   |Name      |Description                                |
   +==========+======+====================================+
   |sh_task_id|static|Show task id                        |
   +----------+------+------------------------------------+
   |start     |class |Start Timer                         |
   +----------+------+------------------------------------+
   |end       |class |End Timer and Log Timer info message|
   +----------+------+------------------------------------+

Timer Method: sh_task_id
^^^^^^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-Timer-sh_task_id-method-label:
  .. table:: *Parameter of Timer sh_task_id method*

   +--------+-----+-----------------+
   |Name    |Type |Description      |
   +========+=====+=================+
   |d_pacmod|TyDic|pacmod dictionary|
   +--------+-----+-----------------+
   |class_id|TyAny|Class Id         |
   +--------+-----+-----------------+
   |parms   |TnAny|Parameter        |
   +--------+-----+-----------------+
   |sep     |TyStr|Separator        |
   +--------+-----+-----------------+

Return Value
""""""""""""

  .. Return values-of-Timer-sh_task_id-method-label:
  .. table:: *Return values of Timer sh_task_id method*

   +----+-----+-----------+
   |Name|Type |Description|
   +====+=====+===========+
   |    |TyStr|Task Id    |
   +----+-----+-----------+

Timer Method: start
^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-start-method-label:
  .. table:: *Parameter of start method*

   +--------+-----+-------------+
   |Name    |Type |Description  |
   +========+=====+=============+
   |cls     |class|current class|
   +--------+-----+-------------+
   |class_id|TyAny|Class Id     |
   +--------+-----+-------------+
   |parms   |TnAny|Parameter    |
   +--------+-----+-------------+
   |sep     |TyStr|Separator    |
   +--------+-----+-------------+

Timer Method: end
^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-end-method-label:
  .. table:: *Parameter of end method*

   +--------+-----+-------------+
   |Name    |Type |Description  |
   +========+=====+=============+
   |cls     |class|current class|
   +--------+-----+-------------+
   |class_id|TyAny|Class Id     |
   +--------+-----+-------------+
   |parms   |TnAny|Parameter    |
   +--------+-----+-------------+
   |sep     |TyStr|Separator    |
   +--------+-----+-------------+

Base Modules
************

Overview
========

  .. Base Modules-label:
  .. table:: *Base Modules*

   +---------+----------------------------+
   |Name     |Decription                  |
   +=========+============================+
   |app\_.py |Application setup module    |
   +---------+----------------------------+
   |cfg\_.py |Configuration setup module  |
   +---------+----------------------------+
   |exit\_.py|Exit Manafement setup module|
   +---------+----------------------------+
   |log\_.py |Log management setup module |
   +---------+----------------------------+

Application setup module: app\_.py
==================================

The Module ``app.py`` contains a single static class ``App_``.

appl\_.py Class: App\_
----------------------

The static class ``App_`` contains the subsequent static variables and methods

Appl\_ Static Variables
^^^^^^^^^^^^^^^^^^^^^^^

  .. Static-variables-of-App_-label:
  .. table:: *Static Variables of App_*

   +---------------+-------+-------+---------------------+
   |Name           |Type   |Default|Description          |
   +===============+=======+=======+=====================+
   |sw_init        |TyBool |False  |initialisation switch|
   +---------------+-------+-------+---------------------+
   |httpmod        |TyDic  |None   |http modus           |
   +---------------+-------+-------+---------------------+
   |sw_replace_keys|TnBool |False  |replace keys switch  |
   +---------------+-------+-------+---------------------+
   |keys           |TnArr  |None   |Keys array           |
   +---------------+-------+-------+---------------------+
   |reqs           |TyDic  |None   |Requests dictionary  |
   +---------------+-------+-------+---------------------+
   |app            |TyDic  |None   |Appliction dictionary|
   +---------------+-------+-------+---------------------+

Appl\_ Methods
^^^^^^^^^^^^^^

  .. Methods-of-App_-label:
  .. table:: *Methods of App_*

   +----+------+------------------------------------+
   |Name|Method|Description                         |
   +====+======+====================================+
   |init|class |initialise static variables of class|
   |    |      |if they are not allready initialized|
   +----+------+------------------------------------+
   |sh  |class |show (return) class                 |
   +----+------+------------------------------------+

Appl\_ Method: init
^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-init-label:
  .. table:: *Parameter of init*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|Current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|Keyword arguments|
   +---------+-----+-----------------+

Appl\_ Method: sh
^^^^^^^^^^^^^^^^^
        
  .. Parameter-of-sh-label:
  .. table:: *Parameter of sh*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|Current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|Keyword arguments|
   +---------+-----+-----------------+

Return Value
""""""""""""

  .. Return-values-of_sh-label:
  .. table:: *Return values of sh*

   +----+--------+-----------+
   |Name|Type    |Description|
   +====+========+===========+
   |log |TyLogger|Logger     |
   +----+--------+-----------+

cfg\_.py
========

The Base module cfg\_.py contains a single static class ``Cfg_``.

Cfg\_ (Static class of Base Module cfg\_.py)
--------------------------------------------

The static class ``Cfg_`` contains the subsequent static variables and methods

Static Variables
^^^^^^^^^^^^^^^^

  .. Static-variables-of-Cfg_-label:
  .. table:: *Static Variables of Cfg_*

   +----+-----+-------+--------------------+
   |Name|Type |Default|Description         |
   +====+=====+=======+====================+
   |cfg |TyDic|None   |Configuration object|
   +----+-----+-------+--------------------+

Cfg\_ Methods
^^^^^^^^^^^^^

  .. Methods-of-Cfg_-label:
  .. table:: *Methods of Cfg_*

   +----+------+-----------------------------------+
   |Name|Method|Description                        |
   +====+======+===================================+
   |sh  |class |read pacmod yaml file into class   |
   |    |      |variable cls.dic and return cls.cfg|
   +----+------+-----------------------------------+

Cfg\_ Method: sh
^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-init-label:
  .. table:: *Parameter of sh*

   +--------+--------+-----------------+
   |Name    |Type    |Description      |
   +========+========+=================+
   |cls     |class   |Current class    |
   +--------+--------+-----------------+
   |log     |TyLogger|Logger           |
   +--------+--------+-----------------+
   |d_pacmod|TyDic   |pacmod dictionary|
   +--------+--------+-----------------+

Return Value
""""""""""""

  .. Return-values-of-sh-label:
  .. table:: *Return values of sh*

   +-------+-----+-----------+
   |Name   |Type |Description|
   +=======+=====+===========+
   |cls.cfg|TyDic|           |
   +-------+-----+-----------+

exit\_.py
=========

The Base module exit\_.py contains a single static class ``Exit_``.

Exit\_ (Static class of Base module exit\_.py)
----------------------------------------------

The static Class ``Exit_`` contains the subsequent static variables and methods.

Exit\_ Static Variables
^^^^^^^^^^^^^^^^^^^^^^^

  .. Exit_-Static variables-label:
  .. table:: *Exit_ Static variables*

   +--------------+------+-------+---------------------+
   |Name          |Type  |Default|Description          |
   +==============+======+=======+=====================+
   |sw_init       |TyBool|False  |initialisation switch|
   +--------------+------+-------+---------------------+
   |sw_critical   |TyBool|False  |critical switch      |
   +--------------+------+-------+---------------------+
   |sw_stop       |TyBool|False  |stop switch          |
   +--------------+------+-------+---------------------+
   |sw_interactive|TyBool|False  |interactive switch   |
   +--------------+------+-------+---------------------+

Exit\_ Methods
^^^^^^^^^^^^^^

  .. Exit_-Methods-label:
  .. table:: *Exit_ Methods*

   +----+------+------------------------------------+
   |Name|Method|Description                         |
   +====+======+====================================+
   |init|class |initialise static variables of class|
   |    |      |if they are not allready initialized|
   +----+------+------------------------------------+
   |sh  |class |show (return) class                 |
   +----+------+------------------------------------+

Exit\_ Method: init
^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-init-label:
  .. table:: *Parameter of init*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|Current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|Keyword arguments|
   +---------+-----+-----------------+

Exit\_ Method: sh
^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-sh-label:
  .. table:: *Parameter of sh*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|Current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|Keyword arguments|
   +---------+-----+-----------------+

Return Value
""""""""""""

  .. Return-values-of-sh-label:
  .. table:: *Return values of sh*

   +----+-----+-------------+
   |Name|Type |Description  |
   +====+=====+=============+
   |cls |class|Current class|
   +----+-----+-------------+

log\_.py
========

The Base module log\_.py contains a single static class ``Log_``.

Log\_ (Static class of Base module log\_.py)
--------------------------------------------

The static Class ``Log_`` contains the subsequent static variables and methods.

Log\_ Static Variables
^^^^^^^^^^^^^^^^^^^^^^

  .. Static variables-of-Log_-label:
  .. table:: *Static variables of Log_*

   +--------+--------+---------------------------------+---------------------+
   |Name    |Type    |Default                          |Description          |
   +========+========+=================================+=====================+
   |sw_init |TyBool  |False                            |initialisation switch|
   +--------+--------+---------------------------------+---------------------+
   |log     |TyLogger|logging.getLogger('dummy_logger')|Logger               |
   +--------+--------+---------------------------------+---------------------+
   |username|TyStr   |psutil.Process().username()      |current username     |
   +--------+--------+---------------------------------+---------------------+

Log\_ Methods
^^^^^^^^^^^^^

  .. Methods-of-class-Log_-label:
  .. table:: *Methods of class Log_*

   +------+------+-------------------------------------+
   |Name  |Method|Description                          |
   +======+======+=====================================+
   |init  |class |initialise static variables of class |
   |      |      |if they are not allready initialized.|
   +------+------+-------------------------------------+
   |sh_cfg|class |Read configuration template into     |
   |      |      |configuration dictionary and return  |
   |      |      |changed configuration dictionary.    |
   +------+------+-------------------------------------+
   |sh    |class |show (return) current class          |
   +------+------+-------------------------------------+

Log\_ Method: init
^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-init-label:
  .. table:: *Parameter of init*

   +---------+-----+-------------------+
   |Name     |Type |Description        |
   +=========+=====+===================+
   |cls      |class|Current class      |
   +---------+-----+-------------------+
   |com      |class|Communication class|
   +---------+-----+-------------------+
   |\**kwargs|TyAny|Keyword arguments  |
   +---------+-----+-------------------+

Log\_ Method: sh_cfg
^^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-sh_cfg-label:
  .. table:: *Parameter of sh_cfg*

   +---------+-----+-------------------+
   |Name     |Type |Description        |
   +=========+=====+===================+
   |cls      |class|Current class      |
   +---------+-----+-------------------+
   |com      |class|Communication class|
   +---------+-----+-------------------+
   |\**kwargs|TyAny|Keyword arguments  |
   +---------+-----+-------------------+

Return Value
""""""""""""

  .. Return-values-of-sh-label:
  .. table:: *Return values of sh*

   +----+-----+-------------+
   |Name|Type |Description  |
   +====+=====+=============+
   |cls |class|Current class|
   +----+-----+-------------+

sh (Method of class Log\_)
^^^^^^^^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-sh-label:
  .. table:: *Parameter of sh*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|Current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|Keyword arguments|
   +---------+-----+-----------------+

Return Value
""""""""""""

  .. Return-values-of-sh-label:
  .. table:: *Return values of sh*

   +----+-----+-------------+
   |Name|Type |Description  |
   +====+=====+=============+
   |cls |class|Current class|
   +----+-----+-------------+

Utility Modules
***************

Overview
========

  .. Utility-Modules-label:
  .. table:: *Utility Modules*

   +-----------+--------------------------------+
   |Name       |Functionality                   |
   +===========+================================+
   |aoeqstmt.py|Manage array of equate statement|
   +-----------+--------------------------------+
   |date.py    |Manage dates                    |
   +-----------+--------------------------------+
   |doeq.py    |Manage dictionary of equates    |
   +-----------+--------------------------------+
   |fnc.py     |Manage functions                |
   +-----------+--------------------------------+
   |pacmod.py  |Manage Packages and Modules     |
   +-----------+--------------------------------+
   |str.py     |Manage strings                  |
   +-----------+--------------------------------+

aoeqstmt.py
===========

Static classes
--------------

  .. Static-clasess-of-module-aoeqstmt-label:
  .. table:: *Static classes of Module aoeqstmt*

   +-------------------------------------------------------+
   |Static Class                                           |
   +---------+---------------------------------------------+
   |Name     |Description                                  |
   +=========+=============================================+
   |AoEqStmt |Manage Commandline Arguments as Equate String|
   +---------+---------------------------------------------+

aoeqtmt.py Class: AoEqStmt
--------------------------

The static Class ``AoEqStmt`` contains the subsequent variables and methods

AoEqStmt Variables
^^^^^^^^^^^^^^^^^^^

  .. Variables-of-AoEqStmt-class-label:
  .. table:: *Variables of AoEqStmt class*

   +----------------------------------------------------+
   |Static Variables                                    |
   +---------------+------+-------+---------------------+
   |Name           |Type  |Default|Description          |
   +===============+======+=======+=====================+
   |sw_init        |TyBool|False  |initialisation switch|
   +---------------+------+-------+---------------------+
   |httpmod        |TyDic |None   |http modus           |
   +---------------+------+-------+---------------------+
   |sw_replace_keys|TnBool|False  |replace keys switch  |
   +---------------+------+-------+---------------------+
   |keys           |TnArr |None   |Keys array           |
   +---------------+------+-------+---------------------+
   |reqs           |TyDic |None   |Requests dictionary  |
   +---------------+------+-------+---------------------+
   |app            |TyDic |None   |Appliction dictionary|
   +---------------+------+-------+---------------------+

AoEqStmt Methods
^^^^^^^^^^^^^^^^

  .. Methods-of-AoEqStmt-class-label:
  .. table:: *Methods of AoEqStmt class*

   +--------------+---------------------------------------------------------+
   |Name          |Description                                              |
   +==============+=========================================================+
   |_set_by_pacmod|set item "current pacmod dictionary" of equate dictionary|
   +--------------+---------------------------------------------------------+
   |_set_by_prof  |set item "show profile" of equate dictionary             |
   +--------------+---------------------------------------------------------+
   |sh            |set and show (return) equate dictionary                  |
   +--------------+---------------------------------------------------------+

AoEqStmt Method: _set_pacmod_curr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description
"""""""""""  

Set item "pacmod_curr" of equate dictionary using item "tenant".

Parameter
"""""""""

  .. Parameter-of-AoEqStmt-Method-set_pacmod_curr-label:
  .. table:: *Parameter Value of AoEqStmt method set_pacmod_curr*

   +--------+-----+---------------------+
   |Name    |Type |Description          |
   +========+=====+=====================+
   |d_eq    |TyDic|Dictionary of Equates|
   +--------+-----+---------------------+
   |root_cls|class|Root Class           |
   +--------+-----+---------------------+

AoEqStmt Method: _set_sh_prof
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description
"""""""""""

Set item "sh_prof" of equate dictionary using profile initialiation function.

Parameter
"""""""""

  .. Parameter-of-Argv-Method-set_sh_prof-label:
  .. table:: *Parameter Value of Argv method set_sh_prof*

   +-------+------+-------------------------------+
   |Name   |Type  |Description                    |
   +=======+======+===============================+
   |d_eq   |TyDic |Dictionary of Equates          |
   +-------+------+-------------------------------+
   |sh_prof|TyCall|Profile initialisation function|
   +-------+------+-------------------------------+

AoEqStmt Method: sh
^^^^^^^^^^^^^^^^^^^

Description
"""""""""""

Set and show (return) equate dictionary

Parameter
"""""""""

  .. Parameter-of-Argv-method-sh-label:
  .. table:: *Parameter Value of Argv method sh*

   +-------+------+-------------------------------+
   |Name   |Type  |Description                    |
   +=======+======+===============================+
   |a_s_eq |TyDic |Dictionary of Equates          |
   +-------+------+-------------------------------+
   |sh_prof|TyCall|Profile initialisation function|
   +-------+------+-------------------------------+

doeq.py
=======

The Module ``doeq.py`` contains a single static class ``DoEq``.

Modul doeq.py Class: DoEq
-------------------------

The static class ``DoEq`` is used to manage Commandline Arguments of Equate Strings.

DoEq Methods
^^^^^^^^^^^^

  .. Methods-of-static-class-DoEq-label:
  .. table:: *Methods of static class DoEq*

   +--------+--------------------------------------------------+
   |Name    |Description                                       |
   +========+==================================================+
   |sh_value|Show value of equate string provided by single    |
   |        |command line argument                             |
   +--------+--------------------------------------------------+
   |sh_d_eq |Show Dictionary created by parsing array of equate|
   |        |strings provided by commandline arguments         |
   +--------+--------------------------------------------------+

DoEq Method: sh_value
^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-sh_value-method-label:
  .. table:: *Parameter of sh_value method*

   +-------------+-----+-------------------------------------+
   |Name         |Type |Description                          |                
   +=============+=====+=====================================+
   |cls          |class|current class                        |
   +-------------+-----+-------------------------------------+
   |key          |TyStr|Key of equate string                 |
   +-------------+-----+-------------------------------------+
   |value        |TyAny|Value of equate string               |
   +-------------+-----+-------------------------------------+
   |d_valid_parms|TnDic|Dictionary of valid keys (parameters)|
   +-------------+-----+-------------------------------------+
   |cls          |class|current class                        |
   +-------------+-----+-------------------------------------+
   |a_s_eq       |TyArr|array of equate strings              |
   +-------------+-----+-------------------------------------+
   |d_valid_parms|TnDic|Dictionary of valid parameter-keys   |
   +-------------+-----+-------------------------------------+

Return Values
"""""""""""""

  .. Return-values-of-sh_value-method-label:
  .. table:: *Return values of sh_value method*

   +-----+-----+----------------------+
   |Name |Type |Description           | 
   +=====+=====+======================+
   |value|Any  |converted Value of the|
   |     |     |equate-string         |
   |     |     |according Value type  |
   |     |     |d_valid_parms         |
   +-----+-----+----------------------+
   |d_eq |TnDic|Dictiony of parameter |
   |     |     |key, values           |
   +-----+-----+----------------------+

Utility Module: pacmod.py
=========================

The Utility module pacmod.py contains a single static class ``PacMod``.

pacmod.py Class: PaMmod
-----------------------

PacMod Methods
^^^^^^^^^^^^^^

  .. PacMod-Methods-label:
  .. table:: *PacMod Methods*

   +-----------------+-------------------------------------------------+
   |Name             |Description                                      |
   +=================+=================================================+
   |sh_d_pacmod      |create and show (return) pacmod dictionary       |
   +-----------------+-------------------------------------------------+
   |sh_path_cfg_yaml |show pacmod file path of the yaml file           |
   |                 |<pacmod module>.yaml in the data directory of the|
   |                 |current module of the current package            |
   +-----------------+-------------------------------------------------+
   |sh_path_keys_yaml|show pacmod file path type for the yaml file     |
   |                 |keys.yml in the data directory of the current    |
   |                 |module of the current pacḱage                    |
   +-----------------+-------------------------------------------------+
   |sh_pacmod_type   |show pacmod type directory path                  |
   +-----------------+-------------------------------------------------+
   |sh_file_path     |show pacmod file path                            |
   +-----------------+-------------------------------------------------+
   |sh_pattern       |show pacmod file path pattern                    |
   +-----------------+-------------------------------------------------+
   |sh_path_cfg_log  |show file path of log configuration file         |
   +-----------------+-------------------------------------------------+
   |sh_d_pacmod      |show pacmod dictionary                           |
   +-----------------+-------------------------------------------------+

PacMod Method: sh_d_pacmod
^^^^^^^^^^^^^^^^^^^^^^^^^^
        
Parameter
"""""""""

  .. Parameter-of-module-sh_d_pacmod-label:
  .. table:: *Parameter of method sh_d_pacmod*

   +--------+-----+-----------------+
   |Name    |Type |Description      |
   +========+=====+=================+
   |root_cls|class|root class       |
   +--------+-----+-----------------+
   |tenant  |Any  |                 |
   +--------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-module-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +------+-----+-----------------+
   |Name  |Type |Description      |
   +======+=====+=================+
   |pacmod|TyDic|                 |
   +------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-module-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +------+-----+-----------------+
   |Name  |Type |Description      |
   +======+=====+=================+
   |pacmod|TyDic|                 |
   +------+-----+-----------------+
   |type\_|Tystr|                 |
   +------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-module-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +------+-----+-----------------+
   |Name  |Type |Description      |
   +======+=====+=================+
   |pacmod|TyDic|                 |
   +------+-----+-----------------+
   |type\_|str  |                 |
   +------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-module-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|current class    |
   +---------+-----+-----------------+
   |pacmod   |TyDic|                 |
   +---------+-----+-----------------+
   |type\_   |TyStr|                 |
   +---------+-----+-----------------+
   |suffix   |TyStr|                 |
   +---------+-----+-----------------+
   |pid      |TyStr|                 |
   +---------+-----+-----------------+
   |ts       |TyAny|                 |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|keyword arguments|
   +---------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-method-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |pacmod   |TyDic|                 |
   +---------+-----+-----------------+
   |type\_   |TyStr|                 |
   +---------+-----+-----------------+
   |suffix   |TyStr|                 |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|keyword arguments|
   +---------+-----+-----------------+
        
PacMod Method: sh_path_cfg_yaml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-method-sh_path_cfg_yaml-label:
  .. table:: *Parameter of method sh_path_cfg_yaml*

   +--------+-----+-----------------+
   |Name    |Type |Description      |
   +========+=====+=================+
   |pacmod  |TnDic|                 |     
   +--------+-----+-----------------+
   |filename|TyStr|                 |
   +--------+-----+-----------------+
        
PacMod Method: sh_d_pacmod
^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-method-sh_d_pacmod-label:
  .. table:: *Parameter of method sh_d_pacmod*

   +---------+-----+-----------------+
   |Name     |Type |Description      |
   +=========+=====+=================+
   |cls      |class|current class    |
   +---------+-----+-----------------+
   |\**kwargs|TyAny|keyword arguments|
   +---------+-----+-----------------+

I/O Control Modules
*******************

jinja2\_.py
===========

The Module ``jinja2_.py`` contains the single static class Jinja2

jinja2\_.py Class: Jinja2
-------------------------

The static Class ``Jinja2`` provides I/O Control methods for Jinja2 files;
it contains the subsequent methods.

Jinja2 Methods
^^^^^^^^^^^^^^

  .. Methods-of-static-class-Jinja2-label:
  .. table:: *Methods of static class Jinja2*

   +-------------+------------------------------+
   |Name         |Description                   |
   +=============+==============================+
   |read         |Read log file path with jinja |
   +-------------+------------------------------+
   |read_template|Read log file path with jinja2|       
   +-------------+------------------------------+

Jinja2 Method: read
^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-Jinja2-method-read-label:
  .. table:: *Parameter Value of Jinja2 method read*

   +--------+-----+---------------+
   |Name    |Type |Description    |
   +========+=====+===============+
   |pacmod  |TnDic|               |
   +--------+-----+---------------+
   |filename|str  |               |
   +--------+-----+---------------+

Jinja2 Method: read_template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-Jinja2-method-read-template-label:
  .. table:: *Parameter Value of Jinja2 method read template*

   +--------+-----+---------------+
   |Name    |Type |Description    |
   +========+=====+===============+
   |pacmod  |TnDic|               |
   +--------+-----+---------------+
   |filename|TnAny|               |
   +--------+-----+---------------+

yaml\_.py
=========

The Module ``yaml_.py`` contains one static class ``Yaml``

Module yaml.py Class: Yaml
--------------------------

The static Class ``Yaml`` provides I/O Control functions for Yaml files;
it contains the subsequent methods

Yaml Methods
^^^^^^^^^^^^

  .. Yaml-Methods-label:
  .. table:: *Yaml Methods*

   +----+------------------------------------------------------+
   |Name|Description                                           |
   +====+======================================================+
   |load|Load yaml string into any object using yaml loader.   |
   |    |Default is yaml.safeloader                            |
   +----+------------------------------------------------------+
   |read|Read yaml file path into any object using yaml loader.|
   |    |Default loader is yaml.safeloader                     |
   +----+------------------------------------------------------+

Yaml Method: load
^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-Yaml-method-load-label:
  .. table:: *Parameter Value of Yaml method load*

   +------+-----+--------------+
   |Name  |Type |Description   |
   +======+=====+==============+
   |string|TyStr|              |
   +------+-----+--------------+
   |loader|TyStr|              |
   +------+-----+--------------+

Yaml Method: read
^^^^^^^^^^^^^^^^^

Parameter
"""""""""

  .. Parameter-of-Yaml-method-read-label:
  .. table:: *Parameter Value of Yaml method read*

   +------+-----+--------------+
   |Name  |Type |Description   |
   +======+=====+==============+
   |path  |TyStr|              |
   +------+-----+--------------+
   |loader|TyStr|              |
   +------+-----+--------------+

Appendix
********

.. contents:: **Table of Content**
