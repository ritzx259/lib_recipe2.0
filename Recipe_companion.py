import tkinter as tk
from tkinter import ttk, font
import random
import matplotlib

# Set the backend before importing pyplot
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CulinaryCompanionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Culinary Companion")
        self.root.geometry("700x700")
        self.root.configure(bg="#f9f7f7")

        # Set up fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.subtitle_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=10)
        self.desc_font = font.Font(family="Helvetica", size=10, slant="italic")

        # Define colors
        self.primary_color = "#ff6b6b"
        self.secondary_color = "#4ecdc4"
        self.accent_color = "#ffe66d"
        self.text_color = "#2d3436"
        self.protein_color = "#6c5ce7"
        self.carbs_color = "#fdcb6e"
        self.fat_color = "#e17055"

        # Current meal type
        self.current_meal_type = None

        # Meal database
        self.initialize_meal_database()

        # Create UI
        self.create_header()
        self.create_meal_selector()
        self.create_meal_result()
        self.create_footer()

        # Initially hide the result frame
        self.result_frame.pack_forget()

    def initialize_meal_database(self):
        """Initialize the meal database with comprehensive nutrition information"""
        self.meals = {
            "breakfast": [
                {
                    "name": "Fluffy Pancakes",
                    "description": "Stack of fluffy buttermilk pancakes topped with maple syrup and butter",
                    "calories": 520,
                    "protein": 11,
                    "carbs": 92,
                    "fat": 14
                },
                {
                    "name": "Avocado Toast with Poached Eggs",
                    "description": "Whole grain toast topped with mashed avocado, poached eggs, and red pepper flakes",
                    "calories": 380,
                    "protein": 19,
                    "carbs": 35,
                    "fat": 22
                },
                {
                    "name": "Greek Yogurt with Honey and Berries",
                    "description": "Creamy Greek yogurt drizzled with honey and topped with fresh mixed berries",
                    "calories": 240,
                    "protein": 18,
                    "carbs": 32,
                    "fat": 5
                },
                {
                    "name": "Breakfast Burrito",
                    "description": "Flour tortilla filled with scrambled eggs, black beans, cheese, and salsa",
                    "calories": 450,
                    "protein": 24,
                    "carbs": 45,
                    "fat": 22
                },
                {
                    "name": "Oatmeal with Bananas and Cinnamon",
                    "description": "Steel-cut oats topped with sliced banana, cinnamon, and a drizzle of honey",
                    "calories": 310,
                    "protein": 10,
                    "carbs": 58,
                    "fat": 5
                },
                {
                    "name": "Spinach and Feta Omelette",
                    "description": "Three-egg omelette filled with sautéed spinach and crumbled feta cheese",
                    "calories": 280,
                    "protein": 22,
                    "carbs": 4,
                    "fat": 19
                },
                {
                    "name": "French Toast with Maple Syrup",
                    "description": "Thick-cut bread dipped in egg mixture, pan-fried, and topped with maple syrup",
                    "calories": 420,
                    "protein": 12,
                    "carbs": 65,
                    "fat": 16
                },
                {
                    "name": "Smoothie Bowl with Granola",
                    "description": "Blended frozen fruits topped with granola, coconut flakes, and sliced banana",
                    "calories": 350,
                    "protein": 8,
                    "carbs": 72,
                    "fat": 7
                },
                {
                    "name": "Eggs Benedict",
                    "description": "English muffin topped with Canadian bacon, poached eggs, and hollandaise sauce",
                    "calories": 650,
                    "protein": 32,
                    "carbs": 33,
                    "fat": 42
                },
                {
                    "name": "Breakfast Sandwich with Bacon",
                    "description": "Toasted bagel with fried egg, bacon, cheese, and avocado",
                    "calories": 480,
                    "protein": 25,
                    "carbs": 40,
                    "fat": 28
                }
            ],
            "lunch": [
                {
                    "name": "Chicken Caesar Salad",
                    "description": "Romaine lettuce with grilled chicken, parmesan cheese, croutons, and Caesar dressing",
                    "calories": 380,
                    "protein": 35,
                    "carbs": 12,
                    "fat": 22
                },
                {
                    "name": "Turkey and Avocado Wrap",
                    "description": "Whole wheat wrap filled with turkey breast, avocado, lettuce, and tomato",
                    "calories": 410,
                    "protein": 28,
                    "carbs": 38,
                    "fat": 18
                },
                {
                    "name": "Quinoa Bowl with Roasted Vegetables",
                    "description": "Quinoa topped with roasted vegetables, chickpeas, and tahini dressing",
                    "calories": 320,
                    "protein": 12,
                    "carbs": 45,
                    "fat": 13
                },
                {
                    "name": "Caprese Panini",
                    "description": "Grilled sandwich with fresh mozzarella, tomatoes, basil, and balsamic glaze",
                    "calories": 450,
                    "protein": 18,
                    "carbs": 48,
                    "fat": 24
                },
                {
                    "name": "Lentil Soup with Crusty Bread",
                    "description": "Hearty lentil soup with vegetables, served with a slice of crusty bread",
                    "calories": 380,
                    "protein": 16,
                    "carbs": 58,
                    "fat": 8
                },
                {
                    "name": "Tuna Salad Sandwich",
                    "description": "Whole grain bread with tuna salad, lettuce, and cucumber",
                    "calories": 420,
                    "protein": 30,
                    "carbs": 42,
                    "fat": 15
                },
                {
                    "name": "Falafel Pita with Tzatziki",
                    "description": "Pita bread filled with crispy falafel, vegetables, and tzatziki sauce",
                    "calories": 490,
                    "protein": 16,
                    "carbs": 65,
                    "fat": 18
                },
                {
                    "name": "Asian Noodle Salad",
                    "description": "Rice noodles with edamame, vegetables, and sesame-ginger dressing",
                    "calories": 390,
                    "protein": 14,
                    "carbs": 62,
                    "fat": 12
                },
                {
                    "name": "Grilled Chicken Sandwich",
                    "description": "Grilled chicken breast with lettuce, tomato, and herb aioli on a ciabatta roll",
                    "calories": 520,
                    "protein": 38,
                    "carbs": 48,
                    "fat": 22
                },
                {
                    "name": "Mediterranean Hummus Plate",
                    "description": "Hummus with olives, feta cheese, vegetables, and pita bread",
                    "calories": 340,
                    "protein": 14,
                    "carbs": 38,
                    "fat": 16
                }
            ],
            "dinner": [
                {
                    "name": "Grilled Salmon with Asparagus",
                    "description": "Grilled salmon fillet with roasted asparagus and lemon butter sauce",
                    "calories": 420,
                    "protein": 38,
                    "carbs": 10,
                    "fat": 24
                },
                {
                    "name": "Spaghetti Bolognese",
                    "description": "Spaghetti pasta topped with rich meat sauce and parmesan cheese",
                    "calories": 580,
                    "protein": 25,
                    "carbs": 72,
                    "fat": 23
                },
                {
                    "name": "Vegetable Stir Fry with Tofu",
                    "description": "Crispy tofu with stir-fried vegetables in a ginger-soy sauce",
                    "calories": 340,
                    "protein": 18,
                    "carbs": 40,
                    "fat": 12
                },
                {
                    "name": "Roast Chicken with Potatoes",
                    "description": "Herb-roasted chicken with golden roasted potatoes and gravy",
                    "calories": 650,
                    "protein": 42,
                    "carbs": 45,
                    "fat": 32
                },
                {
                    "name": "Beef Tacos",
                    "description": "Corn tortillas filled with seasoned ground beef, lettuce, cheese, and salsa",
                    "calories": 510,
                    "protein": 28,
                    "carbs": 42,
                    "fat": 28
                },
                {
                    "name": "Eggplant Parmesan",
                    "description": "Breaded eggplant slices baked with marinara sauce and mozzarella cheese",
                    "calories": 460,
                    "protein": 18,
                    "carbs": 48,
                    "fat": 22
                },
                {
                    "name": "Shrimp Scampi",
                    "description": "Sautéed shrimp in garlic butter sauce served over linguine pasta",
                    "calories": 390,
                    "protein": 30,
                    "carbs": 38,
                    "fat": 16
                },
                {
                    "name": "Mushroom Risotto",
                    "description": "Creamy arborio rice with sautéed mushrooms and parmesan cheese",
                    "calories": 430,
                    "protein": 12,
                    "carbs": 65,
                    "fat": 18
                },
                {
                    "name": "Beef Burger with Sweet Potato Fries",
                    "description": "Grilled beef patty on a brioche bun with toppings and sweet potato fries",
                    "calories": 720,
                    "protein": 38,
                    "carbs": 62,
                    "fat": 40
                },
                {
                    "name": "Thai Green Curry with Rice",
                    "description": "Spicy coconut curry with vegetables and jasmine rice",
                    "calories": 520,
                    "protein": 18,
                    "carbs": 58,
                    "fat": 26
                }
            ]
        }

    def create_header(self):
        """Create the header section of the application"""
        header_frame = tk.Frame(self.root, bg=self.primary_color, pady=20)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Culinary Companion",
            font=self.title_font,
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text="Choose a meal type to get a suggestion with nutrition information",
            font=self.normal_font,
            bg=self.primary_color,
            fg="white"
        )
        subtitle_label.pack(pady=(5, 0))

    def create_meal_selector(self):
        """Create the meal selector section"""
        self.selector_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        self.selector_frame.pack(fill=tk.X, padx=20, pady=20)

        # Add some elevation effect with a border
        self.selector_frame.config(highlightbackground="#ddd", highlightthickness=1)

        selector_title = tk.Label(
            self.selector_frame,
            text="What would you like to eat?",
            font=self.subtitle_font,
            fg=self.primary_color,
            bg="white"
        )
        selector_title.pack(pady=(0, 15))

        # Button frame for the meal type selection
        button_frame = tk.Frame(self.selector_frame, bg="white")
        button_frame.pack()

        # Create meal type buttons
        meal_types = ["breakfast", "lunch", "dinner"]

        for meal_type in meal_types:
            meal_button = tk.Button(
                button_frame,
                text=meal_type.capitalize(),
                bg=self.secondary_color,
                fg="white",
                font=self.normal_font,
                padx=15,
                pady=8,
                borderwidth=0,
                command=lambda mt=meal_type: self.show_random_meal(mt)
            )
            meal_button.pack(side=tk.LEFT, padx=5)

            # Add hover effect
            meal_button.bind("<Enter>", lambda e, btn=meal_button: btn.config(bg="#3db9b2"))
            meal_button.bind("<Leave>", lambda e, btn=meal_button: btn.config(bg=self.secondary_color))

    def create_meal_result(self):
        """Create the meal result section"""
        self.result_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)

        # Add some elevation effect with a border
        self.result_frame.config(highlightbackground="#ddd", highlightthickness=1)

        # Meal information
        self.meal_name_label = tk.Label(
            self.result_frame,
            text="Meal Name",
            font=self.title_font,
            fg=self.primary_color,
            bg="white"
        )
        self.meal_name_label.pack(pady=(0, 10))

        self.meal_desc_label = tk.Label(
            self.result_frame,
            text="Meal description goes here",
            font=self.desc_font,
            fg="#666",
            bg="white",
            wraplength=500
        )
        self.meal_desc_label.pack(pady=(0, 15))

        # Nutrition info frame
        nutrition_frame = tk.Frame(self.result_frame, bg="white")
        nutrition_frame.pack(pady=10)

        # Calories badge
        self.calories_badge = tk.Label(
            nutrition_frame,
            text="Calories: 0",
            bg=self.accent_color,
            fg=self.text_color,
            font=self.normal_font,
            padx=15,
            pady=5,
            relief="flat"
        )
        self.calories_badge.pack(side=tk.LEFT, padx=5)

        # Protein badge
        self.protein_badge = tk.Label(
            nutrition_frame,
            text="Protein: 0g",
            bg=self.protein_color,
            fg="white",
            font=self.normal_font,
            padx=15,
            pady=5,
            relief="flat"
        )
        self.protein_badge.pack(side=tk.LEFT, padx=5)

        # Carbs badge
        self.carbs_badge = tk.Label(
            nutrition_frame,
            text="Carbs: 0g",
            bg=self.carbs_color,
            fg=self.text_color,
            font=self.normal_font,
            padx=15,
            pady=5,
            relief="flat"
        )
        self.carbs_badge.pack(side=tk.LEFT, padx=5)

        # Fat badge
        self.fat_badge = tk.Label(
            nutrition_frame,
            text="Fat: 0g",
            bg=self.fat_color,
            fg="white",
            font=self.normal_font,
            padx=15,
            pady=5,
            relief="flat"
        )
        self.fat_badge.pack(side=tk.LEFT, padx=5)

        # Matplotlib figure for nutrition chart
        self.fig, self.ax = plt.subplots(figsize=(6, 2))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.result_frame)
        self.canvas.get_tk_widget().pack(pady=15)

        # Try again button
        self.try_again_button = tk.Button(
            self.result_frame,
            text="Try Another Meal",
            bg=self.primary_color,
            fg="white",
            font=self.normal_font,
            padx=15,
            pady=8,
            borderwidth=0,
            command=self.get_another_meal
        )
        self.try_again_button.pack(pady=10)

        # Add hover effect
        self.try_again_button.bind("<Enter>", lambda e: self.try_again_button.config(bg="#ff5252"))
        self.try_again_button.bind("<Leave>", lambda e: self.try_again_button.config(bg=self.primary_color))

    def create_footer(self):
        """Create the footer section"""
        footer_frame = tk.Frame(self.root, bg=self.text_color, pady=10)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        footer_label = tk.Label(
            footer_frame,
            text="© 2025 Culinary Companion - Nutrition Tracker",
            font=self.normal_font,
            bg=self.text_color,
            fg="white"
        )
        footer_label.pack()

    def get_random_meal(self, meal_type):
        """Get a random meal based on the selected type"""
        meal_list = self.meals[meal_type]
        return random.choice(meal_list)

    def update_nutrition_chart(self, protein, carbs, fat):
        """Update the nutrition chart with the meal's macronutrients"""
        # Clear the previous chart
        self.ax.clear()

        # Data for the pie chart
        labels = ['Protein', 'Carbs', 'Fat']
        sizes = [protein, carbs, fat]
        colors = [self.protein_color, self.carbs_color, self.fat_color]

        # Create pie chart
        self.ax.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'white'}
        )
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        self.ax.set_title('Macronutrient Distribution')

        # Update the canvas
        self.canvas.draw()

    def show_random_meal(self, meal_type):
        """Display a random meal of the selected type"""
        self.current_meal_type = meal_type
        meal = self.get_random_meal(meal_type)

        # Update the meal information
        self.meal_name_label.config(text=meal["name"])
        self.meal_desc_label.config(text=meal["description"])
        self.calories_badge.config(text=f"Calories: {meal['calories']}")
        self.protein_badge.config(text=f"Protein: {meal['protein']}g")
        self.carbs_badge.config(text=f"Carbs: {meal['carbs']}g")
        self.fat_badge.config(text=f"Fat: {meal['fat']}g")

        # Update the nutrition chart
        self.update_nutrition_chart(meal["protein"], meal["carbs"], meal["fat"])

        # Show the result frame
        self.result_frame.pack(fill=tk.X, padx=20, pady=20)

    def get_another_meal(self):
        """Get another random meal of the current type"""
        if self.current_meal_type:
            self.show_random_meal(self.current_meal_type)


def main():
    root = tk.Tk()
    app = CulinaryCompanionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()