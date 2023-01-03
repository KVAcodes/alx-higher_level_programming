#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the pointer to the first node in the list.
 * @number: the number given to insert.
 *
 * Return: the address of the new node,
 * Otherwise returns NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if ((ptr == NULL) || (number < ptr->n))
	{
		new->next = ptr;
		*head = new;
		return (new);
	}

	while (ptr && ptr->next && (ptr->next->n < number))
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
