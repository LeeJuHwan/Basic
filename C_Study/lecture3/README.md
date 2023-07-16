### Big O

---

가장 느린 것 부터 가장 빠른 순서대로의 빅오 표기법 나열

- $O(n^2)$
- $O(n log n)$
- $O(n)$
- $O(log n)$
- $O(1)$

### Linear Search

---

가장 최악의 경우 $O(n^2)$ 의 형태가 될 수 있지만 운 좋게 가장 최상의 상황인 경우엔 $O(1)$ 형태가 될 수 있다.

### Binary Search

---

가장 최악의 경우 $O(n log n)$의 형태가 될 수 있고, 가장 최상의 경우는 $O(1)$ 형태가 될 수 있다.

이렇게, 알고리즘의 기법을 선택 하여 최상의 경우, 최악의 경우를 고려하여 더 나은 방법을 선택 할 수 있다.

- 💬 코드
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    int main(void)
    {
        string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "top hat"};
        string s = get_string("String: ");
        // int numbers[] = {20, 500, 10, 5, 100, 1, 50};
        // int n = get_int("Number: ");
    
        // linear search
        for (int i = 0; i < 6; i++)
        {
            // if (numbers[i] == n)
            if (strcmp(strings[i], s) == 0)
            {
                printf("Found\n");
                return 0;
            }
        }
            printf("Not Found\n");
            return 1;
    }
    ```
    

### Struct

---

데이터 캡슐화를 시켜 관리하기 위한 클래스 같은 개념으로 사용

- 💬 코드
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>
    
    typedef struct
    {
        string name;
        string number;
    }
    person;
    
    int main(void)
    {
        person people[2];
    
        people[0].name = "Carter";
        people[0].number = "+1-617-495-1000";
    
        people[1].name = "David";
        people[1].number = "+1-949-468-2750";
    
        string name = get_string("Name: ");
    
        for (int i = 0; i <2; i++)
        {
            if (strcmp(people[i].name, name) == 0)
            {
                printf("Found %s\n", people[i].number);
                return 0;
            }
        }
        printf("Not Found\n");
        return 1;
    }
    ```
    

## Sorting

---

### Selection Sort

숫자의 배열을 반복하며 첫번째 수가 다음 수보다 작은지를 판단 하여 작은 수를 첫번째 위치 하게 만드는 정렬 방법이다.

그 중 가장 작은 수가 되는 숫자를 변수에 저장하고, 마지막 반복문까지 돌고 난 수를 앞으로 정렬 시키게된다.

- pseudocode
    
    ```c
    for i from 0 to n - 1
    	Find smallest number between number[i] and numbers[n-1]
    	Swap smallest number with numbers[i]
    
    ```
    

선택 정렬은 정렬 하려는 숫자가 n개 있을 경우 가장 작은 요소를 찾는데 n - 1비교가 필요하다.

결국, 0이 가장 작은 숫자를 알기 위해선 반복문의 마지막 까지 가야만 알 수 있기 때문이다.

상한 빅오 표기법: $O(n^2)$

하향 빅오 표기법: $O(n^2)$

### Bubble Sort

첫번째 기준이 되는 수를 다음 수를 비교하여 기준의 수가 더 크다면 서로의 위치를 바꾼다. 이 과정을 배열의 마지막 까지 반복 하게 되면 최대 n-1번 수행 하게 된다.

- pseudocode
    
    ```c
    Repeat n times
    	for i from 0 to n-2. // 배열의 마지막 요소가 배열의 길이를 넘어서 비교하지 않기 위해 n-2
    		if numbers[i] and numbers[i+1] out of order
    			Swap them
    	if no swaps
    		quit
    ```
    

상한 빅오 표기법: $O(n^2)$

하향 빅오 표기법: $O(n)$ → 이미 모든 목록이 정렬되어 있는 경우 발생

그래도 아직 이 정렬 방식은 많이 느리다. 이 것을 더 발전 시킬 수 있는 방법이 없을까?

### Merge Sort

숫자외 오른쪽 절반을 정렬하고, 왼쪽 절반을 정렬 하고 정렬 된 숫자를 비교하며 병합하는 정렬 방식이다.

병합 정렬은 다시 뒤로 돌아갈 필요가 없고, 기준이 되는 숫자와 다음 숫자간의 비교만 이루어지기 때문에 앞으로만 나아간다. 그렇기 때문에 많은 반복이 일어나지 않는 정렬 방법이다.

하지만, 왼쪽과 오른쪽 정렬을 병합하는 메모리가 더 필요하기 때문에 다른 정렬 방식 보다 메모리 사용량이 많다.

- pseudocode
    
    ```c
    If only one number
    	Quit
    Else
    	Sort left half of numbers
    	Sort right half of numbers
    	Merge sorted havles
    ```
    

![image](https://github.com/LeeJuHwan/LeeJuHwan/assets/118493627/cf709e97-d175-4be4-84c5-0ca7a652d34b)

- 왼쪽과 오른쪽의 절반을 분리하여 순차적으로 왼쪽 부터 정렬한다.
    - 왼쪽의 절반 중 또 왼쪽의 절반을 분리 하여 정렬한다.
    - 왼쪽의 절반이 크기가 1이라면 그대로 끝을 내고, 오른쪽 절반도 크기가 1로 끝이 나면 병합한다.
    - 왼쪽의 오른쪽 절반을 위와 같은 방법으로 정렬 및 병합
- 그렇게 왼쪽과 오른쪽 절반의 정렬이 마무리 되었으면 왼쪽의 0번째, 오른쪽의 0번째 요소의 크기를 비교하고 크기가 작은 것은 새로운 메모리에 할당한다. 그 다음 할당된 숫자는 사라지게 되고, 그 다음 숫자와 비교하게 된다. 이 것을 재귀적으로 호출 하는 방식이다.

상향 빅오 표기법 : $O(n log n)$

하향 빅오 표기법 : $O(n log n)$

시간 복잡도는 감소하고 공간 복잡도는 증가하는 형태이다. 하지만, 선형검색과 같이 운 좋은 케이스로 인해 $O(n)$ 보다 느릴 것이다.

> recursion
> 

재귀 함수를 이용 하여 피라미드를 쌓는 등, 다양한 방법을 사용 할 수 있다. 하지만 재귀를 종료 시점을 명시 하지 않으면 코드를 컴파일 할 수 없다.

- 💬 코드
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    void draw(int n);
    
    int main(void)
    {
        draw(1);
    }
    
    void draw(int n)
    {
        if (n == 5)
        {
            return;
        }
    
        for (int i = 0; i < n; i++)
        {
            printf("#");
        }
        printf("\n");
    
        draw(n + 1);
    }
    ```
    
    > 재귀 함수의 사용
    > 
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    void draw(int n);
    
    int main(void)
    {
        int height = get_int("Height: ");
        draw(height);
    }
    
    void draw(int n)
    {
        if (n <= 0)
        {
            return;
        }
        draw(n - 1);
    
        for (int i = 0; i < n; i ++)
        {
            printf("#");
        }
        printf("\n");
    }
    ```
    
    - draw(n - 1)의 역할과 n이 0보다 작을 때는 return 하는 구문의 영향으로 인해 이 코드는 1 2 3 4 순차적으로 해쉬 기호를 그리게 된다.
    - 디버깅을 해보면 return을 만난 이후 기존에 호출 되었던 호출 스택 메모리에 할당 되어 있는 것들이 순차적으로 다시 실행 된다.
    ![image](https://github.com/LeeJuHwan/LeeJuHwan/assets/118493627/509f9f48-816b-48fc-85c4-2f95b10d8ebc)
        