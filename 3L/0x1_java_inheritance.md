# Inheritance
Object-oriented programming allows you to define new classes from existing classes.This is called inheritance.
## Superclasses and Subclasses
Inheritance enables you to define a general class and later extend it to more specialized classes.
```
public class Geometric{
  private String color="white";
  private boolean filled;
  private java.util.Date dateCreated;
  public Geometric(){
     dateCreated=new java.util.Date();
  }
  public Geometric(String color){
     dateCreated=new java.util.Date();
     this.color=color;
  }
  public String getColor(){
     this.color=color;
  }
   public String setColor(){
     this.color=color;
  }
}
```
```
public class Circle extends Geometric{
  private double radius;
  public Circle(){
  }
  public Circle(double radius){
     this.radius=radius;
  }
  public Circle(double radius,String color){
     this.radius=radius;
     setColor(color);     
  }
}
```
The keyword 'extends' tells the compiler that the 'Circle' class extends the 'Geometric' calss, thus inheriting the methods 'getColor'.
The overloaded constructor 'Circle(double radius,String color)' is implemented by invoking the'setColor' methods to set the 'color'.
The public method is defined in the superclass 'Geometric' and is inherited in 'Circle',so they can be used in the 'Circle' class. 
## Using the 'super' keyword
The keyword 'super' refers to the superclass and can be used to invoke the superclass's methods and constructors.
- To call a superclass constructor.
- To call a superclass method.
The ayntax:
```
 public Circle(double radius,String color){
     super(color);
     this.radius=radius;   
  }
```
```
public void printColor(){
     System.out.printIn("The color is "+super.getColor()+" and the radius is "+radius);
}
```
## Overriding vs. Overloading
- Overriding means to provide a new implementation for a method in the subclass.To override a method,the method must be defined in the subclass using the same signature and the same return type as in its supercalss.
- Overloading means to define multipple methods with the same name but different signatures.
```
public class Test{
	  public static void main(String[] args) {
		  A a=new A();
		  a.p(10);
		  a.p(10.0);
	  }
}
class B{
	public void p(double i) {
		System.out.println(i*2);
	}
}
class A extends B{
	//This method overrides the method in B
	public void p(double i) {
		System.out.println(i);
	}
}
```
```
public class Test{
	  public static void main(String[] args) {
		  A a=new A();
		  a.p(10);
		  a.p(10.0);
	  }
}
class B{
	public void p(double i) {
		System.out.println(i*2);
	}
}
class A extends B{
	//This method overloads the method in B
	public void p(int i) {
		System.out.println(i);
	}
}
```
When you run the Test class in the first code,both 'a.p(10)' and 'a.p(10.0)' invoke the 'p(double i)' method defined in calss 'A' to display 10.0.But in the second code,'a.p(10)' invokes the 'p(int i)' method to display 10,and 'a.p(10.0)' invokse the 'p(double i)' method to display 20.0.
### Note the following:
- Overridden methods  are in defferent classes related by inheritance;overloaded methods can be either in the same classes or different classes  related by inheritance.
