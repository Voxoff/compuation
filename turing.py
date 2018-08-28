x_b = {
  ("B", "s1"):("X", "R", "s2"),
  ("B", "s2"):("B", "L", "s3"),
  ("X", "s3"):("B", "R", "s4"),
  ("B", "s4"):("B", "L", "s1")
}


def simulate():
  tape = ["B", "B"]
  head = 0
  state = "s1"
  print("called")
  for _ in range(8):
    key = x_b[tape[head], state]
    print(key)


simulate()
