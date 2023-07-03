package Introduction_OOP.Example;

public class Book {

    private String bookName;
    private int noOfCopies;

    public int getNoOfCopies() {
        return noOfCopies;
    }

    public void setNoOfCopies(int noOfCopies) {
        if (noOfCopies > 0) {
            this.noOfCopies = noOfCopies;
        }
    }

    Book(String bookName) {
        this.bookName = bookName;
    }

    public void updateNoOfCopies(String operator, int howMuch) {
        if (operator.equals("add")) {
            setNoOfCopies(this.noOfCopies + howMuch);
        } else if (operator.equals("del")) {
            setNoOfCopies(this.noOfCopies - howMuch);
        }
    }

    void read() {
        System.out.println("this is " + bookName);
    }
}
