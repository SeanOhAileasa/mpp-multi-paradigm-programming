public final class Person {
    private final String name;
    private final int age;
    
    public Person(String name, int age) {
    this.name=name;
    this.age=age;
    }
    
    public String toString() {
        return "Name: " + this.name + " Age: " + this.age;
    }
    
    public static void main(String[] args) {
        Person a = new Person("Alice", 12);
        Person b = new Person("John", 34);
        System.out.println(a); // automatically calls toString
        System.out.println(b);       
    }
}
