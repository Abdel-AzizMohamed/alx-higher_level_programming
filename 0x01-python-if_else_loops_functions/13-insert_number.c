#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: linked list
 * @nunber: number to be inserted
 * Return: address of the new node else NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *next_node = *head, *prev_node = NULL;

    if (head == NULL)
        return (NULL);

    new_node = malloc(sizeof(listint_t));

    if (!new_node)
        return (NULL);

    new_node->n = number;

    while (next_node)
    {
        if (next_node->n > new_node->n)
            break;
        prev_node = next_node;
        next_node = next_node->next;
    }

    if (!prev_node)
    {
        *head = new_node;
        new_node->next = next_node;
    }
    else
    {
        prev_node->next = new_node;
        new_node->next = next_node;
    }

    return (new_node);
}
