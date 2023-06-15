#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: linked list
 * @nunber: number to be inserted
 * Return: address of the new node else NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *next_node = *head, *prev_node;

    if (head == NULL)
        return (NULL);

    new_node = malloc(sizeof(listint_t));

    if (!new_node)
        return (NULL);

    new_node->n = number;

    while (new_node->n > next_node->next->n)
        next_node = next_node->next;
    prev_node = next_node;
    next_node = next_node->next;

    prev_node->next = new_node;
    new_node->next = next_node;

    return (new_node);
}
