# PHP

PHP is a server-side scripting language used to develop dynamic web applications. Here are some of the basics of PHP:

### Variables

Variables in PHP are used to store data. They start with a `$` sign followed by the variable name. Here's an example:

```php
$name = "John";
```

### Data types

PHP supports different data types such as strings, integers, floats, booleans, arrays, and objects.

```php
$name = "John"; // string
$age = 30; // integer
$height = 1.75; // float
$isStudent = true; // boolean
$fruits = array("apple", "banana", "orange"); // array
```

### Conditional statements

Conditional statements are used to make decisions based on certain conditions. In PHP, we use `if`, `else if`, and `else` statements for this purpose.

```php
if ($age < 18) {
    echo "You are not allowed to vote.";
} else if ($age >= 18 && $age < 21) {
    echo "You can vote but cannot drink alcohol.";
} else {
    echo "You can vote and drink alcohol.";
}
```

### Loops

Loops are used to repeat a set of instructions multiple times. PHP supports `for`, `while`, and `foreach` loops.

```php
for ($i = 0; $i < 10; $i++) {
    echo $i . "<br>";
}

$fruits = array("apple", "banana", "orange");
foreach ($fruits as $fruit) {
    echo $fruit . "<br>";
}
```

## Object-Oriented Programming in PHP

PHP also supports object-oriented programming (OOP) paradigm. Here are some of the concepts of OOP in PHP:

### Classes and Objects

A class is a blueprint for creating objects. An object is an instance of a class. Here's an example:

```php
class Person {
    public $name;
    public $age;
    
    public function sayHello() {
        echo "Hello, my name is " . $this->name;
    }
}

$person = new Person();
$person->name = "John";
$person->age = 30;
$person->sayHello(); // Output: "Hello, my name is John"
```

### Encapsulation

Encapsulation is a mechanism of wrapping data and methods together as a single unit. In PHP, we use access modifiers such as `public`, `private`, and `protected` to implement encapsulation.

```php
class Person {
    private $name;
    private $age;
    
    public function setName($name) {
        $this->name = $name;
    }
    
    public function setAge($age) {
        $this->age = $age;
    }
    
    public function sayHello() {
        echo "Hello, my name is " . $this->name;
    }
}

$person = new Person();
$person->setName("John");
$person->setAge(30);
$person->sayHello(); // Output: "Hello, my name is John"
```

### Inheritance

Inheritance is a mechanism of creating a new class from an existing class. The new class inherits all the properties and methods of the existing class. Here's an example:

```php
class Animal {
    public function eat() {
        echo "I am eating";
    }
}

class Dog extends Animal {
    public function bark() {
        echo "Woof!";
    }
}

$dog = new Dog();
$dog->eat(); // Output: "I am eating"
$dog->bark(); // Output: "Wo
```

### Polymorphism

Polymorphism is a mechanism of using a single method or property in different ways for different classes. In PHP, we use method overloading and method overriding to implement polymorphism.

```php
class Animal {
    public function makeSound() {
        echo "Animal is making a sound";
    }
}

class Dog extends Animal {
    public function makeSound() {
        echo "Dog is barking";
    }
}

class Cat extends Animal {
    public function makeSound() {
        echo "Cat is meowing";
    }
}

$animals = array(new Dog(), new Cat());

foreach ($animals as $animal) {
    $animal->makeSound();
}
```

This will output:

```
Dog is barking
Cat is meowing
```

### Abstraction

Abstraction is a mechanism of hiding the implementation details and showing only the necessary information to the user. In PHP, we use abstract classes and interfaces to implement abstraction.

```php
interface Shape {
    public function getArea();
}

class Rectangle implements Shape {
    private $width;
    private $height;
    
    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }
    
    public function getArea() {
        return $this->width * $this->height;
    }
}

$rectangle = new Rectangle(10, 5);
echo $rectangle->getArea(); // Output: 50
```

### Static Properties and Methods

Static properties and methods belong to the class itself, rather than to an instance of the class. They can be accessed without creating an object of the class.

```php
class Counter {
    private static $count = 0;
    
    public static function increment() {
        self::$count++;
    }
    
    public static function getCount() {
        return self::$count;
    }
}

Counter::increment();
Counter::increment();
echo Counter::getCount(); // Output: 2
```

### Constructors and Destructors

Constructors are special methods that are called automatically when an object of a class is created. They are used to initialize the properties of the object.

Destructors are special methods that are called automatically when an object is destroyed, either explicitly or when the script ends. They are used to perform cleanup tasks.

```php
class Person {
    private $name;
    
    public function __construct($name) {
        $this->name = $name;
        echo "Person $this->name created <br>";
    }
    
    public function __destruct() {
        echo "Person $this->name destroyed <br>";
    }
}

$person1 = new Person("John");
$person2 = new Person("Jane");
unset($person1);

```

This will output:

```
Person John created
Person Jane created
Person John destroyed

```

### Traits

Traits are a mechanism for code reuse in PHP. They allow you to reuse a set of methods in multiple classes, without using inheritance.

```php
trait Logger {
    public function log($message) {
        echo "Logging message: $message <br>";
    }
}

class Person {
    use Logger;
    
    private $name;
    
    public function __construct($name) {
        $this->name = $name;
    }
    
    public function sayHello() {
        $this->log("Saying hello");
        echo "Hello, my name is $this->name <br>";
    }
}

$person = new Person("John");
$person->sayHello();
```

This will output:

```
Logging message: Saying hello
Hello, my name is John
```

### Type Hinting

Type hinting is a mechanism for specifying the expected data type of a parameter or return value in a method or function. It helps to prevent errors and improve code clarity.

```php
class Calculator {
    public function add(int $a, int $b): int {
        return $a + $b;
    }
}

$calculator = new Calculator();
echo $calculator->add(2, 3); // Output: 5
echo $calculator->add(2.5, 3.5); // Error: Argument 1 passed to Calculator::add() must be of the type int, float given
```