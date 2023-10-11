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
	long int size;
	int i;
	char *string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &string, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", string);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", string[i]);
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
	long int size = PyList_Size(p);
	int i;
	PyListObject *list_t = (PyListObject *)p;
	const char *pl;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_t->allocated);
	for (i = 0; i < size; i++)
	{
		pl = (list_t->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, pl);
		if (!strcmp(pl, "bytes"))
			print_python_bytes(list_t->ob_item[i]);
	}
}
