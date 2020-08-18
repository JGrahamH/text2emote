import time

emoteDict = {
    "A": ":lemmaa:",
    "a": ":lemmaa:",
    "B": ":bbbb:",
    "b": ":bbbb:",
    "C": ":_C_:",
    "c": ":_C_:",
    "D": ":TheD:",
    "d": ":TheD:",
    "E": ":lemmae:",
    "e": ":lemmae:",
    "F": ":ai_fuel:",
    "f": ":ai_fuel:",
    "G": ":boldg:",
    "g": ":boldg:",
    "H": ":htpts:",
    "h": ":htpts:",
    "I": ":fbimania_i:",
    "i": ":fbimania_i:",
    "J": ":_J_:",
    "j": ":_J_:",
    "K": ":_K_:",
    "k": ":_K_:",
    "L": ":lemmal:",
    "l": ":lemmal:",
    "M": ":lemmam:",
    "m": ":lemmam:",
    "N": ":NN:",
    "n": ":NN:",
    "O": ":oooo:",
    "o": ":oooo:",
    "P": ":P:",
    "p": ":P:",
    "Q": ":_Q_:",
    "q": ":_Q_:",
    "R": ":FreebieR:",
    "r": ":FreebieR:",
    "S": ":sgsurvivor:",
    "s": ":sgsurvivor:",
    "T": ":_T_:",
    "t": ":_T_:",
    "U": ":qube2magnet:",
    "u": ":qube2magnet:",
    "V": ":_V_:",
    "v": ":_V_:",
    "W": ":_W_:",
    "w": ":_W_:",
    "X": ":TryAgain:",
    "x": ":TryAgain:",
    "Y": ":Y:",
    "y": ":Y:",
    "Z": ":Z:",
    "z": ":Z:",
    " ": " "
}

print("Enter text to convert:")

text_input = input()

string = text_input

new_string = ""

new_string = ''.join(emoteDict[l] for l in string[::1])

print(new_string)

time.sleep(30)
