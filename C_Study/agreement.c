#include <stdio.h>

char get_char(char *questionString)
{
    char answer;
    printf("%s\n> ", questionString);
    scanf("%c", &answer);


    return answer;
}


int main(void)
{
    char a = get_char("Do you agree?");
    
    if (a == 'y' || a == 'Y')
    {
        printf("Argree.\n");
    }
    else if (a == 'n' || a == 'N')
    {
        printf("Not Argee\n");
    }

}