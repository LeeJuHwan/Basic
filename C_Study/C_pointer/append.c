#include <stdio.h>
#include <stdlib.h>

int *appendValue(int *arrays, int value)
{
    int *tmp = (int *)malloc(sizeof(arrays) + (1 * sizeof(int)));
    printf("last tmp: %lu\n", sizeof(*tmp));
    for (int i = 0; i < sizeof(*tmp); i++)
    {
        printf("index: %d\n", i);
        tmp[i] = arrays[i];
    }
    int last_idx = sizeof(*tmp);
    tmp[last_idx] = value;
    arrays = tmp;
    return arrays;
}

int main(void)
{
    int *array;
    array = (int *)malloc(4 * sizeof(int));
    for (int i = 0; i < sizeof(array); i++)
    {
        array[i] = i + 1;
    }
    printf("size of array: %lu\n", sizeof(*array));
    // int *tmp = (int *)malloc(8 * sizeof(int));
    // for (int i = 0; i < 4; i++)
    // {
    //     tmp[i] = array[i];
    // }
    // array = tmp;

    array = appendValue(array, 10);
    printf("array size: %lu\n", sizeof(*array));
    for (int i = 0; i <= sizeof(*array); i++)
    {
        printf("%i\n", *(array + i));
    }

    // printf("%d\n", *(array + sizeof(array)));
}
