#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the address of a pointer to the head node of the singly
 *	  linked list.
 * @number: the integer to be inserted.
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *prev = NULL, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->next = NULL;
	new->n = number;

	while (curr)
	{
		if (curr->n >= number)
		{
			if (!prev)
			{
				new->next = curr;
				*head = new;
				return (new);
			}
			else
			{
				prev->next = new;
				new->next = curr;
				return (new);
			}

		}
		prev = curr;
		curr = curr->next;
	}
	if (prev)
		prev->next = new;
	else
		*head = new

	return (new);
}

