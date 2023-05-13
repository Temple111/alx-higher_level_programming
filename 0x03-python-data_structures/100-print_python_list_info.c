#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sz, allc, a;
	PyObject *objt;

	sz = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", allc);

	for (a = 0; a < sz; a++)
	{
		printf("Element %d: ", a);

		objt = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(objt)->tp_name);
	}
}
