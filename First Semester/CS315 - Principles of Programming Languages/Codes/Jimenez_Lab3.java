import java.util.Scanner;

class Fraction {
    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
        simplify();
    }

    public void add(Fraction other) {
        int newNumerator = numerator * other.denominator + other.numerator * denominator;
        int newDenominator = denominator * other.denominator;
        numerator = newNumerator;
        denominator = newDenominator;
        simplify();
    }

    public void simplify() {
        int gcd = gcd(numerator, denominator);
        numerator /= gcd;
        denominator /= gcd;
    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    public String toString() {
        if (numerator == denominator) {
            return "1";
        } else if (numerator > denominator) {
            int whole = numerator / denominator;
            int remainder = numerator % denominator;
            if (remainder == 0) {
                return whole + "";
            } else {
                return whole + ", " + remainder + "/" + denominator;
            }
        } else {
            return numerator + "/" + denominator;
        }
    }
}

public class Jimenez_Lab3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numCases = scanner.nextInt();
        for (int i = 0; i < numCases; i++) {
            int num1 = scanner.nextInt();
            int den1 = scanner.nextInt();
            int num2 = scanner.nextInt();
            int den2 = scanner.nextInt();
            Fraction f1 = new Fraction(num1, den1);
            Fraction f2 = new Fraction(num2, den2);
            f1.add(f2);
            System.out.println("Case #" + (i + 1) + ": " + f1.toString());
        }
        scanner.close(); // Close the scanner
    }
}