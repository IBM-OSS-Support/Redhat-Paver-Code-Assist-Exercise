public class Fibonacci {
    public static void main(String[] args) {
        int n = 10; // Number of terms to calculate
        int a = 0, b = 1, c;

        System.out.print("Fibonacci Series: ");

        for (int i = 1; i <= n; ++i) {
            c = a + b;
            a = b;
            b = c;
            System.out.print(c + " ");
        }
    }
}