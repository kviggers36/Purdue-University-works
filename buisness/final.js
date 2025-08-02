function showFood(category) {
    const foodItems = document.getElementById('food-items');
    const foodItemsSection = document.getElementById('food-items');
    foodItemsSection.style.fontSize = '20px';
    foodItems.innerHTML = '';


    let items;
    switch (category) {
        case 'starters':
            items = ['Mozzarella Sticks: (5) 7.00 / (10) 13.00', 'French Fries: Regular 3.00 / Large 5.00', 'Nachos: Regular 3.00 / Loaded 7.00'];
            break;
        case 'pizza':
            items = ['Personal 7in Pizza: cheese 7.00 / One Topping 9.00 / Two Toppings 11.00', 'Family 16in Pizza: cheese 18.00 / One Topping 21.00 / Two Toppings 25.00', 'TOPPINGS: Pepperoni, Sausage, Bacon, Red Onions, Green Peppers, Olives, Black Olives, Banana Peppers, Mushrooms, Tomatoes, Jalapenos'];
            break;
        case 'wings':
            items = ['Boneless Wings: (10) 11.00 / (15) 16.00', 'Traditional Wings: (6) 9.00 / (12) 16.00', 'SAUCES: BBQ, Buffalo, Honey Garlic, Sweet Chili, Garlic Parmesan, Mango Habanero, / RUBS: BBQ, Lemon Pepper', 'Ranch or Blue Cheese: 1.00'];
            break;
        case 'burgers':
            items = ['Cheeseburger: 10.00', 'Veggie Burger: 12.00', 'Comes with fries and drink: 3.00', 'Toppings: Lettuce, Tomatos, Pickles, Onion (raw or caramelized), Cheese: Cheddar, Swiss, American, Pepper Jack, Bacon'];
            break;
        case 'drinks':
            items = ['Coke', 'Sprite', 'Dr.Pepper', 'Water', 'Lemonade', 'Sweet and Unsweetend Tea','Small 16oz: 3.00 / Medium 20oz: 5.00 / Large 32oz: 7.00'];
            break;
        default:
            items = [];
    }

    

    items.forEach(item => {
        const foodItem = document.createElement('p');
        foodItem.textContent = item;
        foodItems.appendChild(foodItem);
    });
}
