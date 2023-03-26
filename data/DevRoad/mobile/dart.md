## Dart Learning Guide

Dart is a programming language created by Google. It is an object-oriented, class-based, and garbage-collected language that is used to build applications for the web, mobile, and desktop. Dart is designed to be easy to learn and has features like optional typing, asynchronous programming, and a modern syntax. In this summary, we will cover some of the key features of Dart with code snippets.

## Variables

Variables in Dart can be declared using the `var` keyword, which allows the type to be inferred, or using a specific type. Here are some examples:

```dart
var name = 'John';
String greeting = 'Hello';
int age = 25;
double height = 1.75;
bool isStudent = true;
```

## Functions

Functions in Dart can be declared using the `void` keyword, which indicates that the function does not return a value, or using a specific return type. Here are some examples:

```dart
void sayHello(String name) {
  print('Hello $name');
}

int calculateSum(int a, int b) {
  return a + b;
}

double calculateBMI(double weight, double height) {
  return weight / (height * height);
}
```

## Classes

Classes in Dart are used to define objects with properties and methods. Here is an example of a class for a Person object:

```dart
class Person {
  String name;
  int age;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  void sayHello() {
    print('Hello, my name is $name');
  }
}
```

## Control Structures

Dart has the standard control structures like `if`\-`else` statements, `for` and `while` loops, and `switch` statements. Here are some examples:

```dart
// if-else statement
int x = 10;
if (x > 5) {
  print('x is greater than 5');
} else {
  print('x is less than or equal to 5');
}

// for loop
for (int i = 0; i < 5; i++) {
  print('Value of i: $i');
}

// while loop
int y = 0;
while (y < 5) {
  print('Value of y: $y');
  y++;
}

// switch statement
String color = 'red';
switch (color) {
  case 'red':
    print('The color is red');
    break;
  case 'blue':
    print('The color is blue');
    break;
  default:
    print('The color is not red or blue');
    break;
}
```

## Inheritance

Dart supports inheritance, allowing you to create classes that inherit properties and methods from a parent class. Here is an example:

```dart
class Animal {
  String name;

  Animal(String name) {
    this.name = name;
  }

  void eat() {
    print('$name is eating');
  }
}

class Dog extends Animal {
  Dog(String name) : super(name);

  void bark() {
    print('$name is barking');
  }
}
```

In this example, the `Dog` class extends the `Animal` class, inheriting the `name` property and `eat()` method. It also defines its own method, `bark()`.

## Interfaces

Dart does not have traditional interfaces, but it does have abstract classes which can be used to define an interface. Here is an example:

```dart
abstract class Animal {
  void eat();
  void makeSound();
}

class Dog implements Animal {
  void eat() {
    print('Dog is eating');
  }

  void makeSound() {
    print('Dog is barking');
  }
}
```

In this example, the `Animal` class is defined as an abstract class with two methods, `eat()` and `makeSound()`. The `Dog` class implements the `Animal` interface, providing its own implementation for both methods.

## Exceptions

Dart has built-in support for handling exceptions using `try`\-`catch` blocks. Here is an example:

```dart
try {
  int result = 10 ~/ 0; // throws an exception
} catch (e) {
  print('An exception occurred: $e');
} finally {
  print('Finally block executed');
}
```

In this example, the `try` block attempts to perform a division by zero, which throws an exception. The `catch` block catches the exception and prints a message, while the `finally` block is executed regardless of whether an exception was thrown or not.

## Asynchronous Programming

Dart has built-in support for asynchronous programming using `async` and `await` keywords. Here is an example of a function that fetches data from an API asynchronously:

```dart
import 'dart:async';
import 'package:http/http.dart' as http;

Future<String> fetchData() async {
  var response = await http.get(Uri.parse('https://example.com/data'));
  return response.body;
}
```