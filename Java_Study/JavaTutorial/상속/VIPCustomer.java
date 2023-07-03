package 상속;

public class VIPCustomer extends Customer {

    int agentId;
    double salesRatio;


    public VIPCustomer(int customerId, String customerName, int agentId) {
        super(customerId, customerName);

        this.agentId = agentId;
        customerGrade = "VIP";
        salesRatio = 0.1;
        bonusRatio = 0.05;
    }


    @Override
    public int calcPrice(int price) {

        bonusPoint += price * bonusRatio;
        return price - (int)(price * salesRatio);
    }


    @Override
    public String showCustomerInfo() {

        return super.showCustomerInfo() + " 상담원 아이디는 " + agentId;
    }

    public int getAgentId() {
        return agentId;
    }

}
