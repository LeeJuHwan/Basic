#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *strdup_implement(char *string);

// I/O used kernel
// int main(void)
// {
//     int BUFFER_SIZE = 100;
//     int n = 0;
//     char *words[100];
//     char buffer[BUFFER_SIZE];

//     while (n < 4 && scanf("%s", buffer) != EOF)
//     {
//         // words[n] = strdup(buffer); // 문자열을 deep copy하여 return -> strcpy는 2개의 매개 변수가 동일한 메모리 크기를 사용하고 있어야 해서 에러남
//         words[n] = strdup_implement(buffer);
//         n++;
//     }

//     for (int i = 0; i < 4; i++)
//     {
//         printf("%s\n", words[i]);
//     }
// }

// File I/O
int main(void)
{
    FILE *fp = fopen("words.txt", "r");
    FILE *write_fp = fopen("output.txt", "w");
    char buffer[100];

    while (fscanf(fp, "%s", buffer) != EOF)
    {
        // printf("%s\n", buffer);
        fprintf(write_fp, "%s\n", buffer);
    }
    fclose(fp);
    fclose(write_fp);
}

// strdup 구현 해보기
char *strdup_implement(char *string)
{
    char *ptr = (char *)malloc(strlen(string) + 1);
    if (ptr != NULL)
    {
        strcpy(ptr, string);
    }
    return ptr;
}
