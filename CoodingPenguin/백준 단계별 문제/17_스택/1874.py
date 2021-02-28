import sys


input = sys.stdin.readline

def create_commands(n, series):
  stack, commands = [], []
  item = 0

  for target in series:
    while item < target:
      item += 1
      stack.append(item)
      commands.append('+')
    if  target == stack[-1]:
      stack.pop()
      commands.append('-')
    else:
      return None
  return commands


if __name__ == "__main__":
  n = int(input().rstrip())
  series = []
  for _ in range(n):
    series.append(int(input()))
  
  commands = create_commands(n, series)
  if not commands:
    print("NO")
  else:
    for c in commands:
      print(c) 