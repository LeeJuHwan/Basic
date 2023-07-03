package Computer;

import java.util.ArrayList;
import java.util.Random;

public class Computer extends CheckView {

    static Computer com = new Computer();
    private ArrayList<Integer> randomIntList;
    private Random rand;

    public Computer() {
        randomIntList = new ArrayList<>();
        rand = new Random();
    }

    ArrayList<Integer> createRandomNumber() {
        for (int i = 0; i < 3; i++) {
            com.randomIntList.add(rand.nextInt(1, 10));
        }
        return com.randomIntList;
    }

    ArrayList<Integer> duplicateRemove(ArrayList<Integer> numList) {
        boolean duplicateCheck = isValidDistinct(numList);

        if (duplicateCheck) {
            while (duplicateCheck) {
                createRandomNumber();
            }
            return com.randomIntList;
        }
        return com.randomIntList;
    }

    public ArrayList<Integer> run() {
        return duplicateRemove(createRandomNumber());
    }

    public static void main(String[] args) {

        Computer com = new Computer();

        System.out.println(com.run());
    }
}
