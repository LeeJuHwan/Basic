#include <stdio.h>

int get_int(char *string) {
    int inputValue;
    printf("%s\n> ", string);
    scanf("%d", &inputValue);
    return inputValue;
}

int main(void) 
{
    int x = get_int("What's x?");
    int y = get_int("What's y?");

    if ( x < y ) {
        printf("x가 y보다 작습니다.\n");
        printf("x: %d y: %d\n", x, y);
    }
    else if ( x > y )
    {
        printf("x가 y보다 큽니다.\n");
        printf("x: %d y: %d\n", x, y);
    }
    else if ( x == y )
    {
        printf("x와 y는 같습니다.\n");
        printf("x: %d y: %d\n", x, y);
    }
}