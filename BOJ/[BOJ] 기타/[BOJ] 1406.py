import sys

text = list(sys.stdin.readline().strip())
buffer = []  # Initialize the buffer list as empty
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if text:
        buffer.append(text.pop())
    elif cmd[0] == "D":
        if buffer:
            text.append(buffer.pop())
    elif cmd[0] == "B":
        if text:
            text.pop()
    elif cmd[0] == "P":
        text.append(cmd[1])

print("".join(text + list(reversed(buffer))))