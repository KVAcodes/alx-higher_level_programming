#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to a list Object.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	if (p == NULL)
		return;
	int index;
	int allocated = ((PyListObject *)p)->allocated, size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	index = 0;
	while (index < size)
	{
		printf("Element %d: %s\n", index,
				Py_TYPE(PyList_GetItem(p, index))->tp_name);
		index++;
	}
}
