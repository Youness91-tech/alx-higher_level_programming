#include "lists.h"

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev = NULL;
	listint_t *second_half = NULL;
	int palindrome = 1;
	listint_t *temp1, *temp2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		second_half = slow_ptr->next;
	}
	else
	{
		second_half = slow_ptr;
	}

	prev->next = NULL;

	second_half = reverse_list(second_half);

	temp1 = *head;
	temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			palindrome = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	second_half = reverse_list(second_half);

	if (fast_ptr != NULL)
	{
		prev->next = slow_ptr;
		slow_ptr->next = second_half;
	}
	else
	{
		prev->next = second_half;
	}

	return (palindrome);
}
