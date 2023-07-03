package 객체연습문제.풀이.자동차공장;

public class CarFactory {

    private static CarFactory instance = new CarFactory();
    private CarFactory() {}

    public static CarFactory getInstance() {

        if (instance == null) {
            instance = new CarFactory();
        }
        return instance;
    }

    public Car createCar() {
        Car car = new Car();
        return car;
    }


}
