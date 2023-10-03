#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *crnt_nd = *head;
	listint_t *new_nd;

	new_nd = malloc(sizeof(listint_t));
	if (new_nd == NULL)
	{
		return (NULL);
	}
	new_nd->n = number;

	if (crnt_nd == NULL || crnt_nd->n >= number)
	{
		new_nd->next = crnt_nd;
		*head = new_nd;
		return (new_nd);
	}

	while (crnt_nd != NULL && crnt_nd->next != NULL
			&& crnt_nd->next->n < number)
		crnt_nd =crnt_nd->next;

	new_nd->next = crnt_nd->next;
	crnt_nd->next = new_nd;

	return (new_nd);
}
