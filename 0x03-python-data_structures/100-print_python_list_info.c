#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sz, aloc, ai
	PyObject *objt;

	sz = Py_SIZE(p);
	aloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", aloc);

	for (ai = 0; a < sz; ai++)
	{
		printf("Element %d: ", ai);

		objt = PyList_GetItem(p, ai);
		printf("%s\n", Py_TYPE(objt)->tp_name);
	}
}
