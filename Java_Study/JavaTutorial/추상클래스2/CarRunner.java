package 추상클래스2;

public class CarRunner {

    public static void main(String[] args) {
        Car aiCar = new AiCar();
        aiCar.run();

        System.out.println("===============");

        Car manualCar = new ManualCar();
        manualCar.run();
    }


}
