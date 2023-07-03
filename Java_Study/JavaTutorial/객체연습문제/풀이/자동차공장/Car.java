package 객체연습문제.풀이.자동차공장;

public class Car {

    private static int serialNum = 10000;
    private int carNum;

    public Car() {
        serialNum ++;
        carNum = serialNum;
    }

    public int getCarNum() {
        return carNum;
    }
}
