#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


char* get_string(char* inputString);


int main(void)
{
    char* s = get_string("'S' 에 들어갈 내용을 입력 하세요");
    if (s == NULL)
    {
        return 1;
    }

    char* t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // for (int i = 0, n = strlen(s); i <= n; i ++)
    // {
    //     t[i] = s[i];
    // }

    strcpy(t, s);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
            printf("s > %s\n", s);
            printf("t > %s\n", t);
            printf("t pointer > %p\n", t);
            printf("s pointer > %p\n", s);
    }
    else
    {
        printf("올바른 내용을 입력해주세요\n");
    }

    free(s);
    free(t);
    return 0;
}


char* get_string(char* inputString)
{
    char* scanValue = (char*)malloc(100);
    printf("%s\n", inputString);
    printf("> ");
    scanf("%[^\n]", scanValue);
    return scanValue;
}