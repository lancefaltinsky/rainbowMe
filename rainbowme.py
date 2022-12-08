import pyperclip as ppc
import argparse

# credits to this guide for teaching me ANSI somewhat https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06
def rainbowify(words, bg, style):
    text = ""
    cur_color = 31
    for c in words:
        if cur_color == 36:
            cur_color = 31
        else:
            cur_color += 1
        text = text + f'[{style};{bg};{cur_color}m{c}'
    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('text', type=str, nargs='*',
                    help='The text to rainbowify')

    parser.add_argument('-bg', '--background',
        choices = ['none', 'darkblue', 'orange', 'marbleblue', 'turquoise', 'gray', 'indigo', 'lightgray', 'white'],
        default = 'none',
        dest='background',
        help='Specify background color for the text',
        type = str
        )
    
    parser.add_argument('-style',
        choices = ['none', 'bold', 'underline'],
        default = 'none',
        dest='style',
        help='Specify a style for the text, i.e bold',
        type = str
    )
    
    colors = {
        'none': 0,
        'darkblue': 40, # actually "firefly dark blue", but we dont want to drive the user crazy
        'orange': 41,
        'marbleblue': 42,
        'turquoise': 43,
        'gray': 44,
        'indigo': 45,
        'lightgray': 46,
        'white': 47
    }

    styles = {
        'none': 0,
        'bold': 1,
        'underline': 4
    }

    args = parser.parse_args()
    output = rainbowify(' '.join(args.text), colors[args.background.lower()], styles[args.style.lower()])
    # we put a sequence here so your console doesnt look like shit after you use this tool lmao
    print(output, '[0;0;0m')
    ppc.copy(f'```ansi\n{output}\n```')
    print("Copied ANSI code to clipboard! Now paste it into a Discord message :)")
    if len(output) > 1000:
        print("WARNING: The output was greater than 1000 characters. The ANSI may not display in Discord at all. As a rule of thumb, try to keep the input text < 100 characters.")
    print("Coded by @lance#8011")