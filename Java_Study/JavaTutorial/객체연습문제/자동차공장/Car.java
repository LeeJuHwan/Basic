package 객체연습문제.자동차공장;

public class Car {

    private static int serialNumber = 10000;
    private int carSerialNum;

    public Car() {
        carSerialNum = ++serialNumber;
    };

    public int getCarNum() {
        return carSerialNum;
    }

}
