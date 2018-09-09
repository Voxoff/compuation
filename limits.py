def halts(f):
  pass

def halter():
  return

def looper():
  while True:
    pass

halts(halter)
halts(looper)

def impossible():
  return halts(impossible) and looper()

# either halts impossible returns true or false
# assume true, so impossible halts
# So we evaluate looper, thus infinite loop and impossible halts
# Contradiction!
# Assume false, so impossible does not halt
# looper not evaluated, so return False so impossible function terminated. 

