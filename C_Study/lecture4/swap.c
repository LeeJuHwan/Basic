#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    printf("x pointer: %p\t", &x);
    printf("y pointer: %p\n", &y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);

    return 0;
}

void swap(int *a, int *b)
{
    printf("a variable: %i, a pointer: %p\n", *a, a);
    printf("b variable: %i, b pointer: %p\n", *b, b);
    int tmp = *a;
    printf("a pointer -> tmp pointer: %p\n", &tmp);
    *a = *b;
    printf("a pointer -> *a variable: %p\n", &a);

    *b = tmp;
    printf("a pointer -> *a variable: %p\n", &b);
}