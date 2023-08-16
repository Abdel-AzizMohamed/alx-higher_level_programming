#include "lists.h"

/**
 * is_palindrome - checks if a given list is palindrome
 * @head: given linked list
 * Return: 1 if palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	int *numbers_list, len, i, j;
	listint_t *node = *head;

	if (!head || *head == NULL)
		return (1);

	for (len = 0; node; len++)
		node = node->next;

	if (len == 1)
		return (1);

	numbers_list = malloc(sizeof(int) * len);

	if (!numbers_list)
		return (-1);

	node = *head;

	for (i = 0; i < len; i++)
	{
		numbers_list[i] = node->n;
		node = node->next;
	}

	for (i = 0, j = len; i < len / 2; i++, j--)
	{
		if (numbers_list[i] != numbers_list[j - 1])
			return (0);
	}

	free(numbers_list);
	return (1);
}
