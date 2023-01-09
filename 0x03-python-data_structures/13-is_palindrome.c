#include "lists.h"

/**
 * length_of_list - finds the length of a singly linked list.
 * @head: a pointer to the first node of the list.
 *
 * Return: The length of the list.
 */
int length_of_list(listint_t *head)
{
	int count;
	listint_t *test_ptr = head;

	if (head == NULL)
	{
		return (0);
	}
	count = 1;

	while (test_ptr->next != NULL)
	{
		test_ptr = test_ptr->next;
		count++;
	}
	return (count);
}

/**
 * mid_node - finds the mid node in the list where
 * the list begins to repeat itself
 *
 * @head: a pointer to the first node of the list.
 * @length: the length of the list.
 *
 * Return: the pointer to the mid node of the list.
 */
listint_t *mid_node(listint_t *head, int length)
{
	int count, mid_position;
	listint_t *test_ptr = head;

	if (head == NULL || head->next == NULL)
		return (head);
	if (length % 2 == 0)
		mid_position = length / 2 + 1;
	else
		mid_position = length / 2 + 2;
	count = 1;
	while (count < mid_position)
	{
		test_ptr = test_ptr->next;
		count++;
	}
	return (test_ptr);
}

/**
 * reverse_list - reverses a list starting from the given
 * node.
 * @mid_node: the mid node of the list on which
 * to start reversal.
 *
 * Return: a pointer to the last node for reversal.
 */
listint_t *reverse_list(listint_t **mid_node)
{
	listint_t *tmp1 = *mid_node;
	listint_t *tmp2 = (*mid_node)->next;
	(*mid_node)->next = NULL;

	while (tmp1 != NULL)
	{
		tmp1 = tmp2->next;
		tmp2->next = *mid_node;
		*mid_node = tmp2;
		tmp2 = tmp1;
	}
	return (*mid_node);
}

/**
 * is_palindrome - checks and returns if a singly linked
 * list is a palindrome or not.
 * @head: the address of the head pointer of the list.
 *
 * Return: 1 if it is a palindrome,
 * Otherwise 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	int length;
	listint_t *mid_node_ptr, *last_node, *tmp1, *tmp2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	length = length_of_list(*head);
	mid_node_ptr = mid_node(*head, length);
	if (length > 3)
	{
		last_node = reverse_list(&mid_node_ptr);
		tmp1 = *head;
		tmp2 = last_node;
	}
	else
	{
		tmp1 = *head;
		tmp2 = mid_node_ptr;
	}

	while (tmp2 != NULL)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	if (length > 3)
	{
		reverse_list(&last_node);
	}
	return (1);
}
