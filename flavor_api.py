from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Flavor logic
score_map = {
    'Relaxed': 'Sweet',
    'Adventurous': 'Spicy',
    'Focused': 'Umami',
    'Playful': 'Tangy',
    'Grounded': 'Savory'
}

flavor_profiles = {
    'Sweet': ['Honey', 'Vanilla', 'Cinnamon', 'Maple Syrup'],
    'Savory': ['Garlic', 'Thyme', 'Soy Sauce', 'Rosemary'],
    'Spicy': ['Chili', 'Black Pepper', 'Ginger', 'Wasabi'],
    'Umami': ['Miso', 'Parmesan', 'Mushroom', 'Anchovy'],
    'Tangy': ['Lemon', 'Tamarind', 'Vinegar', 'Yogurt']
}

@app.route('/generate', methods=['POST'])
def generate_flavor():
    data = request.get_json()
    mood = data.get('mood')
    personality = data.get('personality')

    mood_score = score_map.get(mood, 'Sweet')
    personality_score = score_map.get(personality, 'Savory')
    final_flavor = mood_score if mood_score == personality_score else random.choice([mood_score, personality_score])
    ingredients = random.sample(flavor_profiles[final_flavor], 2)

    return jsonify({
        'flavor': final_flavor,
        'ingredients': ingredients
    })

if __name__ == '__main__':
    app.run(debug=True)