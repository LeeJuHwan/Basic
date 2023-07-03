package Character;

import java.util.ArrayList;
import java.util.Arrays;

public class MyChar {

    private char string;
    ArrayList<Character> alphabets;

    MyChar(char string) {
        this.string = string;
        this.alphabets = new ArrayList<>(Arrays.asList('a','e','i','o','u','A','E','I','O','U'));
    }

    public boolean isVowel() {
        return alphabets.contains(string);
    }

    public boolean isNumber() {
        return Character.isDigit(string);
    }

    public boolean isAlphabet() {
        return Character.isAlphabetic(string);
    }

    public void printLowerCaseAlphabets() {
        for (char i = 'a'; i <= 'z'; i ++) {
            System.out.printf(i + ", ");
        }
        System.out.println();
    }

    public void printUpperCaseAlphabets() {
        for (char i = 'A'; i <= 'Z'; i ++) {
            System.out.printf(i + ", ");
        }
    }


}
