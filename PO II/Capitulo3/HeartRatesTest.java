package Capitulo3;
import java.util.Scanner;
public class HeartRatesTest {
    public static void main(String[] args) throws InterruptedException {
       HeartRates pessoa1 = new HeartRates();

       Scanner input = new Scanner(System.in);

       System.out.println("Waht is your name");
       String nome = input.nextLine();
       pessoa1.setName(nome);

       System.out.println("What is your last name?");
       nome = input.nextLine();
       pessoa1.setLastName(nome);


       System.out.println("What is your date born?");

       String age = input.nextLine();
       pessoa1.setBorn(age);

        //Thread.sleep(2000);

        regist(pessoa1);
    }

    private static void regist(HeartRates people) {
        System.out.println("Your name is "+ people.getName());
        System.out.println("Your last name is " + people.getLastName());
        System.out.println("You have "+ people.ageCalcu() + " age");
        System.out.println("Your max heart rates is " + people.maxHR());
        System.out.println("your half heart rates is 50% - 85% is "+ people.halfHR() +" - " + people.eighfiHR());
    }
}