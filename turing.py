X_B = {
  ("B", "s1"):("X", "R", "s2"),
  ("B", "s2"):("B", "L", "s3"),
  ("X", "s3"):("B", "R", "s4"),
  ("B", "s4"):("B", "L", "s1")
}


def simulate():
  tape = ["B", "B"]
  head = 0
  state = "s1"
  for _ in range(8):
    print(state + ": " + "".join(tape))
    print("    " + " " * head + "^")
    key = X_B[tape[head], state]
    tape[head], direction, state = key
    head += 1 if direction == "R" else -1

simulate()
