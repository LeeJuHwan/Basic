#include <stdio.h>


int get_int(char *string) {
    int inputValue;
    printf("%s\n> ", string);
    scanf("%d", &inputValue);
    return inputValue;
}

long get_long(char *string) {
    long inputValue;
    printf("%s\n> ", string);
    scanf("%li", &inputValue);
    return inputValue;
}

int main(void)
{
    long x = get_long("x:");
    long y = get_long("y: ");

    double z = (double) x / (double) y;
    printf("%.20f\n", z);
}