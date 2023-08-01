#include <stdio.h>
#include <stdlib.h>

typedef struct NODE
{
    int data;
    struct NODE *next;
} NODE;

int main()
{
    NODE list[5] = {0};

    list[0].data = 100;
    list[1].data = 101;
    list[2].data = 103;
    list[3].data = 106;
    list[4].data = 110;

    list[0].next = 0;
    list[1].next = &list[2];
    list[2].next = &list[3];
    list[3].next = &list[0];
    list[4].next = &list[1];

    for (int i = 0; i <= 4; i++)
    {
        printf("list[%i]: %i\n", i, list[i].data);
    }

    NODE *pTmp = &list[4];
    while (pTmp != NULL)
    {
        int node_data = pTmp->data;
        printf("%i\n", node_data);

        pTmp = pTmp->next;
    }

    return 0;
}