import tkinter as tk
from tkinter import ttk
from diceroller import d
from typing import Dict, List

class DiceRollerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        
        # Dictionary to store variables for each die type
        self.dice_vars: Dict[int, Dict] = {}
        
        # Create dice rows
        dice_types = [4, 6, 8, 10, 12, 20, 100]
        for die in dice_types:
            self.create_dice_row(die)
        
        # Create Roll button
        self.roll_button = ttk.Button(root, text="ROLL", command=self.roll_dice)
        self.roll_button.pack(pady=10)
        
        # Create separator
        ttk.Separator(root, orient='horizontal').pack(fill='x', pady=5)
        
        # Create results text field
        self.results_text = tk.Text(root, height=10, width=40)
        self.results_text.pack(pady=5, padx=10)

    def create_dice_row(self, sides: int):
        # Create frame for each row
        frame = ttk.Frame(self.root)
        frame.pack(fill='x', padx=10, pady=2)
        
        # Create variables for this die type
        self.dice_vars[sides] = {
            'enabled': tk.BooleanVar(value=False),
            'count': tk.StringVar(value="1"),
            'modifier': tk.StringVar(value="0")
        }
        
        # Create checkbox
        check = ttk.Checkbutton(frame, variable=self.dice_vars[sides]['enabled'])
        check.pack(side='left')
        
        # Create count entry
        count_entry = ttk.Entry(frame, width=3, textvariable=self.dice_vars[sides]['count'])
        count_entry.pack(side='left', padx=2)
        
        # Create die label
        label = ttk.Label(frame, text=f"d{sides}")
        label.pack(side='left')
        
        # Create plus label
        plus_label = ttk.Label(frame, text="+")
        plus_label.pack(side='left', padx=2)
        
        # Create modifier entry
        mod_entry = ttk.Entry(frame, width=3, textvariable=self.dice_vars[sides]['modifier'])
        mod_entry.pack(side='left')

    def roll_dice(self):
        self.results_text.delete(1.0, tk.END)
        results = []
        
        for sides, vars_dict in self.dice_vars.items():
            if vars_dict['enabled'].get():
                try:
                    count = int(vars_dict['count'].get())
                    modifier = int(vars_dict['modifier'].get())
                    
                    roll_results = d(sides, modifier, count)
                    results.append(f"\nd{sides} results:")
                    
                    for result in roll_results:
                        if result["modifier"] != 0:
                            results.append(f"{result['roll']} + {result['modifier']} = {result['total']}")
                        else:
                            results.append(str(result['roll']))
                            
                except ValueError:
                    results.append(f"\nError with d{sides}: Invalid number entered")
        
        if not results:
            self.results_text.insert(tk.END, "No dice selected!")
        else:
            self.results_text.insert(tk.END, "\n".join(results))

def main():
    root = tk.Tk()
    app = DiceRollerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
