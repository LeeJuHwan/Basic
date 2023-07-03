package 클래스;

public class GoToSchool {

    public static void main(String[] args) {
        Students studentJames = new Students("James", 5000);
        Students studentTomas = new Students("Tomas", 10000);

        Bus bus100 = new Bus(100);
        Subway subwayGreen = new Subway(2);

        studentJames.takeBus(bus100);
        studentTomas.takeSubway(subwayGreen);

        studentJames.showStudentInfo();
        studentTomas.showStudentInfo();

        bus100.showBusInfo();
        subwayGreen.showSubwayInfo();
    }
}
