# Design Patterns
Design patterns refer to reusable solutions to commonly occurring software design problems. They are generalized templates or blueprints that can be applied to different situations to solve similar problems.

Design patterns provide a way for developers to communicate about and standardize common design practices, making it easier to understand, maintain, and modify code. They can improve code quality and reliability, reduce development time and costs, and enhance the scalability and maintainability of software systems.

## Creational Patterns

- Singleton: ensures a class only has one instance and provides a global point of access to it.
- Factory Method: defines an interface for creating objects, but lets subclasses decide which class to instantiate.
- Abstract Factory: provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- Builder: separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
- Prototype: specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

## Structural Patterns

- Adapter: converts the interface of a class into another interface that clients expect.
- Bridge: decouples an abstraction from its implementation so that the two can vary independently.
- Composite: composes objects into tree structures to represent part-whole hierarchies, and allows clients to treat individual objects and compositions of objects uniformly.
- Decorator: attaches additional responsibilities to an object dynamically.
- Facade: provides a unified interface to a set of interfaces in a subsystem, simplifying the subsystem for clients.

## Behavioral Patterns

- Chain of Responsibility: avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
- Command: encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests, queue or log requests, and support for undoable operations.
- Interpreter: defines a representation for a grammar, along with an interpreter that uses the representation to interpret sentences in the grammar.
- Iterator: provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- Mediator: defines an object that encapsulates how a set of objects interact, promoting loose coupling by keeping objects from referring to each other explicitly.