#include "lists.h"

/**
 * check_cycle - Checks if a linked list is cycled
 * @list: The linked list to check
 *
 * Return: 1 if the list is cycled, 0 if it's not
 **/
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	if (list == NULL)
	{
		return (0);
	}

	while (turtle != NULL && rabbit != NULL && rabbit->next != NULL)
	{
		rabbit = rabbit->next->next;
		turtle = turtle->next;
		if (turtle == rabbit)
			return (1);
	}

	return (0);
}
