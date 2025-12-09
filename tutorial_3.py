def checkout(inventory, cart):
    total_price=0
    failed_item_count=len(cart)
    for item in cart:
        try:
            price=inventory[item]
            if price==None:
                raise TypeError("Price missing")
            if price<0:
                raise ValueError("Invalid price")
            total_price+=price
            failed_item_count-=1
        except KeyError:
            print(f"Item not found: {item}")
        except TypeError as e:
            print(f"Data error for {item}: {e}")
        except ValueError as e:
            print(f"Data error for {item}: {e}")
    return (total_price, failed_item_count)

store_db = {
    "Apple": 0.50, 
    "Banana": 0.30, 
    "GhostItem": None,     # Corrupt data
    "GlitchItem": -5.00    # Corrupt data
}
my_cart = ["Apple", "Mango", "GhostItem", "Banana", "GlitchItem"]

cost, errors = checkout(store_db, my_cart)
print(f"Total: ${cost}, Errors: {errors}")
    
    

    
        
        
        
