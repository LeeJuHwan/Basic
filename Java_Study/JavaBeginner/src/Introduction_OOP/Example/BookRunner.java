package Introduction_OOP.Example;

public class BookRunner {

    public static void main(String[] args) {
        Book artOfComputerProgramming = new Book("Art Of Computer Programming");
        Book effectiveJava = new Book("Effective Java");
        Book cleanCode = new Book("Clean Code");

        artOfComputerProgramming.read();
        effectiveJava.read();
        cleanCode.read();

        artOfComputerProgramming.setNoOfCopies(100);
        effectiveJava.setNoOfCopies(300);
        cleanCode.setNoOfCopies(1);

        cleanCode.updateNoOfCopies("del", 50);

        System.out.println(cleanCode.getNoOfCopies());
    }
}
