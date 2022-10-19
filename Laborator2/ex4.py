# Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return
# the song composed by going through the musical notes beginning with the start position
# and following the moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# 	will return ["mi", "fa", "do", "sol", "re"]


def compose(n, m, s):
    song = [n[s]]
    for move in m:
        s = s + move
        if s not in range(0, len(n)):
            while s not in range(0, len(n)):
                if s >= len(n):
                    s = s - len(n)
                if s < 0:
                    s = len(n) + s
        song.append(n[s])
    return song


input_notes = input("Give list of notes (separated by space): ")
notes = list(map(str, input_notes.strip().split()))
input_moves = input("Give list of moves (separated by space): ")
moves = list(map(int, input_moves.strip().split()))
start = int(input("Give start position: "))

print(compose(notes, moves, start))
