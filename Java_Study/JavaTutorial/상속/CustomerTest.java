package 상속;

import java.util.ArrayList;

public class CustomerTest {

    public static void main(String[] args) {

        int price = 10000;
        ArrayList<Customer> arrayList = new ArrayList<>();

        Customer customerLee = new Customer(10010, "이순신");
        Customer customerShin = new Customer(10020, "신사임당");
        Customer customerHong = new GoldCustomer(10030, "홍길동");
        Customer customerYul = new GoldCustomer(10040, "이율곡");
        Customer customerKim = new VIPCustomer(10050, "김유신", 12345);

        arrayList.add(customerLee);
        arrayList.add(customerShin);
        arrayList.add(customerHong);
        arrayList.add(customerYul);
        arrayList.add(customerKim);

        System.out.println("==== 고객 정보 출력 =====");

        for (Customer customer : arrayList) {
            System.out.println(customer.showCustomerInfo());
        }

        System.out.println("====== 할인율과 보너스 계산 ======");

        for (Customer customer : arrayList) {
            int cost = customer.calcPrice(price);
            System.out.println(customer.getCustomerName() + " 님이 " + cost + "원 지불 하셨습니다,");
            System.out.println(customer.getCustomerName() + " 님의 현재 보너스 포인트는 " + customer.bonusPoint);
        }



    }

}
