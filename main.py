import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

class CardSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Selector")
        self.champs = ['archer_queen', 'golden_knight', 'skeleton_king', 'mighty_miner', 'little_prince']
        self.deck_frame = ttk.Frame(root)
        self.deck_frame.pack(pady=10)
        self.select_cards_button = ttk.Button(root, text="Generate Deck", command=self.select_cards)
        self.select_cards_button.pack(pady=10)

    def select_cards(self):
        normal_cards = ['archers', 'arrows', 'balloon', 'bandit', 'barbarians', 'barbarian_barrel', 'barbarian_hut',
                        'bats', 'battle_healer', 'battle_ram', 'bomber', 'bomb_tower', 'bowler', 'cannon', 'cannon_cart',
                        'clone', 'dark_prince', 'dart_goblin', 'earthquake', 'electro_dragon', 'electro_giant',
                        'electro_spirit', 'electro_wizard', 'elite_barbarians', 'elixir_collector', 'elixir_golem',
                        'executioner', 'fireball', 'firecracker', 'fire_spirit', 'fisherman', 'flying_machine', 'freeze',
                        'furnace', 'giant', 'giant_skeleton', 'giant_snowball', 'goblins', 'goblin_barrel', 'goblin_cage',
                        'goblin_drill', 'goblin_gang', 'goblin_giant', 'goblin_hut', 'golden_knight', 'golem', 'graveyard',
                        'guards', 'heal_spirit', 'hog_rider', 'hungry_dragon', 'hunter', 'ice_golem', 'ice_spirit',
                        'ice_wizard', 'inferno_dragon', 'inferno_tower', 'knight', 'lava_hound', 'lightning', 'little_prince',
                        'lumberjack', 'magic_archer', 'mega_knight', 'mega_minion', 'mighty_miner', 'miner', 'minions',
                        'minion_horde', 'minipekka', 'mirror', 'monk', 'mortar', 'mother_witch', 'musketeer', 'night_witch',
                        'pekka', 'phoenix', 'poison', 'prince', 'princess', 'rage', 'ram_rider', 'rascals', 'rocket',
                        'royal_delivery', 'royal_ghost', 'royal_giant', 'royal_hogs', 'royal_recruits', 'skeletons',
                        'skeleton_army', 'skeleton_barrel', 'skeleton_dragons', 'skeleton_king', 'sparky', 'spear_goblins',
                        'tesla', 'the_log', 'three_musketeers', 'tombstone', 'tornado', 'valkyrie', 'wall_breakers', 'witch',
                        'wizard', 'x_bow', 'zap', 'zappies']
        selected = random.sample(normal_cards, 8)
        champ_count = sum(card in self.champs for card in selected)
        while champ_count > 1:
            champ_to_replace = random.choice(self.champs)
            if champ_to_replace in selected:
                replacement_card = random.choice(normal_cards)
                while replacement_card in self.champs:
                    replacement_card = random.choice(normal_cards)
                selected[selected.index(champ_to_replace)] = replacement_card
                champ_count = sum(card in self.champs for card in selected)
            else:
                champ_count = sum(card in self.champs for card in selected)
        self.display_cards(selected)

    def display_cards(self, cards):
        for widget in self.deck_frame.winfo_children():
            widget.destroy()
        for i, card in enumerate(cards):
            image_path = f'cards/{card}.png'
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img = img.resize((197, 251), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                label = ttk.Label(self.deck_frame, image=img, text=card, compound=tk.TOP)
                label.image = img
                row = i // 4
                label.grid(row=row, column=i % 4, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CardSelectorApp(root)
    root.mainloop()
