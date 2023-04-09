# Bash Scripting
Bash scripting is a powerful tool for automating repetitive tasks and performing complex operations. In this learning summary, we will cover some of the fundamental concepts and commands that will take you from zero to hero in Bash scripting.

## Basic Script Structure

A Bash script is a file containing a sequence of commands and instructions that can be executed by the Bash shell. Here's a basic structure for a Bash script:

```bash
#!/bin/bash

# Comments start with a hash symbol
# Declare variables and functions here

# Main script logic here
```

The first line specifies the interpreter to use (in this case, Bash). Comments start with a hash symbol, and variables and functions can be declared and defined before the main script logic.

## Variables and Input

Variables are used to store values that can be referenced and manipulated in a Bash script. Here's how to declare and use variables:

```bash
my_var="Hello, World!"
echo $my_var
```

You can also prompt the user for input using the `read` command:

```bash
echo "What's your name?"
read name
echo "Hello, $name!"
```

## Conditionals and Loops

Conditionals and loops are used to control the flow of a Bash script. Here's how to use an `if` statement:

```bash
if [ $num -eq 0 ]; then
  echo "The number is zero."
elif [ $num -gt 0 ]; then
  echo "The number is positive."
else
  echo "The number is negative."
fi
```

Here's how to use a `for` loop to iterate over a range of numbers:

```bash
for i in {1..10}; do
  echo $i
done
```

## Functions

Functions are reusable blocks of code that can be called multiple times from within a Bash script. Here's how to define and use a function:

```bash
function greet {
  echo "Hello, $1!"
}

greet "Alice"
greet "Bob"
```

## Command Line Arguments

Command line arguments can be passed to a Bash script and accessed within the script using the `$1`, `$2`, etc. variables. Here's an example:

```bash
echo "The first argument is: $1"
echo "The second argument is: $2"
```

## Conclusion

This learning summary covers only the basics of Bash scripting, but it should provide a good starting point for further exploration. By mastering these concepts and commands, you'll be able to create powerful scripts that automate repetitive tasks, manipulate data, and control the flow of execution. With practice and experience, you can become a Bash scripting hero and use it to solve complex problems and streamline workflows.