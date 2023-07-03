package 클래스;

public class Subway {

    private int lineNumber;
    private int passengerCount;
    private int money;

    public Subway(int lineNumber) {
        this.lineNumber = lineNumber;
    }

    public void take(int money) {
        this.money += money;
        passengerCount ++;
    }

    public void showSubwayInfo() {
        System.out.println(lineNumber + "번의 지하철 승객은" + passengerCount + "명 이고, 수입은 " + money + "원 입니다.");
    }
}
