#include "lists.h"

/**
 * insert_node -  function that inserts number into sorted singly linked list
 *
 * Description:
 * @top: double pointer to top node
 * @number: (int) number to insert
 *
 * Return: address of newnode
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node, *prev = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	temp = *head;
	while (temp && new_node->n > temp->n)
	{
		prev = temp;
		temp = temp->next;
	}
	/* Checks for duplicate node values */
	if (temp && new_node->n == temp->n)
	{
		new_node->next = temp;
		prev->next = new_node;
	}
	/* check if new_node value is lower than value at first node */
	else if (!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}

	return (new_node);
}
