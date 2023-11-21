#include <iostream>
using namespace std;

struct Product
{
    string name;
    float weight;
    float price;
};

void read_Product_Record(Product & new_ProductP)
{
    cout << "Enter product name: ";
    getline(cin, new_ProductP.name, '\n');
    cout << "Enter product weight: ";
    cin >> new_ProductP.weight;
    cout << "Enter product price R: ";
    cin >> new_ProductP.price;
}

int main()
{
    Product new_Product;

    read_Product_Record(new_Product);
    cout << new_Product.name << endl;
    cout << new_Product.weight << endl;
    cout << new_Product.price << endl;

    return 0;
}
