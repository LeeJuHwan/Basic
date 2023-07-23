#include <stdio.h>

int get_int(char *printString);

int main(void)
{
    int x = get_int("X: ");
}

int get_int(char *printString)
{
    int x;
    printf("%s", printString);
    scanf("%i", &x);
    printf("%p\n", &x);
    return x;
}