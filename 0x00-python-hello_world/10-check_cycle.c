include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 **/
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	if (!list != NULL)
		return (0);

	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}

	return (0);
}
