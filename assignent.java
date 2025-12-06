public class Car {
    // Instance fields
    private String brand;
    private String model;
    private int year;
    private double speed;

    // Unchangeable shared data fields (static final)
    private static final String COMPANY_OWNER = "AutoCorp";
    private static final String COMPANY_FOUNDATION_YEAR = "1995";

    // Constructor 1: Initialize brand, model, year
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.speed = 0.0;
    }

    // Constructor overload: brand, model, year, country (extra parameter, assuming country is relevant)
    public Car(String brand, String model, int year, String country) {
        this(brand, model, year);
        // If country should be stored, add a field for it. 
        // Since not specified, we just note it's an overload example.
        System.out.println("Car manufactured in: " + country);
    }

    // Accelerate method
    public void accelerate(double increment) {
        if (increment > 0) {
            speed += increment;
            System.out.println("Speed increased by " + increment + ". Current speed: " + speed);
        }
    }

    // Overloaded accelerate method (example: with a message)
    public void accelerate(double increment, String reason) {
        accelerate(increment);
        System.out.println("Reason: " + reason);
    }

    // Brake method
    public void brake(double decrement) {
        speed -= decrement;
        if (speed < 0) {
            speed = 0;
        }
        System.out.println("Speed decreased by " + decrement + ". Current speed: " + speed);
    }

    // Display details
    public void displayDetails() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
        System.out.println("Current Speed: " + speed);
        System.out.println("Company Owner: " + COMPANY_OWNER);
        System.out.println("Company Foundation Year: " + COMPANY_FOUNDATION_YEAR);
    }

    // Optional: getters if needed
    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public double getSpeed() {
        return speed;
    }
}