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

	for (len = 0; node; len++)
		node = node->next;

	numbers_list = malloc(sizeof(int) * len);

	node = *head;

	for (i = 0; node; i++)
	{
		numbers_list[len] = node->n;
		node = node->next;
	}

	for (i = 0, j = len; i < len / 2; i++, j--)
	{
		if (numbers_list[i] != numbers_list[j - 1])
			return (0);
	}

	return (1);
}
