"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item]+=1
        else:
            current_cart.setdefault(item,1)
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    notes_dict = {}
    for item in notes:
        notes_dict.setdefault(item,1)
    return notes_dict
    


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    new_dict = {}
    for item in recipe_updates:
        new_dict[item[0]]= item[1]
            
    ideas.update(new_dict)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    new_dict = dict(sorted(cart.items()))
    return new_dict


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = {}
    for item, quantity in cart.items():
        aisle, refrigerated = aisle_mapping[item]
        fulfillment[item] = [quantity, aisle, refrigerated]
    
    # Trier en ordre alphabétique INVERSÉ (reverse=True)
    return dict(sorted(fulfillment.items(), reverse=True))
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, fulfillment_info in fulfillment_cart.items():
        quantity_ordered = fulfillment_info[0]  # Quantité commandée
        
        if item in store_inventory:
            current_stock = store_inventory[item][0]  # Stock actuel
            
            # Si la commande dépasse ou égale le stock, mettre "Out of Stock"
            if quantity_ordered >= current_stock:
                store_inventory[item][0] = 'Out of Stock'
            else:
                # Sinon, soustraire la quantité commandée
                store_inventory[item][0] -= quantity_ordered
    
    return store_inventory
    
