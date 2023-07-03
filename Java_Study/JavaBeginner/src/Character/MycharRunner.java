package Character;

public class MycharRunner {

    public static void main(String[] args) {

        MyChar myChar = new MyChar('B');

        System.out.println(myChar.isVowel());
        System.out.println(myChar.isNumber());
        System.out.println(myChar.isAlphabet());

        myChar.printLowerCaseAlphabets();
        myChar.printUpperCaseAlphabets();
    }
}
