#include <stdio.h>
#include <cs50.h>

const int N = 3;

float average(int length, int array[]);


int main(void)
{
    int scores[N];
    // scores[0] = get_int("Score: ");
    // scores[1] = get_int("Score: ");
    // scores[2] = get_int("Score: ");

    for (int i = 0; i < 3; i ++)
    {
        scores[i] = get_int("Score: ");
    }
    // printf("평균: %f\n", (scores[0] + scores[1] + scores[2]) / (float) 3);
    printf("평균: %f\n", average(N, scores));
}


float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i ++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}


