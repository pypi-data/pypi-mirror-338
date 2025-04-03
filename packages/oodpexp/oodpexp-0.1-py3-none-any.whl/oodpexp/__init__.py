def exp_21():
    a = '''#include <iostream>
using namespace std;

class Car {
private:
    string brand;
    int year;

public:
    // Method to set car details
    void setDetails(string b, int y) {
        brand = b;
        year = y;
    }

    // Method to display car details
    void displayDetails() {
        cout << "Car Brand: " << brand << endl;
        cout << "Manufacturing Year: " << year << endl;
    }
};

int main() {
    Car myCar;

    // Setting car details
    myCar.setDetails("Toyota", 2022);

    // Displaying car details
    myCar.displayDetails();

    return 0;
}

-------------------------------------------------------------------------------------------------------------'''
    return a


def exp_22():
    a='''#include <iostream>
using namespace std;

// Class definition
class Student {
private:
    string name;
    int age;

public:
    // Constructor
    Student(string n, int a);

    // Method declaration
    void display();
};

// Constructor definition outside the class
Student::Student(string n, int a) {
    name = n;
    age = a;
}

// Method definition outside the class
void Student::display() {
    cout << "Student Name: " << name << endl;
    cout << "Student Age: " << age << endl;
}

int main() {
    // Creating an object of Student class
    Student s1("Alice", 20);

    // Calling method
    s1.display();

    return 0;
}
----------------------------------------------------------------------------------------------------------------'''
    return a


def exp_23():
    a='''#include <iostream>
using namespace std;

// Class definition
class Adder {
private:
    int num1, num2;

public:
    // Constructor to initialize numbers
    Adder(int a, int b) {
        num1 = a;
        num2 = b;
    }

    // Method to add the two numbers
    int sum() {
        return num1 + num2;
    }
};

int main() {
    int a, b;

    // Taking input from user
    cout << "Enter two integers: ";
    cin >> a >> b;

    // Creating an object of Adder class
    Adder obj(a, b);

    // Displaying the sum
    cout << "Sum: " << obj.sum() << endl;

    return 0;
}
--------------------------------------------------------------------------------------------------------------'''
    return a


def exp_24():
    a='''#include <iostream>
using namespace std;

class Student {
private:
    string name;
    int age;
    int rollNo;

public:
    void getData() {
        cout << "Enter Name: ";
        cin >> name;
        cout << "Enter Age: ";
        cin >> age;
        cout << "Enter Roll No: ";
        cin >> rollNo;
    }

    void displayData() {
        cout << "\nStudent Information:\n";
        cout << "Name: " << name << "\nAge: " << age << "\nRoll No: " << rollNo << endl;
    }
};

int main() {
    Student s;
    s.getData();
    s.displayData();
    return 0;
}

----------------------------------------------------------------------------------------------------------------'''
    return a



def exp_25():
    a='''#include <iostream>
using namespace std;

class PrimeChecker {
private:
    int num;

public:
    void getNumber() {
        cout << "Enter a number: ";
        cin >> num;
    }

    bool isPrime() {
        if (num < 2) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
};

int main() {
    PrimeChecker p;
    p.getNumber();
    if (p.isPrime())
        cout << "The number is Prime.\n";
    else
        cout << "The number is Not Prime.\n";
    return 0;
}

-------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_26():
    a='''#include <iostream>
using namespace std;

class Complex {
private:
    int real, imag;

public:
    Complex(int r = 0, int i = 0) {
        real = r;
        imag = i;
    }

    friend Complex add(Complex c1, Complex c2);

    void display() {
        cout << real << " + " << imag << "i" << endl;
    }
};

Complex add(Complex c1, Complex c2) {
    return Complex(c1.real + c2.real, c1.imag + c2.imag);
}

int main() {
    Complex c1(3, 4), c2(5, 6);
    Complex c3 = add(c1, c2);
    cout << "Sum of Complex Numbers: ";
    c3.display();
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''

    return a



def exp_27():
    a='''#include <iostream>
using namespace std;

class Box {
private:
    int length, width, height;

public:
    Box(int l, int w, int h) {
        length = l;
        width = w;
        height = h;
    }

    int volume() {
        return length * width * height;
    }
};

int main() {
    Box b(5, 6, 7);
    cout << "Volume of Box: " << b.volume() << endl;
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_28():
    a='''#include <iostream>
using namespace std;

class Demo {
public:
    Demo() {
        cout << "Constructor Called\n";
    }

    ~Demo() {
        cout << "Destructor Called\n";
    }
};

int main() {
    Demo d;
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_29():
    a='''#include <iostream>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    void getData() {
        cout << "Enter Name: ";
        cin >> name;
        cout << "Enter Age: ";
        cin >> age;
    }

    void displayData() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

class Patient : public Person {
private:
    string disease;

public:
    void getPatientData() {
        getData();
        cout << "Enter Disease: ";
        cin >> disease;
    }

    void displayPatientData() {
        displayData();
        cout << "Disease: " << disease << endl;
    }
};

int main() {
    Patient p;
    p.getPatientData();
    p.displayPatientData();
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_30():
    a='''#include <iostream>
using namespace std;

class Base {
private:
    int privateVar = 10;
protected:
    int protectedVar = 20;
public:
    int publicVar = 30;
};

class Derived : public Base {
public:
    void display() {
        // cout << privateVar; // Not accessible
        cout << "Protected Variable: " << protectedVar << endl;
        cout << "Public Variable: " << publicVar << endl;
    }
};

int main() {
    Derived d;
    d.display();
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_31():
    a='''#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    cout << "Enter n: ";
    cin >> n;

    cout << "Odd Natural Numbers: ";
    for (int i = 1; i <= n; i++) {
        cout << 2 * i - 1 << " ";
        sum += 2 * i - 1;
    }

    cout << "\nSum: " << sum << endl;
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_32():
    a='''#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    cout << "Factors: ";
    for (int i = 1; i <= num; i++) {
        if (num % i == 0)
            cout << i << " ";
    }

    cout << endl;
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_33():
    a='''#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("data.txt");
    outFile << "Hello, File Handling!";
    outFile.close();

    ifstream inFile("data.txt");
    string content;
    while (getline(inFile, content)) {
        cout << content << endl;
    }
    inFile.close();
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_34():
    a='''#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int choice;
    do {
        cout << "1. Add\n2. Display\n3. Exit\nEnter choice: ";
        cin >> choice;

        if (choice == 1) {
            ofstream file("data.txt", ios::app);
            string text;
            cout << "Enter text: ";
            cin.ignore();
            getline(cin, text);
            file << text << endl;
            file.close();
        } else if (choice == 2) {
            ifstream file("data.txt");
            string line;
            while (getline(file, line)) {
                cout << line << endl;
            }
            file.close();
        }
    } while (choice != 3);

    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_35():
    a='''#include <iostream>
using namespace std;

template <typename T>
T getLargest(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int x = 5, y = 10;
    cout << "Largest integer: " << getLargest(x, y) << endl;

    double a = 5.5, b = 2.2;
    cout << "Largest double: " << getLargest(a, b) << endl;

    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_36():
    a='''#include <iostream>
using namespace std;

template <typename T>
void swapData(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 10, y = 20;
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swapData(x, y);
    cout << "After swap: x = " << x << ", y = " << y << endl;
    
    // Using swap with doubles as well
    double d1 = 3.14, d2 = 2.71;
    cout << "\nBefore swap: d1 = " << d1 << ", d2 = " << d2 << endl;
    swapData(d1, d2);
    cout << "After swap: d1 = " << d1 << ", d2 = " << d2 << endl;

    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_37():
    a='''#include <iostream>
using namespace std;

template <typename T>
class Calculator {
public:
    T add(T a, T b) {
        return a + b;
    }
    T subtract(T a, T b) {
        return a - b;
    }
    T multiply(T a, T b) {
        return a * b;
    }
    T divide(T a, T b) {
        if (b == 0) {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
        return a / b;
    }
};

int main() {
    Calculator<double> calc;
    double a = 20.0, b = 10.0;
    
    cout << "Addition: " << calc.add(a, b) << endl;
    cout << "Subtraction: " << calc.subtract(a, b) << endl;
    cout << "Multiplication: " << calc.multiply(a, b) << endl;
    cout << "Division: " << calc.divide(a, b) << endl;
    
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a



def exp_38():
    a='''#include <iostream>
using namespace std;

int main() {
    try {
        int numerator = 10;
        int denominator = 0;
        if (denominator == 0)
            throw "Division by zero error!";
        cout << "Result: " << numerator / denominator << endl;
    }
    catch (const char* errorMsg) {
        cout << "Exception caught: " << errorMsg << endl;
    }
    
    return 0;
}

    -------------------------------------------------------------------------------------------------------------------'''
    return a


