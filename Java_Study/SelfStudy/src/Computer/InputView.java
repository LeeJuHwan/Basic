package Computer;

import java.util.ArrayList;
import java.util.Scanner;


public class InputView {

    private static final Scanner SCANNER = new Scanner(System.in);
    ArrayList<Integer> inputValueToList;

    InputView() {
        inputValueToList = new ArrayList<>();
    }

    ArrayList<Integer> inputNumber() {
        System.out.print("숫자를 입력 해 주세요: ");
        String clientInputValue = SCANNER.nextLine();
        String[] tempToSplit = clientInputValue.split("");

        for (String value : tempToSplit) {
            inputValueToList.add(Integer.parseInt(value));
        }
        return inputValueToList;
    }


    public static void main(String[] args) {
        InputView input = new InputView();

        System.out.println(input.inputNumber());
    }

}
