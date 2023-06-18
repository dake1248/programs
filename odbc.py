import pyodbc
print([x for x in pyodbc.drivers() if x.startswith('Microsoft')] )

import timeit
a=timeit.timeit()
print(a.timeit(for i in range(1000):))
