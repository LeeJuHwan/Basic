#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE
{
    char nodeData[64];
    struct NODE *next;
} NODE;

NODE g_head = {0};

int isEmpty()
{
    if (g_head.next == NULL)
    {
        return 1;
    }
    return 0;
}

int InsertAtHead(char *inputData)
{
    NODE *ptrNode = (NODE *)malloc(sizeof(NODE));
    memset(ptrNode, 0, sizeof(NODE));
    strcpy(ptrNode->nodeData, inputData);

    if (isEmpty())
    {
        g_head.next = ptrNode;
    }
    else
    {
        ptrNode->next = g_head.next;
        g_head.next = ptrNode;
    }
    return 1;
}

int insertAtTail(char *inputData)
{
    NODE *ptrTmp = &g_head;
    while (ptrTmp->next != 0)
    {
        ptrTmp = ptrTmp->next;
    }

    NODE *ptrNode = (NODE *)malloc(sizeof(NODE));
    memset(ptrNode, 0, sizeof(NODE));
    strcpy(ptrNode->nodeData, inputData);

    ptrTmp->next = ptrNode;
    return 0;
}

void PrintList()
/*연결 리스트 전체 데이터 출력*/
{
    NODE *pHead = g_head.next;
    while (pHead != NULL)
    {
        printf("[%p]: %s, next[%p]\n",
               pHead, pHead->nodeData, pHead->next);
        pHead = pHead->next;
    }
    putchar('\n');
}

NODE *FindData(char *pszData)
{
    NODE *pCur = g_head.next;
    NODE *pPrev = g_head.next;
    while (pCur != NULL)
    {
        if (strcmp(pCur->nodeData, pszData) == 0)
        {
            return pPrev; // 앞 전 노드 반환
        }
        pCur = pCur->next;
        pPrev = pPrev->next;
    }
    return 0;
}

// 노드 삭제
void ReleaseList(void)
{
    NODE *pTmp = g_head.next;
    printf("Realese List\n");
    while (pTmp != NULL)
    {
        NODE *pDelete = pTmp;
        pTmp = pTmp->next;

        printf("Delete : [%p] %s\n", pDelete, pDelete->nodeData);
        free(pDelete);
    }

    g_head.next = 0;
}

int DeleteData(char *pszData)
{
    NODE *pPrev = FindData(pszData);

    if (pPrev != 0)
    {
        NODE *pDelete = pPrev->next;
        pPrev->next = pDelete->next;

        printf("DeleteData(): %s\n", pDelete->nodeData);
        free(pDelete);
        return 1;
    }
    return 0;
}

int main()
{
    puts("--- INSERT AT HEAD ---");
    InsertAtHead("TEST01");
    InsertAtHead("TEST02");
    InsertAtHead("TEST03");
    PrintList();
    ReleaseList();

    puts("--- INSERT AT TAIL ---");
    insertAtTail("TEST01");
    insertAtTail("TEST02");
    insertAtTail("TEST03");
    PrintList();
    ReleaseList();

    insertAtTail("TEST01");
    insertAtTail("TEST02");
    // ReleaseList();

    puts("--- FIND DATA ---");
    printf("%p: [data] %s\n", FindData("TEST01"), FindData("TEST01")->nodeData);

    return 0;
}