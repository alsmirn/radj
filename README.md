Radj
====

Rough russian adjectives detector written in python.


Satus
-----

Stable'n'rough.


Description
-----------

Use with Python=>2.6.

Radj represent the python class for russian adjectives forecasting.

**Input** - list of words (LOW).

**Output** - list of tuples (idx, type):
 * **idx** is index in input LOW,
 * **type** can be sum of codes: 1 (possessive), 3 (relative) or 5 (qualitative).


Warning
-------
Filter result with noun dictionary please ;).


Authors
-------

 * Lingvo: Sergeeva Elena <el.v.sergeeva@yandex.ru>
 * Programming: Alexey Smirnov <alsmirn@gmail.com>
