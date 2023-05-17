#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	long int sz;
	int a;
	char *try_string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_string, &sz);

	printf("  size: %li\n", sz);
	printf("  trying string: %s\n", try_string);
	if (sz < 10)
		printf("  first %li bytes:", sz + 1);
	else
		printf("  first 10 bytes:");
	for (a = 0; a <= sz && a < 10; a++)
		printf(" %02hhx", try_string[a]);
	printf("\n");
}
/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	long int sz = PyList_Size(p);
	int a;
	PyListObject *lt = (PyListObject *)p;
	const char *tp;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", lt->allocated);
	for (a = 0; a < sz; a++)
	{
		tp = (lt->ob_item[a])->ob_type->tp_name;
		printf("Element %i: %s\n", a, tp);
		if (!strcmp(tp, "bytes"))
			print_python_bytes(lt->ob_item[a]);
	}
}
