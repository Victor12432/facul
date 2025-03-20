package Capitulo3;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.Period;

public class HeartRates extends IMC {
    private String name, lastName, born, gender;

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    public String getLastName(){
        return lastName;
    }
    public void setBorn(String born){
        this.born = born;
    }
    public String getBorn(){
        return born;
    }
    public void setGender(String gender){
        this.gender = gender;
    }
    public String getGender(){
        return gender;
    }

    public int ageCalcu(){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MM yyyy");

        LocalDate dateNow = LocalDate.now();

        LocalDate dateBorn = LocalDate.parse(born, formatter);

        Period period = Period.between(dateBorn, dateNow);

        return period.getYears();
    }
    public int maxHR(){
        int number = ageCalcu();
        return 220 - number;
    }

    public float halfHR(){
        return (float) (maxHR() * 0.5);
    }
    public float eighfiHR(){
        return (float) (maxHR() * 0.85);
    }
}
