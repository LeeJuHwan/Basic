package 객체연습문제.자동차공장;

public class CarFactoryTest {

    public static void main(String[] args) {
        CarFactory factory = CarFactory.getInstance();
        Car mySonata = factory.createCar();
        Car yourSonata = factory.createCar();

        System.out.println(mySonata.getCarNum());     //10001 출력
        System.out.println(yourSonata.getCarNum());   //10002 출력
    }
}

