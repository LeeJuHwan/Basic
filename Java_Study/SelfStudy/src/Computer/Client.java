package Computer;

import java.util.ArrayList;

public class Client extends CheckView {

    //    Design pattern -> Singleton pattern: InputView
    static InputView input = new InputView();

//    public ArrayList<Integer> run() {
//        return duplicateRemove(createRandomNumber());
//    }

    public static void main(String[] args) {
    /* 1. Client check to duplicate: values in array list
       2. Client check to length: have 3 values */
        Client client = new Client();
        System.out.println(client.isValidDistinct(input.inputNumber()));

        System.out.println(client.getClass().getSimpleName());
    }
}
