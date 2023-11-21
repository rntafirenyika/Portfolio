import java.util.Scanner;

public class average {
    public static void main(String[] args) {
        int i1, i2, i3;
        float average;

        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter the first integer: ");
        i1 = keyboard.nextInt();

        System.out.println("Enter the second integer: ");
        i2 = keyboard.nextInt();

        System.out.println("Enter the third integer: ");
        i3 = keyboard.nextInt();

        average = (i1 + i2 + i3) / 3f;

        System.out.println(average);

    }
}
