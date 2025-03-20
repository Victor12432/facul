package Capitulo3;
//import java.util.random;
import java.util.Scanner;
public class HeartProfileTest {
    public static void main(String[] args) throws InterruptedException {
        HeartRates paciente = new HeartRates();
        Scanner input = new Scanner(System.in);

        System.out.print("Name? ");
        String generic = input.nextLine();
        paciente.setName(generic);

        System.out.print("Lastname? ");
        generic = input.nextLine();
        paciente.setLastName(generic);

        System.out.print("Date born? ");
        generic = input.nextLine();
        paciente.setBorn(generic);

        System.out.print("Weight in Kg: ");
        float genericFloat = input.nextFloat();
        paciente.setWeight(genericFloat);

        System.out.print("Height in Meters: ");
        genericFloat = input.nextFloat();
        paciente.setHeight(genericFloat);

        regist(paciente);

        
    }
    private static void regist(HeartRates prompt){
        System.out.println("Your name is "+ prompt.getName() + " " + prompt.getLastName());
        System.out.println("=====================");
        System.out.println("You have "+ prompt.ageCalcu() + " age");
        System.out.println("=====================");
        System.out.println("Your max heart rates is " + prompt.maxHR());
        System.out.println("your half heart rates is 50% - 85% is "+ prompt.halfHR() +" at " + prompt.eighfiHR());
        System.out.println("=====================");
        System.out.println("BMI VALUES \n Underweight: less than 18.5 \n Normal: between 18.5 and 24.9 \n Overweight: between 25 and 29.9 \n Obese: 30 or greater");
        System.out.println("=====================");
        System.out.println("Check your value from IMC in the table: " + prompt.imcCalcu());
    }
}
