import java.util.Scanner;

public class ifs {
    public static void main(String[] args) {
        int age;
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Please enter your age: ");
        age = keyboard.nextInt();

        if (age >= 16){
            System.out.println("You can drive!");
        }
        else{
            System.out.println("You cannot drive yet!");
        }
    }

}
