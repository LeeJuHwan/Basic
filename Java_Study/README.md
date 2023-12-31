### 메모리 영역

- Heap Memory
- Data
- Stack Memory
    - 함수가 호출이 되면 함수를 위한 공간으로 잡는 영역
    - 지역 변수가 쓰이는 곳

### 인스턴스 생성과 힙 메모리
---

> 인스턴스
> 
- new 키워드를 사용 하여 인스턴스 생성
- 실제 클래스 기반으로 생성 된 객체는 각각 다른 멤버 변수를 갖게 됨

> Heap Memory
> 
- 동적으로 할당 되는 메모리
- 자바는 Garbage Collector가 주기적으로 사용하지 않는 메모리는 수거
- 하나의 클래스로 부터 여러개의 인스턴스가 생성되고 각각 다른 메모리 주소를 가지게 됨

### 생성자

---

- 생성자 기본 문법 <class_name>([<argument_list]) { [<statments>]} → initalize
- 객체를 생성할 때 new 키워드와 함께 사용 - new Student();
- 생성자는 일반 함수 처럼 기능을 호출하는 것이 아니고 객체를 생성하기 위해 new와 함께 호출 됨
- 객체가 생성 될 때 변수나 상수를 초기화 하거나 다른 초기화 기능을 수행하는 메서드를 호출 함
- 생성자는 반환 값이 없고, 클래스의 이름과 동일하다
- 대부분의 생성자는 외부에서 접근 가능하지만, 필요에 의해 private으로 선언되는 경우도 있음

### 기본 생성자(default constructor)

---

- 클래스에는 반드시 적어도 하나 이상의 생성자가 존재한다
- 클래스에 생성자를 구현하지 않아도 new 키워드와 함께 생성자를 호출 할 수 있음
- 클래스에 생성자가 하나도 없는 경우 컴파일러가 생성자 코드를 넣어준다
    
    ```java
    public Student() {}
    ```
    
- 매게 변수가 없고 구현부가 없다.

### 접근 제어 지시자

---

- 클래스 외부에서 클래스의 멤버 변수, 메서드, 생성자를 사용할 수 있는지 여부를 지정하는 키워드
- private : 같은 클래스 내부에서만 접근 가능 ( 외부 클래스, 상속 관계의 클래스에서도 접근 불가)
- 아무것도 없음 (default) : 같은 패키지 내부에서만 접근 가능 ( 상속 관계라도 패키지가 다르면 접근 불가)
- protected : 같은 패키지나 상속관계의 클래스에서 접근 가능하고 그 외 외부에서는 접근 할 수 없음
- public : 클래스의 외부 어디서나 접근 할 수 있음