package Introduction_OOP;

public class MotorBikeRunner {

    public static void main(String[] args) {

        MotorBike ducati = new MotorBike(100);
        MotorBike honda = new MotorBike(80);

        ducati.start();
        honda.start();

        System.out.println(ducati.getSpeed());
        System.out.println(honda.getSpeed());

        ducati.increaseSpeed(30);
        honda.increaseSpeed(30);

        ducati.decreaseSpeed(30);
        honda.decreaseSpeed(110);


    }

}
