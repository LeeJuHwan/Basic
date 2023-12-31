### C - string

---

|  함수  |     내용      |           예제            |
| :----: | :-----------: | :-----------------------: |
| strcpy |  문자열 복사  | `strcpy(assign, value);`  |
| strlen | 문자열의 길이 |      `strlen(str);`       |
| strcat | 문자열 합치기 | `strcat(origin, addfor);` |
| strcmp |  문자열 비교  |   `strcmp(str1, str2);`   |

> strcpy vs strdup

- strcpy: 문자배열의 주소를 저장하는 공간이 서로 같을 때 첫번째 매개변수는 Assign될 매개변수이고, 두번째 매개변수는 복사 할 대상이 된다. 하지만, 그 크기가 달라지게 되면 컴파일 자체에서 에러를 나타낸다는 단점이 있다.

- strdup: strcpy를 활용하여 크기가 달라도 deep copy를 도와주는 함수 역할을 한다. 입력 받은 문자배열의 포인터 주소 값을 전달 받아서 문자배열의 크기보다 1증가 시킨 임시 동적 배열을 할당 하고, strcpy(임시 동적 배열, 입력 받은 매개변수)를 호출 하여 임시 동적 배열을 반환하는 형태이다.
