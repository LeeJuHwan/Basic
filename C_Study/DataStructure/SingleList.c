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
    NODE *pHead = g_pHead;
    while (pHead != NULL)
    {
        printf("g_Phead: %p >> Next: %p\n", g_pHead, g_pHead->next);
        printf("[%p]: %s, next[%p]\n",
               pHead, pHead->szData, pHead->next);
        pHead = pHead->next;
    }
    putchar('\n');
}

// 노드 추가
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

// 노드 삭제
void ReleaseList(void)
{
    NODE *pTmp = g_pHead;
    while (pTmp != NULL)
    {
        NODE *pDelete = pTmp;
        pTmp = pTmp->next;

        printf("Delete : [%p] %s\n", pDelete, pDelete->szData);
        free(pDelete);
    }
}

int FindData(char *pszData)
{
    NODE *pTmp = g_pHead;
    while (pTmp != NULL)
    {
        if (strcmp(pTmp->szData, pszData) == 0)
        {
            return 1;
        }
        pTmp = pTmp->next;
    }
    return 0;
}

int DeleteData(char *pszData)
{
    NODE *pTmp = g_pHead;
    NODE *pPrev = NULL;

    while (pTmp != NULL)
    {
        if (strcmp(pTmp->szData, pszData) == 0)
        {
            printf("DeleteData(): %s\n", pTmp->szData);
            if (pPrev != NULL)
            {
                pPrev->next = pTmp->next;
            }
            else
            {
                // 삭제 할 데이터가 첫 번째 인 경우
                g_pHead = pTmp->next;
            }
            free(pTmp);
            return 1;
        }
        pPrev = pTmp;
        pTmp = pTmp->next;
    }
    return 0;
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

    if (FindData("TEST01") == 1)
    {
        printf("FindDat(): TEST01 found\n");
    }

    if (FindData("TEST02") == 1)
    {
        printf("FindDat(): TEST02 found\n");
    }

    if (FindData("TEST03") == 1)
    {
        printf("FindDat(): TEST03 found\n");
    }

    DeleteData("TEST01");
    DeleteData("TEST02");
    DeleteData("TEST03");

    ReleaseList();
    return 0;
}