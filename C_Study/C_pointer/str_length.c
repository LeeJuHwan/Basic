#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define BUFFER_SIZE 20

// char *get_string();
// int get_length(char *string);
int get_length(char *str, int limit);

int main(void)
{
    char buffer[BUFFER_SIZE];
    while (1)
    {
        // char *str = get_string();
        printf("$ ");
        int length = get_length(buffer, BUFFER_SIZE);
        // if (strcmp(str, "q") == 0)
        // {
        //     printf("프로그램이 종료 됩니다.\n");
        //     break;
        // }
        // printf("%s: %d\n", str, get_length(str));
        printf("%s: %d\n", buffer, length);
    }
}

// char *get_string()
// {
//     char *string = (char *)malloc(100 * sizeof(char));
//     printf("$ ");
//     scanf("%[^\n]%*c", string);
//     return string;
// }
// int get_length(char *string)
// {
//     return strlen(string);
// }

int get_length(char str[], int limit)
{
    int ch, i = 0;

    while ((ch = getchar()) != '\n')
    {
        if (i < limit)
        {
            str[i++] = ch;
        }
    }
    str[i] = '\0';
    return i;
}
