from collections import deque
bank = deque(["Mehedi","Amin","Bijoy"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("No person left ")