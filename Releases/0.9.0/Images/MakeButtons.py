from PIL import Image
import os

def add_logo(background, foreground):
    background.paste(foreground, (11, 11))
    


for filename in os.listdir("Logos"):
    bg = Image.open('Button.png')
    fg = Image.open(f"Logos/{filename}").resize((30,30))
    out = add_logo(bg,fg)
    
    bg.save(f'Buttons/{filename[0:-4]}_button.png')