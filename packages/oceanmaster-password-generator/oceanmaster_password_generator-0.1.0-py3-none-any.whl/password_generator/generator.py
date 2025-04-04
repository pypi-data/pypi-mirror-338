# password_generator/generator.py

import random
import string
import re
from typing import Dict, List, Optional, Union

class PasswordGenerator:
    """An advanced password generator with multiple security features and customization options."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.similar_chars = "O0Il1|"  # Characters that look similar
        self.ambiguous_chars = "{}[]()/\\'\"`~,;:.<>"  # Characters that may cause issues in different contexts
        
    def generate_password(self, length: int = 12, difficulty: str = "medium", 
                          numbers: bool = True, alphabets: bool = True, 
                          special_chars: bool = False, exclude_similar: bool = False,
                          exclude_ambiguous: bool = False, 
                          min_counts: Optional[Dict[str, int]] = None) -> str:
        """
        Generate a password with customizable options.
        
        Args:
            length: Length of the password
            difficulty: Password complexity level ("easy", "medium", "hard")
            numbers: Include numeric characters
            alphabets: Include alphabetic characters
            special_chars: Include special characters
            exclude_similar: Exclude similar-looking characters
            exclude_ambiguous: Exclude ambiguous characters
            min_counts: Dictionary specifying minimum counts for each character type
            
        Returns:
            A generated password string
        """
        if length < 1:
            return "Length must be at least 1"
            
        # Build character pool based on selected options
        char_pool = ""
        
        if alphabets:
            if difficulty.lower() == "easy":
                char_pool += self.lowercase
            elif difficulty.lower() == "medium":
                char_pool += self.lowercase + self.uppercase
            elif difficulty.lower() == "hard":
                char_pool += self.lowercase + self.uppercase
        
        if numbers and difficulty.lower() != "easy":
            char_pool += self.digits
            
        if special_chars and difficulty.lower() == "hard":
            char_pool += self.special_chars
            
        # Apply exclusion filters
        if exclude_similar:
            char_pool = ''.join(c for c in char_pool if c not in self.similar_chars)
            
        if exclude_ambiguous:
            char_pool = ''.join(c for c in char_pool if c not in self.ambiguous_chars)
            
        if not char_pool:
            return "Please select at least one character type"
            
        # Initialize password with required character types
        password = []
        
        # Handle minimum counts for each character type
        if min_counts:
            for char_type, count in min_counts.items():
                if char_type == "lowercase" and alphabets:
                    filtered_chars = self._filter_chars(self.lowercase, exclude_similar, exclude_ambiguous)
                    password.extend(random.choice(filtered_chars) for _ in range(count))
                elif char_type == "uppercase" and alphabets:
                    filtered_chars = self._filter_chars(self.uppercase, exclude_similar, exclude_ambiguous)
                    password.extend(random.choice(filtered_chars) for _ in range(count))
                elif char_type == "digits" and numbers:
                    filtered_chars = self._filter_chars(self.digits, exclude_similar, exclude_ambiguous)
                    password.extend(random.choice(filtered_chars) for _ in range(count))
                elif char_type == "special_chars" and special_chars:
                    filtered_chars = self._filter_chars(self.special_chars, exclude_similar, exclude_ambiguous)
                    password.extend(random.choice(filtered_chars) for _ in range(count))
        
        # Fill remaining characters
        remaining_length = length - len(password)
        if remaining_length > 0:
            password.extend(random.choice(char_pool) for _ in range(remaining_length))
            
        # Shuffle the password to ensure randomness
        random.shuffle(password)
        
        return "".join(password)
    
    def _filter_chars(self, chars: str, exclude_similar: bool, exclude_ambiguous: bool) -> str:
        """Filter characters based on exclusion criteria."""
        result = chars
        if exclude_similar:
            result = ''.join(c for c in result if c not in self.similar_chars)
        if exclude_ambiguous:
            result = ''.join(c for c in result if c not in self.ambiguous_chars)
        return result if result else chars  # Fallback to original if everything was filtered
    
    def generate_multiple_passwords(self, count: int = 5, **kwargs) -> List[str]:
        """Generate multiple passwords with the same settings."""
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def check_password_strength(self, password: str) -> str:
        """
        Evaluate the strength of a password.
        
        Returns:
            "Weak", "Medium", or "Strong"
        """
        # Initialize score
        score = 0
        
        # Length check
        if len(password) >= 12:
            score += 3
        elif len(password) >= 8:
            score += 2
        elif len(password) >= 6:
            score += 1
            
        # Character variety checks
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[^a-zA-Z0-9]', password):  # Special characters
            score += 2
            
        # Pattern checks (penalize)
        if re.search(r'(.)\1\1', password):  # Repeated characters
            score -= 1
        if re.search(r'(123|abc|qwerty|password)', password.lower()):  # Common patterns
            score -= 2
            
        # Determine strength based on score
        if score >= 7:
            return "Strong"
        elif score >= 4:
            return "Medium"
        else:
            return "Weak"
    
    def generate_passphrase(self, word_count: int = 4, separator: str = "-") -> str:
        """Generate a passphrase from random words."""
        # Simple word list (in a real implementation, use a larger dictionary)
        words = [
    "apple", "banana", "orange", "grape", "mango", "lemon", "kiwi", "peach", "plum", "cherry", "pineapple", "strawberry", "blueberry", "watermelon", "pear", 
    "coconut", "apricot", "fig", "date", "papaya", "nectarine", "melon", "lime", "tangerine", "pomegranate", "avocado", "cantaloupe", "jackfruit", "blackberry", 
    "house", "window", "door", "floor", "ceiling", "wall", "room", "garden", "kitchen", "livingroom", "bathroom", "bedroom", "corridor", "garage", "attic", 
    "balcony", "porch", "backyard", "stairs", "roof", "chimney", "furniture", "sofa", "chair", "table", "lamp", "mirror", "clock", "cupboard", "drawer", "shelf", 
    "computer", "keyboard", "mouse", "monitor", "printer", "phone", "tablet", "headphones", "television", "radio", "microwave", "toaster", "fridge", "dishwasher", 
    "vacuum", "oven", "stove", "fan", "heater", "airconditioner", "lights", "switch", "socket", "broom", "duster", "mop", "bucket", "towel", "toothbrush", "toothpaste", 
    "water", "river", "ocean", "lake", "mountain", "valley", "forest", "desert", "rain", "snow", "wind", "cloud", "storm", "thunder", "lightning", "fog", "earthquake", 
    "sun", "moon", "star", "planet", "comet", "galaxy", "universe", "space", "satellite", "telescope", "astrology", "meteor", "constellation", "sky", "clouds", 
    "rainbow", "dawn", "dusk", "night", "day", "seasons", "summer", "winter", "fall", "spring", "autumn", "leaves", "breeze", "waves", "shore", "beach", "coast", 
    "hill", "cliff", "rock", "sand", "soil", "earth", "waterfall", "riverbank", "pond", "stream", "pool", "island", "archipelago", "bay", "cave", "gorge", 
    "happy", "angry", "sad", "excited", "tired", "strong", "weak", "brave", "fearful", "hopeful", "grateful", "calm", "nervous", "worried", "joyful", "peaceful", 
    "cheerful", "confident", "determined", "stressed", "relaxed", "bored", "enthusiastic", "guilty", "ashamed", "proud", "confused", "surprised", "shocked", 
    "curious", "distracted", "ambitious", "motivated", "exhausted", "content", "delighted", "optimistic", "pessimistic", "satisfied", "dissatisfied", "grumpy", 
    "optimistic", "pessimistic", "focused", "exhilarated", "miserable", "joyous", "nervous", "indifferent", "melancholy", "delighted", "elated", "overwhelmed", 
    "hopeful", "lucky", "unlucky", "serene", "lively", "calm", "restless", "grumpy", "positive", "negative", "neutral", "hungry", "full", "thirsty", "sleepy", 
    "lazy", "creative", "intelligent", "clever", "friendly", "gracious", "thoughtful", "rude", "polite", "generous", "honest", "deceptive", "loyal", "distant", 
    "strong-willed", "kind", "compassionate", "selfish", "careful", "reckless", "wise", "inexperienced", "experienced", "sophisticated", "simple", "complex", 
    "authentic", "real", "fake", "distrustful", "loyal", "faithful", "shy", "outgoing", "noble", "gentle", "violent", "savage", "peaceful", "warm", "cold", 
    "frosty", "hot", "mild", "spicy", "sweet", "bitter", "sour", "salty", "tangy", "crunchy", "soft", "smooth", "rough", "sharp", "blunt", "soft", "hard", "sticky", 
    "tough", "bouncy", "flexible", "firm", "smooth", "silky", "coarse", "sandy", "gritty", "dusty", "fluffy", "fluffy", "waxy", "gravelly", "icy", "fuzzy", 
    "creamy", "sweet", "mild", "muggy", "sweltering", "temperate", "pleasant", "boiling", "chilly", "frigid", "scalding", "freezing", "wet", "dry", "humid", 
    "sunny", "overcast", "cloudy", "stormy", "rainy", "thunderstorm", "tornado", "blizzard", "heatwave", "flashflood", "snowstorm", "hurricane", "earthquake", 
    "volcano", "tsunami", "naturaldisaster", "fire", "explosion", "damage", "emergency", "dangerous", "safe", "survival", "rescue", "firstaid", "health", "hospital", 
    "doctor", "nurse", "medicine", "treatment", "surgery", "clinic", "healthcare", "wellness", "fitness", "exercise", "workout", "yoga", "meditation", "breathing", 
    "therapy", "mentalhealth", "psychology", "counseling", "rehabilitation", "mindfulness", "cognitive", "emotion", "selfcare", "diet", "nutrition", "meal", "grocery", 
    "cook", "recipe", "dish", "snack", "dessert", "delicacy", "spices", "herbs", "vegetable", "fruit", "meat", "chicken", "beef", "pork", "fish", "seafood", 
    "cereal", "grain", "bread", "cheese", "butter", "milk", "yogurt", "tea", "coffee", "soda", "juice", "water", "wine", "beer", "cocktail", "whiskey", "vodka", 
    "rum", "champagne", "whiskey", "brandy", "liquor", "alcohol", "lifestyle", "diet", "fitness", "healthy", "unhealthy"
]

        return separator.join(random.choice(words) for _ in range(word_count))
