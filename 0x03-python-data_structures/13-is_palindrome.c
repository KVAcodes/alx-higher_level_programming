#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a
 * a palindrome.
 * @head : address of the pointer to the head node of the
 * linked list
 *
 * Return: 0 if it is not a palindrome. 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *backward = *head, *forward = *head;
	listint_t **backwards, **forwards;

	if (!(*head))
		return (1);

	backwards = &backward;
	forwards = &forward;

	if (is_palindrome_recursive(backwards, forwards))
		return (1);

	return (0);
}

/**
 * is_palindrome_recursive - recursively checks if the nodes
 * contain the same values from the tail to the head of the linked list
 * and vice-versa.
 * @backwards: address of the pointer going from the tail to the head.
 * @forwards: address of the pointer going from the head to the tail.
 *
 * Return: 0 if any difference is noticed else if none is noticed 1 is
 * returned
 */
int is_palindrome_recursive(listint_t **backwards, listint_t **forwards)
{
	int ret;
	listint_t *current = *backwards;

	if ((*backwards)->next)
	{
		*backwards = (*backwards)->next;
		ret = is_palindrome_recursive(backwards, forwards);
		if (!ret)
			return (0);
	}
	if (current->n == (*forwards)->n)
	{
		*forwards = (*forwards)->next;
		return (1);
	}
	return (0);
}
