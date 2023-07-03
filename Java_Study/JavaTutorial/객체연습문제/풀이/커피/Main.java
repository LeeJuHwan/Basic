package 객체연습문제.풀이.커피;

public class Main {

    public static void main(String[] args) {

        Person personKim = new Person("Kim", 10000);
        Person personLee = new Person("Lee", 10000);

        StarCoffee starCoffee = new StarCoffee();
        BeanCoffee beanCoffee = new BeanCoffee();

        personKim.buyStarCoffee(starCoffee, Menu.STARAMERICANO);
        personLee.buyBeanCoffee(beanCoffee, Menu.BEANLATTE);
    }
}
