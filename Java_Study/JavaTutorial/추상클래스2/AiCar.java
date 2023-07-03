package 추상클래스2;

public class AiCar extends Car{

    @Override
    public void drive() {
        System.out.println("자율 주행입니다.");
        System.out.println("자동차가 스스로 방향을 바꿉니다.");
    }

    @Override
    public void stop() {
        System.out.println("자동차가 멈춥니다.");
    }

    @Override
    public void fuel() {
//        System.out.println("기름을 넣습니다.");
    }
}
