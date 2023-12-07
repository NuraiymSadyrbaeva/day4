public class HelloWorld {
    public static void main(String[] args) {
        // Ausgabe von "Hello, World!" in der Konsole
        System.out.println("Hello, World!");
    }
}

public class SimpleCalculations {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        
        // Addition
        int sum = a + b;
        System.out.println("Summe: " + sum);
        
        // Subtraktion
        int difference = a - b;
        System.out.println("Differenz: " + difference);
        
        // Multiplikation
        int product = a * b;
        System.out.println("Produkt: " + product);
        
        // Division (ganzzahlig und mit Dezimalzahlen)
        int divisionInteger = a / b;
        System.out.println("Division (ganzzahlig): " + divisionInteger);
        
        double divisionDouble = (double) a / b;
        System.out.println("Division (Dezimalzahl): " + divisionDouble);
    }
}
