from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# 事件卡列表
event_cards = [
    # 天气卡
    "Clear Skies ☀️: Roll a die to determine a horizontal row; next turn, all players in that row reduce stamina consumption by 1 per space.",
    "Blizzard 🌨️: Roll a die to determine a horizontal row; next turn, every space in that row costs 1 extra stamina.",
    "Avalanche 🗻: Roll a die to determine a vertical column; all players in that column return to the previous camp.",
    # 随机事件卡
    "Lucky Draw: Roll dice. Highest gains a supply card, lowest moves back one space.",
    "Exhaustion: All players lose 2 stamina immediately.",
    "Support Drop: Last player gets 2 supply cards and gives one to the first player.",
    "Lost Gear: Player with the lowest dice roll loses a supply card.",
    "Universal Supply: All players immediately receive one supply card.",
    "Setback: All players move back two spaces.",
    "Disease Outbreak: All players receive one random disease card.",
    "Group Recovery: All players recover 2 stamina points."
]

# 补给卡列表
supply_cards = [
    "Tent 🏕️: Blocks the negative effect of one blizzard event.",
    "Rope 🧗‍♂️: Removes stamina consumption once in a climbing zone.",
    "Goggles 🕶️: Immune to negative events in glacier zones.",
    "Thermal Jacket 🧥: Immune to the effect of one disease card.",
    "Surveyor 🔍: Roll the die twice each turn, choose one result to move.",
    "GPS Locator 📍: Draw two random supply cards.",
    "Adrenaline 💉: Move 3 extra spaces this turn, each extra space costs 2 stamina.",
    "Firearm 🔫: Reduce another player’s 2 stamina and steal one supply card, but can only be used when you are on the same horizontal row.",
    "Helicopter 🚁: Fly directly to the nearest camp.",
    "Canned Food 🥫: Restore 1 stamina.",
    "First Aid Kit 🩹: Restore 2 stamina and remove one disease card."
]

# 疾病卡列表
disease_cards = [
    "Frostbite ❄️: Move slowly. Roll two dice next turn, pick the lower result.",
    "Altitude Sickness 🤢: Lose 1 stamina every turn until cured.",
    "Snow Blindness 👀: Stop moving next turn, but regain 1 stamina.",
    "High Altitude Pulmonary Edema 🫁: Lose 3 stamina immediately and return to the previous camp.",
    "Dehydration 💧: Cannot use any active item in the next turn.",
    "Sunburn ☀️: In the next turn, every space moved costs 1 extra stamina.",
    "Fatigue 😴: Cannot move more than 3 spaces in the next turn."
]

# 路由：返回 HTML 页面
@app.route('/')
def home():
    return render_template('index.html')

# 路由：抽取事件卡
@app.route('/draw-event-card')
def draw_event_card():
    card = random.choice(event_cards)
    return jsonify({"card": card})

# 路由：抽取补给卡
@app.route('/draw-supply-card')
def draw_supply_card():
    card = random.choice(supply_cards)
    return jsonify({"card": card})

# 路由：抽取疾病卡
@app.route('/draw-disease-card')
def draw_disease_card():
    card = random.choice(disease_cards)
    return jsonify({"card": card})

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
