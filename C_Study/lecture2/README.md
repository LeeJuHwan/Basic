### GCC 컴파일러

---

> 어셈블러 파일로 컴파일
> 

```jsx
$ clang -o hello hello.c -lcs50
```

- -o: 커맨드 라인 인자 값으로 a.out과 같은 어셈블러 고유 파일명이 아닌, 지정 파일 명으로 선언이 가능하다.

> 실행
> 
- -l: 헤더 파일을 기계코드로 변경
- cs50: 헤더파일 명
    
    → make는 구문 내 모든 컴파일을 자동화 하지만, clang은 수동으로 실행 할 수 있어 제어권이 있다.
    

```jsx
./{callable file name}
```

1주차에서 배운 make 외에도 많은 컴파일러가 있지만, clang을 사용 하여 수동적으로 컴파일 하는 방식을 적용 하였다.

### 컴파일 단계

---

> Preprocessing
> 
- #표시가 되어 있는 파일은 전처리 되어 분석된다.
- /usr/include 의 형태를 띄고 있는 폴더에 헤더 파일을 찾게 된다.
- 위 과정을 함수 프로토타입이라고 한다.
    
    ```jsx
    #include <stdio.h> -> string get_string(string prompt);
    #include <cs50.h> -> int printf(string format, ...);
    
    int main(void)
    {
        string name = get_string("What's your name? ");
        printf("hello, %s\n", name);
    }
    ```
    

> Compiling
> 
- 모든 해쉬 표시가 된 기능을 전처리 하고 난 뒤, clang 또는 어떠한 컴파일러로 코드를 어셈블리 코드로 변환한다.
<img width="664" alt="image" src="https://github.com/LeeJuHwan/Basic/assets/118493627/410078f4-9723-44c0-b634-e862280ce494">

> assembling
> 
- 0과 1로 이루어진 기계 코드로 변경한다.

> linking
> 
- 작성한 코드를 linking을 통해 printf.c 등 다양한 라이브러리에서 사용 되는 메서드를 0과 1로 변경 하여 하나의 파일로 합친다.

<aside>
💡 이런 과정을 거치는 것을 **컴파일링**이라고 한다.
</aside>


### 헤더파일 직접 구현해보기
---

위에서 컴파일링 과정을 듣고 나니, 헤더 파일을 갖다 쓰는 것도 좋지만 한 번 어떻게 만드는지 궁금해서 검색 해 보고 만들어보았다.

- 나만의 헤더파일 요구사항
    1. 나는 printf는 부자연 스러우니 파이썬 처럼 print를 사용 할거야.
        - 💬  `**코드**`
            
            print.h
            
            ```c
            #ifndef HEADER_H
            # define HEADER_H
            #include <stdio.h>
            
            void print(char *string)
            {
                printf("%s", string);
            }
            
            #endif
            ```
            
            hello.c
            
            ```c
            #include <stdio.h>
            #include "print.h"
            
            int main(void)
            {
                print("hello, world!");
            }
            ```
            
            컴파일
            
            ```jsx
            clang -o hello hello.c
            ./hello
            ```
            

### debugging

---

코드를 작성 하는 사람은 누구나 다 실수 하지만 그 것을 위해 사용 할 수 있는 도구가 있디.

이 실수들은 물리적 버그가 아닌 논리적 버그이다.

> 해쉬 기호를 3개 출력 하는 구문을 작성 해보자.
> 

→ 의도치 않게 해쉬 기호는 3개가 아닌 4개가 출력 되었다. 이 것은 논리연산자를 의도 하여 작성 했다.

1. 초기에는 printf를 사용 하여 출력 할 것이다.
    
    ```jsx
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i <= 3; i ++)
        {
            printf("i is %i\n", i);
            printf("#\n");
        }
    }
    ```
    
- 출력되는 화면을 보고 0 ~ 3 까지는 4개의 숫자를 나타내는 것을 확인하고 수정 할 것이다.

→ 이 것은 프로그램이 성장함에 따라 프린트를 출력하는 구문이 많고 끝나면 다 지워줘야 하는 단점이 있다.

2. 비주얼 스튜디오 코드에 내장 되어 있는 브레이크 포인트를 활용한 디버거를 호출한다.
    
    ```c
    debug50 ./{filename}
    ```
    

3. 러버덕 에게 문제를 설명하기
    - 영상에서는 고무 오리 인형에게 내 문제를 얘기하면 어느 순간 문제가 잘못 되었다는 것을 느낄 수 있다고 설명한다.
    - 위 말을 뒷받침 하는 내용은 사실, 문제를 해결 할 때 화면만 응시하지 말고 누군가에게 조언을 얻거나 누군가에게 문제를 설명 하며, 머리를 식히는 시간도 필요하다는 얘기였다.