#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // if (s[i] >= 'a' && s[i] <= 'z')
        if (islower(s[i]))
        {
            // printf("%c", s[i]-32);
            printf("%c", toupper(s[i]));
        }
        // else if (s[i] >= 'A' && s[i] <= 'Z')
        else if (isupper(s[i]))
        {
            // printf("%c", s[i]+32);
            printf("%c", tolower(s[i]));
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}