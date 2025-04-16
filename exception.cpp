#include <iostream>
using namespace std;

int main()
{
    float i, j;

    cout << "Enter numerator: " << endl;
    std::cin >> i;
    cout << "Enter denominator:" << endl;
    std::cin >> j;

    try{

        if(j == 0)
        throw "Error";

        float k = i/j;
        cout  << i<< "/" << j << " = "<< k;
    }

    // (...) can handle any type of exception 
    // or default 

    catch(...)
    {
        cout<< "Trying to divide by zero\n";
		throw;
    }
}
