package ForLoop;

public class WhileNumberPlayer {

    int LIMIT;

    WhileNumberPlayer(int number) {
        this.LIMIT = number;
    }

    public void printSquareLimit() {
        int i = 1;
        while (i * i <= LIMIT) {
            System.out.print(i * i + " ");
            i++;
        }
        System.out.println();
    }

    public void printCubesUptoLimit() {
        int i = 1;
        while(Math.pow(i, 3) < LIMIT) {
            System.out.print((int) Math.pow(i, 3) + " ");
            i ++;
        }
    }


}
