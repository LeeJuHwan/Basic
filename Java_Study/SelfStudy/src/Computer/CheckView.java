package Computer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class CheckView {

    static CheckView check = new CheckView();

    static boolean isValidDistinct(ArrayList<Integer> numList) {
        Set<Integer> numSet = new HashSet<>(numList);

        if (numList.size() != numSet.size()) {
            return true;
        }
        return false;
    }


    public static void main(String[] args) {

        ArrayList<Integer> testList = new ArrayList<Integer>(Arrays.asList(1,1,2,3,4,5));

        System.out.println(check.isValidDistinct(testList));
    }

}
