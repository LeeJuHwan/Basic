#include <stdio.h>

// typedef char *string;

int main(void)
{
    // int num = 50;
    // int *p = &num;
    // printf("%i\n", *p);

    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", s[2]);
}
