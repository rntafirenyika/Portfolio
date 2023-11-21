import java.util.Scanner;

public class SumFun {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int input, total;

        total = 0;

        //priming read
        System.out.println("Enter a non-negative integer");
        System.out.println("Or negative to exit");
        input = keyboard.nextInt();

        while (input >= 0) {
            total += input;

            System.out.println("Enter another non-negative integer");
            System.out.println("Or negative to exit");
            input = keyboard.nextInt();
        }

        System.out.println("The sum of the numbers is " + total);
    }
}
