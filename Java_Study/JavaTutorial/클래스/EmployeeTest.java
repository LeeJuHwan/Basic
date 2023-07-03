package 클래스;

public class EmployeeTest {
    public static void main(String[] args) {

        Employee employeeLee = new Employee();
        employeeLee.setEmployeeName("Lee");


        Employee employeeKim = new Employee();
        employeeKim.setEmployeeName("Kim");

        System.out.println(employeeLee.getEmployeeId());
        System.out.println(employeeKim.getEmployeeId());

        System.out.println(Employee.getSerialNum());
    }
}
