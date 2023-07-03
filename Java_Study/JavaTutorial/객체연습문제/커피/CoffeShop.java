package 객체연습문제.커피;

import java.util.HashMap;
import java.util.Map;

public class CoffeShop {

    Map<String, Integer> coffeeMenu = new HashMap<>() {{
        put("아메리카노", 4000);
        put("라떼", 4500);
    }};
    private String shopName;

    public CoffeShop(String shopName) {
        this.shopName = shopName;
    }

    public void showMenu() {
        System.out.println("################################");
        System.out.printf("어서오세요 %s 매장 입니다.\n", shopName);
        coffeeMenu.forEach((strKey, intValue) -> {
            System.out.println(strKey + ":" + intValue);
        });
        System.out.println("################################");
        System.out.println();
    }

    public boolean isEnoughMoney(String customerOrderMenu, int customerMoney) {
        int coffeePrice = coffeeMenu.get(customerOrderMenu);

        if (coffeePrice > customerMoney) {
            return false;
        }
        return true;
    }

    public String takeOrder(String customerName, String customerOrderMenu, int customerMoney) {
        int  coffeePrice = coffeeMenu.get(customerOrderMenu);

        System.out.println("result:" + isEnoughMoney(customerOrderMenu, customerMoney));
        if (isEnoughMoney(customerOrderMenu, customerMoney) == false) {
            String failedMessage = "금액이 부족합니다.";
            return failedMessage;
        }
        System.out.println(coffeePrice + " 원이 결제 되었습니다.");
        String successMessage = customerName + " 님이 " + shopName + "에서 " + customerOrderMenu + "를 구매 하였습니다.";
        return successMessage;
    }
}
