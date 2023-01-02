#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * in it.
 * @list: The head(address of the first node).
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL)
	{
		return (0);
	}

	while ((hare != NULL) && (hare->next != NULL))
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
