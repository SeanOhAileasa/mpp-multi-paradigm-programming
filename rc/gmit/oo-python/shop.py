import csv

from enum import IntEnum # set integer values
from os import path # file error checking
from os import system # clear screen output

# 
# define class Product
#
class Product:

    #
    # instance attributes initialiser
    # 
    def __init__(self,name,price=0): # default Product state
        """Initialise (specify) object initial attributes:
         i. name;
        ii. price.
    """    
        self.name=name # assign instance attribute
        self.price=price # assign instance attribute
    # --- END (instance attributes) ---

# ------------------------------------------------
# --------------- END (class Product) ------------
# ------------------------------------------------

# 
# define class ProductStock
#
class ProductStock:
    
    #
    # instance attributes initialiser
    # 
    def __init__(self,product,quantity): # default ProductStock state
        """Initialise (specify) object initial attributes:
         i. product;
        ii. quantity.
    """      
        self.product=product # assign instance attribute
        self.quantity=quantity # assign instance attribute
    # --- END (instance attributes) ---

# ------------------------------------------------    
# --------------- END (class ProductStock) -------
# ------------------------------------------------

# 
# define class Customer
#
class Customer():
    
    #
    # instance attributes initialiser
    #    
    def __init__(self,path): # default Customer state
        """Read CSV and initialise (specify) object initial attributes:
         i. name;
        ii. budget.
    """      
        self.shopping_list=[] # assign instance attribute
        try: # handle runtime exceptions
            with open('../'+path) as csv_file:
                csv_reader=csv.reader(csv_file, delimiter=',')
                first_row=next(csv_reader)
                self.name=first_row[0] # assign instance attribute
                self.budget=float(first_row[1]) # assign instance attribute
                for row in csv_reader:
                    name=row[0]
                    quantity=float(row[1])
                    p=Product(name)
                    ps=ProductStock(p,quantity)
                    self.shopping_list.append(ps) # populate instance attribute
        except FileNotFoundError: # check file exists
            print(f'(Invalid File: CSV file does not exist) >>> {path}\n') # prompt error message
            self.name=''; # assign attribute empty
            self.budget=0 # assign attribute zero
        else:

            csv_file.close() # close CSV file 

            if self.budget==0: # see customer david.csv
                print(f'\n\n\n\t\t<<<<<NO MONEY>>>>>') # display purposes only
    # --- END (instance attributes) ---

# ------------------------------------------------
# --------------- END (class Customer) -----------
# ------------------------------------------------

# 
# define class Shop
#
class Shop():

    #
    # class attributes all
    #
    MAX_CHARACTERS=49 # display purposes only
    class shop_menu_choice(IntEnum): # set integer values
        quit=0 # False then exit
        shop_inventory=1 # shop option 1
        read_orders=2 # shop option 2
        live_mode=3 # shop option 3
    class ShopMenuChoiceError(ValueError): pass # input outside range
    # --- END (class attributes) ---

    #
    # instance attributes initialiser
    #
    def __init__(self,path): # default Shop state
        self.stock=[] # assign instance attribute
        try: # handle runtime exceptions
            with open(path) as csv_file:
                csv_reader=csv.reader(csv_file, delimiter=',')
                first_row=next(csv_reader)
                self.cash=float(first_row[0]) # assign instance attribute
                for row in csv_reader:
                    p=Product(row[0], float(row[1]))
                    ps=ProductStock(p, float(row[2]))
                    self.stock.append(ps) # populate instance attribute
        except FileNotFoundError: # check file exists
            self.shop_menu_display_header('ERROR - stock.csv!'); # call instance method
            exit() # terminate the program

        csv_file.close() # close CSV file
    
        system('clear') # clear screen output
        self.shop_menu_display() # call instance method

    # --- END (instance attributes) ---

    #
    # class instance methods
    #
    def ui_shop_menu_display(self,c,n):
        """Display purposes only.
    """
        for i in range(n):
            print(c,end='')

    def shop_menu_display_header(self,s):
        """Display purposes only (using instance method ``ui_shop_menu_display``).
    """
        system('clear') # clear screen output
        self.ui_shop_menu_display('\n',3) # call instance method
        self.ui_shop_menu_display('\t',2); print(s) # call instance method
        self.ui_shop_menu_display(' ',16); self.ui_shop_menu_display('-',18) # call instance method
        self.ui_shop_menu_display('\n',3) # call instance method

    def shop_menu_display(self):
        """Display purposes only (using instance method ``ui_shop_menu_display``) and 
        call instance method ``shop_menu``. Utilising class attribute ``MAX_CHARACTERS``.
    """
        self.ui_shop_menu_display('+',self.MAX_CHARACTERS) # call instance method
        print(f'\n\t\t------ SHOP ------')
        print(f'\t\t1 - Shop Inventory')
        print(f'\t\t2 -  Read Orders')
        print(f'\t\t3 -   Live Mode')
        print(f'\t\t0 -     Exit')
        self.ui_shop_menu_display('+',self.MAX_CHARACTERS) # call instance method
        print(f'\n(Valid Input: 0 or 1 or 2 or 3)\t\t>>> ',end='')

        # ***behaviour sequence pattern***
        self.shop_menu() # call instance method
        # ################################

    def print_product(self,p):
        """Amend function print_product to only display the product name via:
        i. option 2 'Read Orders'.

        (using instance method ``ui_shop_menu_display``)
    """   
        if p.price!=0: # option 1 "Shop Inventory"
            print(f'PRODUCT NAME: {p.name} \nPRODUCT PRICE: EUR{p.price:.2f}') # original source code
        else: # option 2 "Read Orders"
            print(f'PRODUCT NAME: {p.name}') # display name only
        self.ui_shop_menu_display('-',13); print() # call instance method

    def print_shop(self,s):
        """Method print_shop having no original functionality changed:
         i. minor amendments for display purposes only;
        ii. using instance method ``ui_shop_menu_display`` for display purpoes.
    """ 
        print(f'Shop has {s.cash:.2f} in cash') # original source code
        self.ui_shop_menu_display('_',24); print(); print() # call instance method
        for item in s.stock: # original source code
            self.print_product(item.product) # call instance method
            print(f'The Shop has {item.quantity:.0f} of the above') # original source code
            self.ui_shop_menu_display('-',13); print() # call instance method

    def shop_menu_display_footer(self):
        """Display purposes only (using instance method ``ui_shop_menu_display``) and 
        call instance method ``shop_menu_display``.
    """
        self.ui_shop_menu_display('\n',3) # call instance method
        self.ui_shop_menu_display(' ',16); self.ui_shop_menu_display('-',18) # call instance method
        self.ui_shop_menu_display('\n',4) # call instance method

        # ***behaviour sequence pattern***
        self.shop_menu_display() # call instance method
        # ################################

    def print_customer_update_shop_state(self,c,s):
        """Method:
         i. updating shop state;
        ii. using instance method ``ui_shop_menu_display`` for display purposes
    """
        count_no_product_match=0 # cart shop iterations
        shopping_cart_invoice=0.0 # empty until add
        can_fill_full_order=1 # assume is true
        count_outer_customer=0 # check equal count_inner_shop
        count_inner_shop=0 # check equal count_outer_customer

        print(f'\n\n\nCUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: EUR{c.budget:.2f}') # display purposes only
        self.ui_shop_menu_display('-',13); print() # call instance method

        #
        # for each customer
        #
        for item in c.shopping_list: # original source code
            countShopIterations=0 # cart shop iterations
            count_no_product_match=0 # reset next customer

            self.print_product(item.product) # call instance method
            print(f'{c.name} ORDERS {item.quantity:.0f} OF ABOVE PRODUCT') # original source code
            self.ui_shop_menu_display('-',13); print() # call instance method

            #
            # iterate all stock
            #
            for shop_item in s.stock: # update stop state
                cost=item.quantity*shop_item.product.price # product full cost
                countShopIterations+=1 # latter compare count_no_product_match 

                if item.product.name==shop_item.product.name: # shop stocks product
                    print(f'The cost to {c.name} will be EUR{cost:.2f}') # original source code
                    self.ui_shop_menu_display('-',13); print() # call instance method
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
                    self.ui_shop_menu_display('-',13); print() # display purposes only
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
                    self.ui_shop_menu_display('-',13); print() # display purposes only
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
                self.ui_shop_menu_display('-',13); print() # display purposes only

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

        self.cash+=shopping_cart_invoice # cash shop state

    def shop_menu(self):
        """Process user choice.
    """
        while True: # infinite until False
            try: # handle runtime exceptions
                user=int(input()) # user input integer
                if user<0 or user>len(self.shop_menu_choice)-1: # range interval [0,4)
                    raise self.ShopMenuChoiceError('COMMENT: allowable input [0,3]') # outside choice range
            except (ValueError, # check for characters
                self.ShopMenuChoiceError, # custom exception created 
                EOFError, # input EOF Ctrl-Z
                KeyboardInterrupt): # terminate Ctrl-C etc
                self.shop_menu_display_header('Invalid Choice!!!!'); print() # call instance method
                self.shop_menu_display() # call instance method
            else:

                if user==self.shop_menu_choice.quit: # user input 0
                    self.shop_menu_display_header('\tBye!'); print() # call instance method
                    exit() # terminate the program
                if user==self.shop_menu_choice.shop_inventory: # user input 1
                    self.shop_menu_display_header('1 - Shop Inventory'); print() # call instance method
                    self.print_shop(self) # call instance method
                    self.shop_menu_display_footer() # call instance method
                if user==self.shop_menu_choice.read_orders: # user input 2
                    self.shop_menu_display_header('2 -  Read Orders'); print() # display purposes only
                    print(f'(Valid Input: Name - excluding \'.csv\')  >>> ',end="") # CSV name only
                    csv_file=str(input()).lower()+'.csv' # CSV excluding '../'

                    # ***behaviour sequence pattern***
                    customer_instance=Customer(path=csv_file) # instantiate object Customer
                    # ################################
                    
                    if customer_instance.name!="" and customer_instance.budget!=0: # customer has money
                        self.print_customer_update_shop_state(customer_instance,self) # call instance method
                    self.shop_menu_display_footer() # call instance method
                if user==self.shop_menu_choice.live_mode: # user input 3
                    self.shop_menu_display_header('  Shop Inventory'); print() # display purposes only
                    self.print_shop(self) # call instance method

                    # ***behaviour sequence pattern***
                    live_instance=Live() # instantiate object Live
                    # ################################

                    system('clear') # clear screen output
                    self.print_customer_update_shop_state(live_instance,self) # call instance method             
                    self.shop_menu_display_footer() # call instance method
    # --- END (instance methods) ---

    #
    # object string representation
    #
    def __repr__(self): # overriding method repr
        str="" # create a string
        str+=f'Shop has {self.cash} in cash\n' # append to str
        for item in self.stock: # iterate product stock
            str+=f"[item]\n" # everything in shop
        return str # object printable string
    # --- END (string representation) ---

# ------------------------------------------------    
# --------------- END (class Shop) ---------------
# ------------------------------------------------

# 
# define class Live
#
class Live(Shop): # child parent ``Shop``

    #
    # class attributes all
    #
    class ReplicateShopDotCError(ValueError): pass # allow newline character
    class live_menu_choice(IntEnum): # set integer values
        quit=0 # False then exit
        add_product_to_cart=1 # shop option 1    
    # --- END (class attributes) ---

    #
    # instance attributes initialiser
    #
    def __init__(self): # default Live state
        """Initialise (specify) object initial attributes:
         i. name (live customer name);
        ii. budget (live customer budget).
    """
        self.shop_menu_live_display_header() # call instance method

        self.shopping_list=[] # assign instance attribute

        print(f'(Valid Input: Customer Name)            >>> ',end="") # display purposes only
        while True: # infinite until False
            try: # handle runtime exceptions
                self.name=str(input()) # assign instance attribute
                if self.name=='': # check no input
                    raise self.ReplicateShopDotCError('COMMENT: allow newline character') # replicate shop.c behaviour
            except (ValueError, # check for string
                self.ReplicateShopDotCError): # custom exception created
                print(end="") # shop.c allows newline
            else:
                self.name=self.name.capitalize() # assign instance attribute               
                break # nothing to do

        print(f'(Valid Input: Customer Budget)          >>> EUR',end="") # display purposes only
        while True: # infinite until False
            try: # handle runtime exceptions
                self.budget=float(input()) # assign instance attribute
                while self.budget<=0: # error check budget
                    print(f'(Valid Input: Customer Budget)          >>> EUR',end="") # display purposes only
                    self.budget=float(input()) # assign instance attribute
            except ValueError: # check for float
                print(end="") # shop.c allows newline
            else:
                self.budget # user budget state
                break

        self.shop_menu_live_display_header() # call instance method
        self.shop_menu_live_display() # call instance method

        self.create_live_mode_checkout() # call instance method
    # --- END (instance attributes) ---

    #
    # class instance methods
    #
    def shop_menu_live_display_header(self):
        """Display purposes only.
        From inherited parent class ``Shop`` using:
        i. class Shop instance method ``ui_shop_menu_display``.
    """   
        self.ui_shop_menu_display('\n',3) # call instance method
        self.ui_shop_menu_display(' ',16); self.ui_shop_menu_display('-',18) # call instance method
        self.ui_shop_menu_display('\n',4) # call instance method

    def shop_menu_live_display(self):
        """Display purposes only.
        From inherited parent class ``Shop`` using:
         i. class Shop instance method ``ui_shop_menu_display``;
        ii. class Shop class attribute ``MAX_CHARACTERS``.
    """
        self.ui_shop_menu_display('+',self.MAX_CHARACTERS) # call instance method
        print(f'\n\t\t---- LIVE MODE----')
        print(f'\t\t1 -  Add to Cart')
        print(f'\t\t0 -     Exit')
        self.ui_shop_menu_display('+',self.MAX_CHARACTERS) # call instance method
        print(f'\n(Valid Input: 0 or 1)\t\t\t>>> ',end='')

    def create_live_mode_checkout(self):
        """Live mode menu.
        Using class Shop class attribute ``ShopMenuChoiceError``.
    """
        while True: # infinite until False        

            try: # handle runtime exceptions
                user=str(input()) # user input integer
                if user=='': # check no input
                    raise self.ReplicateShopDotCError('COMMENT: allow newline character') # replicate shop.c behaviour
            except (ValueError, # check for characters
                self.ReplicateShopDotCError): # custom exception created
                print(end="") # shop.c allows newline
            else:
                pass

            try:
                user=int(user) # correct format integer
                if user<0 or user>len(self.live_menu_choice)-1: # range interval [0,2)
                    raise self.ShopMenuChoiceError('COMMENT: allowable input [0,1]') # outside choice range
            except (ValueError, # check for characters
                self.ShopMenuChoiceError): # custom exception created 
                print(end="") # shop.c allows newline
            else:

                if user==self.live_menu_choice.quit: # user input 0
                    break # back to shop
                elif user==self.live_menu_choice.add_product_to_cart: # user input 1
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

                    product=Product(p_name,p_price) # populate class Product
                    customer_item=ProductStock(product,quantity) # populate class ProductStock

                    self.shopping_list.append(customer_item) # ready for checkout
                    
                    self.shop_menu_live_display() # call instance method
    # --- END (instance methods) ---

# ------------------------------------------------
# --------------- END (class Live) ---------------
# ------------------------------------------------
# ------------------------------------------------

if __name__=='__main__': # __name__ current module
    shop_instance=Shop(path="../stock.csv") # instantiate object Shop