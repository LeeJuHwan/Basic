#include <cs50.h>
#include <stdio.h>



int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    string s = "HI!";
    printf("CHAR ARRAY: %c%c%c\n", c1,c2,c3);
    printf("STRING S: %s\n", s);

    printf("CHAR S: %c%c%c\n", s[0],s[1],s[2]);

    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    for (int i = 0; i < 2; i ++)
    {
        for (int j = 0; j < 4; j ++)
        {
            printf("%c", words[i][j]);
        }
        printf("\n");
    }


}