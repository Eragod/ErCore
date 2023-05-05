colors = {
    'Foreground': {
        'Black': '\033[30m',
        'Red': '\033[31m',
        'Green': '\033[32m',
        'Yellow': '\033[33m',
        'Blue': '\033[34m',
        'Magenta': '\033[35m',
        'Cyan': '\033[36m',
        'White': '\033[37m'},
    'Background': {
        'Black': '\033[40m',
        'Red': '\033[41m',
        'Green': '\033[42m',
        'Yellow': '\033[43m',
        'Blue': '\033[44m',
        'Magenta': '\033[45m',
        'Cyan': '\033[46m',
        'White': '\033[47m'}
}
text_format = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'DIM': '\033[2m',
    'ITALIC': '\033[3m',
    'UNDERLINE': '\033[4m',
    'BLINK': '\033[5m',
    'RAPID B': '\033[6m',
    'INVERT C': '\033[7m',
    'HIDDEN': '\033[8m',
    'STRIKETHROUGH': '\033[9m',
}
f = colors.get('Foreground')
f_black = f.get('Black')
f_red = f.get('Red')
f_green = f.get('Green')
f_yellow = f.get('Yellow')
f_blue = f.get('Blue')
f_magenta = f.get('Magenta')
f_cyan = f.get('Cyan')
f_white = f.get('White')
b = colors.get('Background')
b_black = b.get('Black')
b_red = b.get('Red')
b_green = b.get('Green')
b_yellow = b.get('Yellow')
b_blue = b.get('Blue')
b_magenta = b.get('Magenta')
b_cyan = b.get('Cyan')
b_white = b.get('White')
reset = text_format.get('RESET')
bold = text_format.get('BOLD')
dim = text_format.get('DIM')
italic = text_format.get('ITALIC')
underline = text_format.get('UNDERLINE')
blink = text_format.get('BLINK')
rapid_b = text_format.get('RAPID B')
invert_c = text_format.get('INVERT C')
hidden = text_format.get('HIDDEN')
strikethrough = text_format.get('STRIKETHROUGH')
