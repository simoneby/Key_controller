

signals = ["*","4", "3", "2", "1", "#"]

signal = signals.pop()
print(signals)
signals.reverse()
signals += ["hello"]
signals.reverse()

print(signals)
signal = signals.pop()
print(signals)