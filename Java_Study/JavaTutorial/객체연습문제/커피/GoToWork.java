package 객체연습문제.커피;

public class GoToWork {

    public static void main(String[] args) {

        CoffeShop starCoffeShop = new CoffeShop("별다방");
        CoffeShop beanCoffeShop = new CoffeShop("콩다방");

        starCoffeShop.showMenu();
        beanCoffeShop.showMenu();

        Customer customerLee = new Customer("Lee", 10000);
        String payment = starCoffeShop.takeOrder(customerLee.name, "아메리카노", customerLee.money);
        System.out.println(payment);

        Customer customerKim = new Customer("Kim", 10000);
        String payment2 = beanCoffeShop.takeOrder(customerKim.name, "라떼", customerKim.money);
        System.out.println(payment2);

        Customer customerJohn = new Customer("John", 20);
        String payment3 = beanCoffeShop.takeOrder(customerJohn.name, "라떼", customerJohn.money);
        System.out.println(payment3);
    }


}
