package Introduction_OOP;

import java.math.BigDecimal;

public class SimpleInterestFormula {

    private BigDecimal demicalPrincipal;
    private BigDecimal demicalInterest;

    SimpleInterestFormula(String principal, String interest) {
        this.demicalPrincipal = new BigDecimal(principal);
        this.demicalInterest = new BigDecimal(interest);

    }

    BigDecimal CalculateToValue(int year) {
        BigDecimal pricipalMultiply = demicalPrincipal.multiply(demicalInterest.divide(new BigDecimal(100)));
        BigDecimal multiplyYear = pricipalMultiply.multiply(new BigDecimal(year));

        return demicalPrincipal.add(multiplyYear);
    }

}
