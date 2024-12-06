Usage
=====

.. _installation:
Installation
------------

To use the Chelexicon, first install it using pip:

.. code-block:: console

   (.venv) $ pip install chelexicon


Example
---------
This is an example of documenting a function from an .rst

.. py:function:: chelexicon.example_function(happy=True)

   Return a statement about happiness.

   :param happy: Are you happy?
   :type happy: bool
   :raise chelexicon.InvalidTypeError: Raised if the 'happy' argument is not boolean.
   :return: A sentence praising or encouraging you.
   :rtype: str

.. py:exception:: chelexicon.InvalidTypeError

   Raised when an incorrect type is used.