#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define BUFFER_SIZE 80
int strip(char str[], int limit);

int main(void)
{
    char line[BUFFER_SIZE];

    while (1)
    {
        printf("$ ");
        int length = strip(line, BUFFER_SIZE);
        printf("%s: %d\n", line, length);
    }
}

int strip(char str[], int limit)
{
    int ch, i = 0;

    while ((ch = getchar()) != '\n')
    {
        if (i < limit - 1 && (!isspace(ch) || i > 0 && !isspace(str[i - 1])))
        {
            str[i++] = ch;
        }
    }
    if (i > 0 && isspace(str[i - 1]))
    {
        i--;
    }
    str[i] = '\0';
    return i;
}
