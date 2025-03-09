package _04AndreiGodja.exercitii;

/*input string ce ar trebui sa aiba lungime minim 1. Stringul e o propozitie si fiecare cuvant este o cheie.
output: pe primul rand cate chei avem. urmand ca incepand cu randul 2 sa fie postata cate o cheie.
un cuvant=o cheie
semnele de punctuatir nu sunt considerate cuvinte ex. intr-un = doua cuvinte
o metoda ce primeste input propozitie si returneaza output dorit
 */
public class Main {
    static void procesare(String propozitie) {
        if (propozitie.isEmpty()) {
            System.out.println("Stringul este gol");
        } else {
            String replaceC = propozitie.replace(",", "").replace("'", " ").replace("?", "");

            String[] propozitieArray = replaceC.split(" ");
            System.out.println(propozitieArray.length);

            for (String st : propozitieArray) {
                System.out.println(st);
            }
        }


    }

    public static void main(String[] args) {
        String propozitie = "He is a very very good boy, isn't he?";
        procesare(propozitie);
    }
}