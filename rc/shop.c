#include <stdio.h>
#include <string.h>
struct STagProduct{
    const char *mName;
    double mPrice;
};
struct STagProductStock{
    struct STagProduct mProduct;
    int mQuantity;
};
struct STagShop{
    double mCash;
    struct STagProductStock mStock[20];
};
struct STagCustomer{
    const char *mName;
    double mBudget;
    struct STagProductStock mShoppingList[10];
    int mIndex;
};
// define function - fDisplay
void fDisplay(){
    printf("---------------\n");
}
// define function - fPrintProduct
void fPrintProduct(struct STagProduct p){
    // function fDisplay - call
    fDisplay();
    printf("<PRODUCT NAME> : %s\n       <PRICE> : %.2f\n",
           p.mName,p.mPrice);
    // function fDisplay - call
    fDisplay();
}
// define function - fPrintCustomer
void fPrintCustomer(struct STagCustomer c){
    // function fDisplay - call
    printf("<CUSTOMER NAME>: %s\n      <BUDGET> : %.2f\n",
           c.mName,c.mBudget);
    // function fDisplay - call
    for(int i=0;i<c.mIndex;i++){
        // function fPrintProduct - call
        fPrintProduct(c.mShoppingList[i].mProduct);
        printf("     <SUMMARY> : %s <ORDERS> %d <ABOVE>\n",
            c.mName,c.mShoppingList[i].mQuantity);
        double cost=c.mShoppingList[i].mQuantity*c.mShoppingList[i].mProduct.mPrice;
        printf("        <COST> : %s <TOTAL> €%.2f\n",c.mName,cost);
    }
}
int main(void){
    struct STagCustomer vDoe={"John Doe",100.0};
    
    struct STagProduct vCoke={"Can Coke",1.10};
    struct STagProductStock vCokeStock={vCoke,20};
    
    struct STagProduct vBread={"Half Loaf",0.7};
    struct STagProductStock vBreadStock={vBread,2};
    
    vDoe.mShoppingList[vDoe.mIndex++]=vCokeStock;
    vDoe.mShoppingList[vDoe.mIndex++]=vBreadStock;
    // function fPrintCustomer - call
    fPrintCustomer(vDoe);
    return 0;
}