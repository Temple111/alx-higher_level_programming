#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old_nd;
	listint_t *nw_nd;

	old_nd = *head;

	nw_nd = malloc(sizeof(listint_t));

	if (nw_nd == NULL)
		return (NULL);
	nw_nd->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		nw_nd->next = *head;
		*head = nw_nd;
		return (nw_nd);
	}

	while (old_nd->next != NULL)
	{
		if ((old_nd->next)->n >= number)
		{
			nw_nd->next = old_nd->next;
			old_nd->next = nw_nd;
			return (nw_nd);
		}
		old_nd = old_nd->next;
	}
	nw_nd->next = NULL;
	old_nd->next = nw_nd;
	return (nw_nd);
}

