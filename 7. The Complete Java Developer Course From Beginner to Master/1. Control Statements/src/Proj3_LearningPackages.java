import java.util.Scanner;

public class Proj3_LearningPackages {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int packageNum, courses, total;

        total = 0;

        System.out.println("Welcome to Learning Stars.");
        System.out.println("");
        System.out.println("Packages available:");
        System.out.println("Packages 1: $10/month, includes 2 courses per month. Each additional course is $6");
        System.out.println("Packages 2: $12/month, includes 4 courses per month. Each additional course is $4");
        System.out.println("Packages 3: $15/month, includes 6 courses per month. Each additional course is $3");
        System.out.println("");

        //prompt user for info
        System.out.print("Which of the packages do you want? 1,2 or 3: ");
        packageNum = keyboard.nextInt();
        if (packageNum <= 0 || packageNum > 3) {
            System.out.println("Invalid package code!");
            System.exit(1);
        }

        System.out.print("How many courses did you enroll for the month: ");
        courses = keyboard.nextInt();
        if (courses <= 0) {
            System.out.println("Invalid number of courses!");
            System.exit(1);
        }

        if (packageNum == 1) {
            if (courses <= 2) {
                total = 10;
            }
            else {
                total = 10 + ((courses-2) * 6);
            }
        }
        else if (packageNum == 2) {
            if (courses <= 4) {
                total = 12;
            }
            else {
                total = 12 + ((courses-4) * 4);
            }
        }
        else if (packageNum == 3) {
            if (courses <= 6) {
                total = 15;
            }
            else {
                total = 15 + ((courses-6) * 3);
            }
        }

        System.out.println("");
        System.out.println("Total for the month is $" + total);

    }// end main
}
