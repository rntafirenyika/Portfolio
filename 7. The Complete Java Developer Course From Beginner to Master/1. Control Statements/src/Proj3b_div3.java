import java.util.Scanner;

public class Proj3b_div3 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int number;

        System.out.print("Enter any integer: ");
        number = keyboard.nextInt();
        System.out.println("");

        if (number % 3 != 0) {
            System.out.println(number + " is NOT divisible by 3.");
        }
        else {
            System.out.println(number + " is divisible by 3.");
        }
    }
}
