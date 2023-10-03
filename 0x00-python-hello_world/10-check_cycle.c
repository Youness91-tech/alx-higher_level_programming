#include "lists.h"

/**
 * check_cycle - Checks if a linked list is cycled
 * @list: The linked list to check
 *
 * Return: 1 if the list is cycled, 0 if it's not
 **/
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL)
	{
		return (0);
	}

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
