from dataclasses import dataclass, field
from typing import List
import csv

from enum import IntEnum # set integer values
from os import path # file error checking
from os import system # clear screen output

# capitals represent constants
MAX_CHARACTERS=49 # display purposes only

@dataclass # original source code
class Product:
    name: str
    price: float = 0.0

@dataclass # original source code
class ProductStock:
    product: Product
    quantity: int

@dataclass # original source code
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass # original source code
class Customer:
    name: str = ''
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

def print_product(p): # original source code
    """Amend function print_product to only display the product name via:
    i. option 2 'Read Orders'.
"""   
    if p.price!=0: # option 1 "Shop Inventory"
        print(f'PRODUCT NAME: {p.name} \nPRODUCT PRICE: EUR{p.price:.2f}') # original source code
    else: # option 2 "Read Orders"
        print(f'PRODUCT NAME: {p.name}') # display name only
    ui_shop_menu_display('-',13); print() # display purposes only

def print_customer_update_shop_state(c,s):
    """Amend function print_customer (signature: 'def print_customer(c)') having:
      i. the same functionality as before;
     ii. updating shop state and;
    iii. return shop state to function main. 
"""
    count_no_product_match=0 # cart shop iterations
    shopping_cart_invoice=0.0 # empty until add
    can_fill_full_order=1 # assume is true
    count_outer_customer=0 # check equal count_inner_shop
    count_inner_shop=0 # check equal count_outer_customer

    # print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: EUR{c.budget}') # original source code
    print(f'\n\n\nCUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: EUR{c.budget:.2f}') # display purposes only
    ui_shop_menu_display('-',13); print() # display purposes only

    #
    # for each customer
    #
    for item in c.shopping_list: # original source code
        countShopIterations=0 # cart shop iterations
        count_no_product_match=0 # reset next customer

        print_product(item.product) # original source code
        print(f'{c.name} ORDERS {item.quantity:.0f} OF ABOVE PRODUCT') # original source code
        ui_shop_menu_display('-',13); print() # display purposes only

        #
        # iterate all stock
        #
        for shop_item in s.stock: # update stop state
            # cost = item.quantity * item.product.price # original source code
            cost=item.quantity*shop_item.product.price # product full cost
            countShopIterations+=1 # latter compare count_no_product_match 

            if item.product.name==shop_item.product.name: # shop stocks product
                print(f'The cost to {c.name} will be EUR{cost:.2f}') # original source code
                ui_shop_menu_display('-',13); print() # display purposes only
            else:
                count_no_product_match+=1 # determines product existence

            if item.product.name!=shop_item.product.name: # product not exist
                continue # continue sanity checking
            elif item.quantity>shop_item.quantity: # exceed shop quantity
                if shop_item.quantity<=0: # product all gone
                    print(f'(Invalid Shop Quantity: Out of Stock)   >>> {item.product.name}') # thrown appropriate error
                    print(f'The cost to {c.name} will be EUR0.00') # thrown appropriate error
                else:
                    print(f'(Invalid Shop Quantity: Quantity Limit) >>> {shop_item.quantity:.0f}') # thrown appropriate error
                    shopping_cart_invoice+=shop_item.quantity*shop_item.product.price # product partial cost 
                    print(f'The cost to {c.name} will be EUR{shop_item.quantity*shop_item.product.price:.2f}') # thrown appropriate error
                ui_shop_menu_display('-',13); print() # display purposes only
                can_fill_full_order=0 # partial order false
            elif c.budget<cost: # budget not allowing
                canOnlyAfford=int(c.budget/shop_item.product.price) # price into budget
                
                if canOnlyAfford>=int(c.budget): # complete partial order
                    print(f'Unfortunately {c.name} has a budget of EUR{c.budget:.2f}') # display purposes only
                    shopping_cart_invoice+=canOnlyAfford*shop_item.product.price # update cart affordability 
                    c.budget-=canOnlyAfford*shop_item.product.price # reduce budget accordingly
                    print(f'{c.name} can only afford {canOnlyAfford} {shop_item.product.name} at a cost of EUR{canOnlyAfford*shop_item.product.price:.2f}') # display purposes only
                    item.quantity=canOnlyAfford # quanitity shop state
                else:
                    item.quantity-=item.quantity # quanitity shop state
                    print(f'Unfortunately {c.name} cannot purchase any {shop_item.product.name}') # display purposes only
                ui_shop_menu_display('-',13); print() # display purposes only
                can_fill_full_order=0 # now partial order
            elif c.budget>=cost: # all going well
                shopping_cart_invoice+=cost # add to cart
                c.budget-=shopping_cart_invoice # reduce down budget
            
            shop_item.quantity-=item.quantity # quanitity shop state

            if shop_item.quantity<0: # shop negative quantities                
                shop_item.quantity=0 # quanitity shop state
            
            count_inner_shop+=1 # full partial order

        #
        # onto next customer
        #
        if countShopIterations==count_no_product_match: # iteration no match
            print(f'(Invalid Shop Product: <NOT IN STOCK>)  >>> {item.product.name}') # thrown appropriate error
            print(f'The cost to {c.name} will be EUR0.00') # thrown appropriate error
            ui_shop_menu_display('-',13); print() # display purposes only

        count_outer_customer+=1 # full partial order                

    #
    # all customers done
    #
    if shopping_cart_invoice>0: 
        if can_fill_full_order==1 and count_inner_shop==count_outer_customer:
            print(f'(Completed <FULL> Order: Now Due)       >>> EUR{shopping_cart_invoice:.2f}') # display full order
        else:
            print(f'(Completed <PARTIAL> Order: Now Due)    >>> EUR{shopping_cart_invoice:.2f}') # display partial order
    else:
        print(f'(Invalid Order: <NIL> Shopping Cart)    >>> EUR{shopping_cart_invoice:.2f}') # thrown appropriate error

    s.cash+=shopping_cart_invoice # cash shop state

    return s # full shop state

def print_shop(s): # original source code
    """Function print_shop having no original functionality changed:
    i. minor amendments for display purposes only.
""" 
    print(f'Shop has {s.cash:.2f} in cash') # original source code
    ui_shop_menu_display('_',24); print(); print() # display partial order
    for item in s.stock: # original source code
        print_product(item.product) # original source code
        print(f'The Shop has {item.quantity:.0f} of the above') # original source code
        ui_shop_menu_display('-',13); print() # partial order display

def create_and_stock_shop():
    """Amend function create_and_stock_shop (otherwise unchanged) having:
     i. error message displayed (before exit) if the file (stock.csv) cannot be located (or name is changed).
    Additional:
    ii. closing file (stock.csv) after reading (returning the shop state to main - now in memory).
"""
    s = Shop()

    try: # handle runtime exceptions
        with open('../stock.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            s.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                s.stock.append(ps)
                #print(ps)            
    except FileNotFoundError: # check file exists
        shop_menu_display_header('ERROR - stock.csv!'); # display purposes only
        exit() # terminate the program

    csv_file.close() # close CSV file
    
    return s

def read_customer(file_path): # original source code
    """Amend function read_customer using most of the original functionality:
    i .adding additional error runtime exceptions.
""" 
    try: # handle runtime exceptions
        with open('../'+file_path) as csv_file: # original source code           
            csv_reader = csv.reader(csv_file, delimiter=',') # original source code
            first_row = next(csv_reader) # original source code
            c = Customer(first_row[0], float(first_row[1])) # original source code
            for row in csv_reader: # original source code
                name = row[0] # original source code
                quantity = float(row[1]) # original source code
                p = Product(name) # original source code
                ps = ProductStock(p, quantity) # original source code
                c.shopping_list.append(ps) # original source code             
    except FileNotFoundError: # check file exists
        print(f'(Invalid File: CSV file does not exist) >>> {file_path}\n') # prompt error message
        name=''; # customer not exist
        budget=0 # therefore no budget
        notRealCustomer=Customer(name,budget) # create non-existent customer
        return notRealCustomer # return dummy customer
    else:

        csv_file.close() # close CSV file 

        if c.budget==0: # see customer david.csv
            print(f'\n\n\n\t\t<<<<<NO MONEY>>>>>') # display purposes only

        return c # original source code

def create_customer_live_mode():
    """Function create_customer_live_mode via shop menu option 3 "Live Mode" and return live customer.
"""
    shop_menu_live_display_header() # display purposes only

    print(f'(Valid Input: Customer Name)            >>> ',end="") # display purposes only
    while True: # infinite until False
        try: # handle runtime exceptions
            name=str(input()) # user input string
            if name=='': # check no input
                raise ReplicateShopDotCError('COMMENT: allow newline character') # replicate shop.c behaviour
        except (ValueError, # check for string
            ReplicateShopDotCError): # custom exception created
            print(end="") # shop.c allows newline
        else:
            break # nothing to do

    print(f'(Valid Input: Customer Budget)          >>> EUR',end="") # display purposes only
    while True: # infinite until False
        try: # handle runtime exceptions
            budget=float(input()) # user input string
            while budget<=0: # error check budget
                print(f'(Valid Input: Customer Budget)          >>> EUR',end="") # display purposes only
                budget=float(input()) # continue until correct
        except ValueError: # check for float
            print(end="") # shop.c allows newline
        else:
            c=Customer(name.capitalize(),budget) # populate live customer
            break

    return c

def create_live_mode_checkout(cart):
    """ Function create_live_mode_checkout passing live customer via function create_customer_live_mode and return cart.
""" 
    class live_menu_choice(IntEnum): # set integer values [1] 
        quit=0 # False then exit
        add_product_to_cart=1 # shop option 1

    shop_menu_live_display_header() # display purposes only
    shop_menu_live_display() # display purposes only
    
    while True: # infinite until False        

        try: # handle runtime exceptions
            user=str(input()) # user input integer
            if user=='': # check no input
                raise ReplicateShopDotCError('COMMENT: allow newline character') # replicate shop.c behaviour
        except (ValueError, # check for characters
            ReplicateShopDotCError): # custom exception created
            print(end="") # shop.c allows newline
        else:
            pass

        try:
            user=int(user) # correct format integer
            if user<0 or user>len(live_menu_choice)-1: # range interval [0,2)
                raise ShopMenuChoiceError('COMMENT: allowable input [0,1]') # outside choice range
        except (ValueError, # check for characters
            ShopMenuChoiceError): # custom exception created 
            print(end="") # shop.c allows newline
        else:

            if user==live_menu_choice.quit: # user input 0
                return cart # send back cart
            elif user==live_menu_choice.add_product_to_cart: # user input 1
                print(f'(Valid Input: Product Name - Case-sensitive!)') # display purposes only
                print(f'(Correct Uppercase/Lowercase Letters)   >>> ',end="") # display purposes only
                p_name=str(input()) # input product name
                p_price=0; # not displaying price

                while True:
                    print(f'(Valid Input: Product Quantity)         >>> ',end="") # display purposes only
                    try:
                        quantity=int(input()) # user input integer
                        if quantity<=0: # zero or negative
                            raise ValueError # continue requesting input
                    except ValueError: # check for characters
                        continue
                    else:
                        break

                product=Product(p_name,p_price) # populate the dataclass
                customer_item=ProductStock(product,quantity) # populate the dataclass

                cart.shopping_list.append(customer_item) # full shopping cart
                shop_menu_live_display() # display purposes only

    return cart # live customer basket

def main():
    """Implementation ground zero.
""" 
    class shop_menu_choice(IntEnum): # set integer values [1] 
        quit=0 # False then exit
        shop_inventory=1 # shop option 1
        read_orders=2 # shop option 2
        live_mode=3 # shop option 3

    shop=create_and_stock_shop() # CSV return shop

    system('clear') # clear screen output [2]
    shop_menu_display() # display purposes only

    while True: # infinite until False
        try: # handle runtime exceptions
            user=int(input()) # user input integer
            if user<0 or user>len(shop_menu_choice)-1: # range interval [0,4)
                raise ShopMenuChoiceError('COMMENT: allowable input [0,3]') # outside choice range
        except (ValueError, # check for characters
            ShopMenuChoiceError, # custom exception created 
            EOFError, # input EOF Ctrl-Z
            KeyboardInterrupt): # terminate Ctrl-C etc
            shop_menu_display_header('Invalid Choice!!!!'); print() # display purposes only
            shop_menu_display() # display purposes only
        else:

            if user==shop_menu_choice.quit: # user input 0
                shop_menu_display_header('\tBye!'); print() # display purposes only
                break # exit program bye!
            if user==shop_menu_choice.shop_inventory: # user input 1
                shop_menu_display_header('1 - Shop Inventory'); print() # display purposes only
                print_shop(shop) # display shop inventory
                shop_menu_display_footer() # display purposes only
            if user==shop_menu_choice.read_orders: # user input 2
                shop_menu_display_header('2 -  Read Orders'); print() # display purposes only
                print(f'(Valid Input: Name - excluding \'.csv\')  >>> ',end="") # CSV name only
                csv_file=str(input()).lower()+'.csv' # CSV excluding '../'
                customer=read_customer(csv_file) # read customer CSV
                if customer.name!="" and customer.budget!=0: # read_customer not notRealCustomer
                    shop=print_customer_update_shop_state(customer,shop) # update shop state
                shop_menu_display_footer() # display purposes only
            if user==shop_menu_choice.live_mode: # user input 3
                shop_menu_display_header('  Shop Inventory'); print() # display purposes only
                print_shop(shop) # display shop inventory
                live_customer=create_customer_live_mode() # create live customer
                live_customer_cart=create_live_mode_checkout(live_customer) # create shopping basket 
                system('clear') # clear screen output [2]               
                shop=print_customer_update_shop_state(live_customer_cart,shop) # update shop state
                shop_menu_display_footer() # display purposes only

'''
 *
 * Custom exception handling (includes programmer message).
 *
'''

class ShopMenuChoiceError(ValueError): pass # input outside range

class ReplicateShopDotCError(ValueError): pass # allow newline character 

"""
 * 
 * Display purposes only (no functionality).  
 *
"""

def ui_shop_menu_display(c, n):
    """Display purposes only.
""" 
    for i in range(n):
        print(c,end='')

def shop_menu_display():
    """Display purposes only.
"""     
    ui_shop_menu_display('+',MAX_CHARACTERS)
    print(f'\n\t\t------ SHOP ------')
    print(f'\t\t1 - Shop Inventory')
    print(f'\t\t2 -  Read Orders')
    print(f'\t\t3 -   Live Mode')
    print(f'\t\t0 -     Exit')
    ui_shop_menu_display('+',MAX_CHARACTERS)
    print(f'\n(Valid Input: 0 or 1 or 2 or 3)\t\t>>> ',end='')

def shop_menu_display_header(s):
    """Display purposes only.
""" 
    system('clear') # clear screen output [2]
    ui_shop_menu_display('\n',3) # display range [1,3]
    ui_shop_menu_display('\t',2); print(s) # display line 4
    ui_shop_menu_display(' ',16); ui_shop_menu_display('-',18) # display line 5
    ui_shop_menu_display('\n',3) # display range [6,8]    

def shop_menu_display_footer():
    """Display purposes only.
""" 
    ui_shop_menu_display('\n',3) # display range [1,3]
    ui_shop_menu_display(' ',16); ui_shop_menu_display('-',18) # display line 4
    ui_shop_menu_display('\n',4) # display range [5,7]
    shop_menu_display() # display shop men

def shop_menu_live_display_header():
    """Display purposes only.
"""     
    ui_shop_menu_display('\n',3)
    ui_shop_menu_display(' ',16); ui_shop_menu_display('-',18)
    ui_shop_menu_display('\n',4)

def shop_menu_live_display():
    """Display purposes only.
""" 
    ui_shop_menu_display('+',MAX_CHARACTERS)
    print(f'\n\t\t---- LIVE MODE----')
    print(f'\t\t1 -  Add to Cart')
    print(f'\t\t0 -     Exit')
    ui_shop_menu_display('+',MAX_CHARACTERS)
    print(f'\n(Valid Input: 0 or 1)\t\t\t>>> ',end='')  

if __name__=='__main__': # __name__ current module
    main() # call function main

'''
 *
 * References:
 * [1] https://www.python.org/dev/peps/pep-0435/#intenum
 * [2] https://codecap.org/clear-screen-in-python/
 *
'''