#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr_pos, *view;

	if (list == NULL || list->next == NULL)
		return (0);
	curr_pos = list;
	view = curr_pos->next;

	while (curr_pos != NULL && view->next != NULL
		&& view->next->next != NULL)
	{
		if (curr_pos == view)
			return (1);
		curr_pos = curr_pos->next;
		view = view->next->next;
	}
	return (0);
}

