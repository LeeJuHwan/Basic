### 컴파일 방식
---

기계코드로 컴파일링

```c
make {filename}
```

코드 실행

```c
./{filename}
```

### 변수
---

자바 데이터 타입과 비슷한 형태를 띄지만, 문자열에서 차이를 나타낸다.

- String → char[]
    - 문자열 방식에서 동적, 정적이 적용된다.

> 요구사항
> 

프로그래밍을 처음 접하게 되면 “hello, world!” 를 출력하는 것이 관습, 여기서는 world 대신 당신의 이름을 입력 받아 출력해보세요.

- 💬  `**코드**`
    
    ```c
    #include <stdio.h>
    
    int main(void)
    {
        char name[10];
        printf("What's your name?\n");
        printf("> ");
        scanf("%s", name);
        printf("hello, %s!\n", name);
       
    }
    ```
    
    - 문자열을 scanf에 대입 할 때 그냥 사용 하지만, 그 외에 데이터 타입을 scanf로 대입 할 때는 &기호를 변수명 앞에 같이 적어야 한다.

### 조건 분기
---

자바와 매우 비슷한 코드 형태를 띄고 있었다.

> 요구사항 - 1
> 

x와 y를 입력 받아 서로의 크기를 비교 하여 어떤 값이 더 큰지 나타내주세요.

- 💬  `**코드**`
    - cs50.h 헤더 파일을 인클루드 할 수 없어 함수를 비슷하게 구현했다.
    
    ```c
    int get_int(char *string) {
        int inputValue;
        printf("%s\n> ", string);
        scanf("%d", &inputValue);
        return inputValue;
    }
    ```
    
    ```c
    #include <stdio.h>
    
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
    ```
    

> 요구사항 - 2
> 

캐릭터 타입을 입력 받아 입력한 값이 비교하는 값과 같은지 비교 하세요. 소문자, 대문자를 구분 하여주세요.

- 💬  `**코드**`
    
    캐릭터 타입 입력 받는 함수 구현
    
    ```c
    char get_char(char *questionString)
    {
        char answer;
        printf("%s\n> ", questionString);
        scanf("%c", &answer);
    
        return answer;
    }
    ```
    
    ```c
    
    #include <stdio.h>
    
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
    ```
    

### 부동소수와 숫자형일 때 소수점 버리기
---

프로그래밍에서 흔히 아는 소수점과 메모리의 관계를 따져보고 어떻게 사용 하는지 배우지만 Decimal한 자료형은 없는 것 같았다.

> 요구사항
> 

정수를 입력 받아 나눗셈을 실행 하고 값을 확인 하세요. 값의 이상함을 눈치 채셨다면 다른 데이터 타입으로 조금 더 정확한 값이 나오는지 확인하세요.

- 💬  `**코드**`
    
    함수 구현
    
    ```c
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
    ```
    
    ```c
    #include <stdio.h>
    
    int main(void)
    {
        long x = get_long("x:");
        long y = get_long("y: ");
    
        double z = (double) x / (double) y;
        printf("%.20f\n", z);
    }
    ```
    

### 반복문
---

반복문도 자바와 비슷한 문법의 형태였다.

> 요구사항 - 1
> 

고양이의 울음소리를 3번 출력하세요. 

- 💬  `**코드**`
    
    ```c
    int main(void)
    {
        // int i = 0;
        // while ( i < 3 )
        // {
        //     printf("Meow\n");
        //     i ++;
        // }
    
        for (int i = 0; i < 3; i++)
        {
            printf("Meow\n");
        }
    
    }
    ```
    

> 요구사항 - 2
> 

슈퍼 마리오의 게임에서 블록을 커널에서 나타낼 것 입니다. 3x3 그리드의 블록을 나타내세요. 다 나타내었다면 코드를 함수화 하여 반복되는 구문을 최소화 하세요.

- 💬  `**코드**`
    
    함수
    
    ```c
    int get_int(char *string) {
        int inputValue;
        printf("%s\n> ", string);
        scanf("%d", &inputValue);
        return inputValue;
    }
    
    int get_size(void)
    {
        int n;
        do
        {
            n = get_int("Size:");
        }
        while (n < 1);
        return n;
    }
    
    void print_grid(int size)
    {
        for (int i = 0; i < size; i ++)
        {
            for (int j = 0; j < size; j ++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    ```
    
    메인 코드
    
    ```c
    int main(void)
    {
        // Get size of grid
        int n = get_size();
    
        //  Print grid of bricks
        print_grid(n);
    }
    ```