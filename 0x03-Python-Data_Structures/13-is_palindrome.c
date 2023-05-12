#include "lists.h"

listint_t *list_reverse(listint_t **head_ptr);
int is_palindrome(listint_t **head);

/**
 * list_reverse - Reverses a singly-linked listint_t list.
 * @head_ptr: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *list_reverse(listint_t **head_ptr)
{
	listint_t *nd = *head_ptr, *link, *prev_nd = NULL;

	while (nd)
	{
		link = nd->next;
		nd->next = prev_nd;
		prev_nd = nd;
		nd = link;
	}

	*head_ptr = prev_nd;
	return (*head_ptr);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cmp, *re, *md;
	size_t sz = 0, a;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	cmp = *head;
	while (cmp)
	{
		sz++;
		cmp = cmp->next;
	}

	cmp = *head;
	for (a = 0; a < (sz / 2) - 1; a++)
		cmp = cmp->next;

	if ((sz % 2) == 0 && cmp->n != cmp->next->n)
		return (0);

	cmp = cmp->next->next;
	re = list_reverse(&cmp);
	md = re;

	cmp = *head;
	while (re)
	{
		if (cmp->n != re->n)
			return (0);
		cmp = cmp->next;
		re = re->next;
	}
	list_reverse(&md);

	return (1);
}

