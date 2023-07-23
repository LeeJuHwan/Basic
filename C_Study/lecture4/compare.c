#include <stdio.h>
#include <cs50.h>
// #include <string.h>

// int get_int(char* string) {
//     int inputValue;
//     printf("%s\n> ", string);
//     scanf("%d", &inputValue);
//     return inputValue;
// }


int main(void)
{
    char* str = get_string("String: ");
    char* str2 = get_string("String: ");

    // if (strcmp(str, str2) == 0)
    // {
    //     printf("True\n");
    // }
    // else
    // {
    //     printf("False\n");
    // }

    printf("%p\n", str);
    printf("%p\n", str2);
}