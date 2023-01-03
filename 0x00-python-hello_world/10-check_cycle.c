#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a loop.
 * @list: The head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list, *tortoise = list;

	while (hare && hare->next && hare->next->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
			return (1);
	}
	return (0);
}
