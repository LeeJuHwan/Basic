### 메모리의 저장 된 주소 값 확인

---

```c
#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);

}
-> 0x7ffd1921a72c
```

### 포인터

---

`*p = &n;` 과 같은 명령어를 C에서 입력 하면 메모리에 저장 되어있는 주소 값을 얻을 수 있었다.

이 과정은 `*p` 라는 포인터를 획득하고, `&{변수}` 로 메모리 주소를 가져오는 형태가 된다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4ba0ce0e-c0c6-471a-ba2d-a959deb41aa7/Untitled.png)

- 포인터는 포인터를 가르킬 수 있다. 그 것은 \*\*로 표기하며 이중 포인터라고 표현한다.

`string s = “Hi!”;` 이러한 문자열을 입력 하면, C는 char타입의 캐릭터 문자를 1개씩 배열로 받아들인다. 값은 `H`, `i`, `!`, `\0` 으로 모두 각자 메모리 주소 값을 가지고 있지만 실제 문자열에 저장 된 `‘s’` 는 문자들의 배열에 첫번째 메모리 주소 값을 갖게된다.

이러한 문자열에 대한 메모리 저장 방식은 왜, 3가지의 변수가 쓰이지 않았고 왜, 첫번째 문자의 주소 값만 갖고 있을까?

- 문자열은 항상 null로 종료 하기 때문에 첫번째 메모리 주소를 얻고, null 데이터(`\0`)가 나올 때 까지 출력하면 된다.

하지만! 지금 까지 C에서는 string이라는 것은 존재 하지 않았다. 문자배열의 포인터를 사용 했기 때문에 문자열 처럼 보여진 것이다.

그래서, 이 코드는 서로 같다.

```python
// string s = "HI!";
    char *s = "Hi!";
    printf("%s\n", s);
```

→ 여기서 string을 구현 하고 싶다면?

```c
typedef char *string;
```

구조체를 이용 하여 string 타입은 문자 배열들의 포인터 라고 명시 해주면 결국 string 타입을 만들어 낼 수 있었다.

→ 문자열에 대한 메모리 주소 값 확인하기

```c
int main(void)
{
		char *s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);

}
0x563ebf838004
0x563ebf838004
```

> 포인터 역참조

이렇게 포인터는 해당 변수에 있는 메모리 주소 값을 가지고 있다. 하지만, 이 주소 값이 의미하는 것은 그 안에 담겨져 있는 정수, 문자열이 필요할 뿐 메모리 주소를 활용 하기는 아직 어렵다. 이럴 때 쓰일 수 있는게 역참조 방식

```c
int main(void)
{
    int num = 50;
    int *p = &num;
    printf("%i\n", *p);

}
-> memory/ $ make addresses
memory/ $ ./addresses
50
```

이렇게, 포인터를 지정하고 메모리 주소 값을 얻은 다음 역참조 하게 되면 아래와 같이 변수를 호출 할 수 있다.

> 포인터 연산

문자배열의 포인터는 위에서 봤듯이 캐릭터의 첫번째 문자 주소를 갖고 있는 포인터다. 하지만, 두번째 ~ 세번째 등 등 그 이후에 있는 주소값을 역참조 하려면 어떻게 해야 할까?

일단, 머릿속에 있는 일방적인 인덱스 방법으로는 역참조가 불가능 했고 포인터 연산을 이용 하면 그 이후에 값도 가지고 올 수 있었다.

```c
int main(void)
{
		char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", s[2]);

}
memory/ $ ./addresses
H
I
!
```

> 포인터 얕은 복사

하나의 포인터를 가르키고 있는 문자열 포인터의 값을 다른 변수에 집어 넣어보자.

그 후 포인터 값을 담고 있는 변수를 Capitalizing 하는 대문자 값으로 변경 했다. 그 다음 출력을 해보면 둘이 같은 값을 나타내고 있다. 이 것은 메모리 값을 복사 하게 되어 같은 공간을 서로 같이 바라보는 현상이다.

코드로 보자면 이렇게 볼 수 있다

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char* get_string(char* inputString);

int main(void)
{
    char* s = get_string("'S' 에 들어갈 내용을 입력 하세요");

    char* t = s;

    if (strlen(s) > 0)
    {
        t[0] = toupper(t[0]);
    }
    else
    {
        printf("대문자로 변경 할 값이 없습니다.");
    }

    printf("%s\n", s);
    printf("t pointer > %p\n", t);
    printf("s pointer > %p\n", s);
}

char* get_string(char* inputString)
{
    char* scanValue = (char*)malloc(100);
    printf("%s\n", inputString);
    printf("> ");
    scanf("%s", scanValue);
    return scanValue;
}

'S' 에 들어갈 내용을 입력 하세요
> hello
Hello  // s가 아닌 t를 출력
t pointer > 0x558d2870a2a0
s pointer > 0x558d2870a2a0
```

> 새로 사용 하는 함수 정리

- Malloc
  - 메모리 할당을 위한 함수
  - 원하는 만큼 할당할 메모리를 미리 요청 할 수 있으며 메모리의 첫번째 바이트 주소를 반환한다.
  - 하지만, 사용자가 입력 한 메모리를 기억하고 사용해야한다.
- free
  - Malloc 같은 함수에서 정의되어 사용 되는 메모리를 해제하고, 나중에 다시 사용 할 수 있도록 메모리를 관리한다.
  - 이러한 free문 없이 구현 된 코드는 나중에 메모리 부족 현상을 겪을 수 있다.

위 내용을 읽고 코드를 수정 하여 메모리 관리를 돕고, 안정화 된 코드를 작성해보자

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char* get_string(char* inputString);

int main(void)
{
    char* s = get_string("'S' 에 들어갈 내용을 입력 하세요");
    if (s == NULL)
    {
        return 1;
    }

    char* t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    strcpy(t, s);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
            printf("s > %s\n", s);
            printf("t > %s\n", t);
            printf("t pointer > %p\n", t);
            printf("s pointer > %p\n", s);
    }
    else
    {
        printf("올바른 내용을 입력해주세요\n");
    }

    free(s);
    free(t);
    return 0;
}

char* get_string(char* inputString)
{
    char* scanValue = (char*)malloc(100);
    printf("%s\n", inputString);
    printf("> ");
    scanf("%[^\n]", scanValue);
    return scanValue;
}
```

이렇게 우린 명시적으로 메모리를 관리 할 수 있었지만, 누군가에 의해 작성된 코드들은 메모리 관리가 어떻게 되어있는지 모르며 실제 이렇게 막 작성해도 돌아간다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    int* x = malloc(3 * sizeof(int));
    x[1] = 72;
    x[2] = 73;
    x[3] = 33;

}
```

이 코드의 문제점은 사람의 눈엔 보이지만 컴퓨터는 그저 실행 할 뿐이었다. 왜냐 구문적 오류가 없기 때문에 그가 의도한 듯 실행된다. 그래서 이러한 오류를 파헤치기 위해 소프트웨어의 힘을 빌릴 수 있다.

> Valgrind

위에서 실행 한 멍청한 코드를 트래킹 해 본 결과 아래와 같은 결과가 나온다.

```
memory/ $ valgrind ./memory
==13778== Memcheck, a memory error detector
==13778== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==13778== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==13778== Command: ./memory
==13778==
==13778== Invalid write of size 4
==13778==    at 0x109170: main (memory.c:10)
==13778==  Address 0x4bb404c is 0 bytes after a block of size 12 alloc'd
==13778==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==13778==    by 0x109151: main (memory.c:7)
==13778==
==13778==
==13778== HEAP SUMMARY:
==13778==     in use at exit: 12 bytes in 1 blocks
==13778==   total heap usage: 1 allocs, 0 frees, 12 bytes allocated
==13778==
==13778== 12 bytes in 1 blocks are definitely lost in loss record 1 of 1
==13778==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==13778==    by 0x109151: main (memory.c:7)
==13778==
==13778== LEAK SUMMARY:
==13778==    definitely lost: 12 bytes in 1 blocks
==13778==    indirectly lost: 0 bytes in 0 blocks
==13778==      possibly lost: 0 bytes in 0 blocks
==13778==    still reachable: 0 bytes in 0 blocks
==13778==         suppressed: 0 bytes in 0 blocks
==13778==
==13778== For lists of detected and suppressed errors, rerun with: -s
==13778== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

- 🟦 라인: 4바이트 크기의 배열이 0바이트가 생략되고 작성 되었다 라는 첫번째 키 포인트
  - 해결 방법 → 인덱스 번호를 0번 부터 지정 하여 배열을 관리하면 됨
- 🟥 라인: 메모리 누수 현상에 대해 안내하고 있다.
  - 해결 방법 → free 함수를 통해 메모리 관리 하면 됨

해결 후 트래킹

```
==2001== Memcheck, a memory error detector
==2001== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==2001== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==2001== Command: ./memory
==2001==
==2001==
==2001== HEAP SUMMARY:
==2001==     in use at exit: 0 bytes in 0 blocks
==2001==   total heap usage: 1 allocs, 1 frees, 12 bytes allocated
==2001==
==2001== All heap blocks were freed -- no leaks are possible
==2001==
==2001== For lists of detected and suppressed errors, rerun with: -s
==2001== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0
```

### Garvage Values

---

처음 할당 한 배열에 값을 초기화 하지 않고 출력을 요구하면 이 값은 0으로 C 자체적으로 초기화 해 주지만 그걸 반복하진 않는다. 그럼 0이 출력 되다 어떠한 난수가 출력이 되고, 그 것은 양수일수도 음수일수도 있다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int scores[1024];

    for (int i = 0; i < 1024; i++)
    {
        printf("%i\n", scores[i]);
    }
}
```

- Console
  ```
  0
  0
  0
  0
  0
  0
  0
  -841321604
  32745
  -841127184
  32745
  -841366128
  32745
  -2051164689
  0
  -841366168
  32745
  -844876912
  32745
  -841320471
  32745
  30
  0
  -841365168
  32745
  -841127184
  32745
  -734445720
  32767
  -734445724
  32767
  -734446672
  32767
  -841365168
  32745
  -2051164689
  0
  -734445724
  32767
  35059415
  0
  -841369128
  32745
  0
  0
  0
  0
  -844747366
  32745
  -844850168
  32745
  -734445520
  32767
  -734445536
  32767
  1242940676
  0
  1
  32745
  6
  0
  -844869568
  32745
  0
  3
  46
  0
  0
  0
  46
  0
  -2051164689
  0
  -734445376
  32767
  -844747366
  32745
  -841369760
  32745
  -734445536
  32767
  -734445520
  32767
  -841317871
  32745
  5
  0
  -844876912
  32745
  1
  0
  0
  0
  ```

### Scope 문제를 해결 할 수 있는 포인터

---

지역 변수에서 사용 되는 값은 반환을 하지 않는다면 바꾸기 어렵다. 하지만, C에서 강력한 포인터 기능을 이용해서 메모리 주소값에 1차적으로 접근 하고, 메모리 주소로 향해 내부에 있는 값을 임시 변수에 넣는다.

그 다음, a 메모리 주소에 향해 있는 값에 b 메모리 주소에 향해 있는 값을 대입하고, b 메모리 주소에 향해 있는 값을 임시 변수에 있는 값을 가지고 나오면 서로 다른 Scope에서 포인터 하나로 같은 알고리즘을 수행 했을 때 값을 변경 시킬 수 있었다.

- 코드
  ```c
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
  ```
  - 콘솔
    ```
    memory/ $ make swap
    memory/ $ ./swap
    x is 1, y is 2
    x pointer: 0x7ffeb770bc28       y pointer: 0x7ffeb770bc24
    a variable: 1, a pointer: 0x7ffeb770bc28
    b variable: 2, b pointer: 0x7ffeb770bc24
    a pointer -> tmp pointer: 0x7ffeb770bbfc
    a pointer -> *a variable: 0x7ffeb770bc08
    a pointer -> *a variable: 0x7ffeb770bc00
    x is 2, y is 1
    ```
