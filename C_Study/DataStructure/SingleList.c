#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE
{
    char szData[64];
    struct NODE *next;
} NODE;

NODE *g_pHead = NULL;

void PrintList()
/*연결 리스트 전체 데이터 출력*/
{
    // NODE *pHead = g_pHead;
    while (g_pHead != NULL)
    {
        printf("[%p]: %s, next[%p]\n",
               g_pHead, g_pHead->szData, g_pHead->next);
        g_pHead = g_pHead->next;
    }
    // while (pHead != NULL)
    // {
    //     printf("g_Phead: %p >> Next: %p\n", g_pHead, g_pHead->next);
    //     printf("[%p]: %s, next[%p]\n",
    //            pHead, pHead->szData, pHead->next);
    //     pHead = pHead->next;
    // }

    putchar('\n');
}

int InsertNewNode(char *pszData)
{
    NODE *pNode = (NODE *)malloc(sizeof(NODE));
    memset(pNode, 0, sizeof(NODE));

    strcpy(pNode->szData, pszData);

    if (g_pHead == NULL)
    {
        g_pHead = pNode;
    }
    else
    {
        pNode->next = g_pHead;
        g_pHead = pNode;
    }
    return 1;
}
int main()
{
    // List test case
    InsertNewNode("TEST01");
    PrintList();
    InsertNewNode("TEST02");
    PrintList();
    InsertNewNode("TEST03");
    PrintList();

    return 0;
}