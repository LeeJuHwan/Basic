#include <stdio.h>
#include <unistd.h>

void excuted_pid(int pid)
{
    printf("excuted %d\n", pid);
}

int main(void)
{
    if (fork() == 0) // fork는 부모 프로세스를 그대로 복사
    {
        if (fork() == 0)
        {
            printf("11번 라인 자식 프로세스의 13번 라인 자식 프로세스 아이디: %d\n", getpid());
            excuted_pid(getpid());
        }
        else
        {
            printf("11번 자식 프로세스의 아이디: %d\n", getpid());
            excuted_pid(getpid());
        }
    }
    else
    {
        if (fork() == 0)
        {
            printf("26번의 자식 프로세스 아이디: %d\n", getpid());
            excuted_pid(getpid());
        }
        else
        {
            printf("가장 최상위 부모 프로세스 아이디: %d\n", getpid());
            excuted_pid(getpid());
        }
    }
}