#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * 
 * Description:
 * @list: pointer to head of list
 *
 * Return: 0 if list has cycle. Otherwise 1
*/

int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (!list || !list->next)
		return (0);

	tail = list;
	head = list->next;
	while (head && tail && head->next)
	{
		if (head == tail)
			return (1);
		head = head->next->next;
		tail = tail->next;
	}
	return (0);
}
