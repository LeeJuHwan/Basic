package 추상클래스;

public class ComputerRunner {

    public static void main(String[] args) {
        Computer deskTop = new DeskTop();
        deskTop.display();
        deskTop.turnOff();

        NoteBook myNoteBook = new MyNoteBook();
        myNoteBook.typing();
    }



}
