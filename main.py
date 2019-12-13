from scapy.all import *
import functools

file = rdpcap('data_streams.pcap')

streams = {
    1: [],
    2: [],
    3: [],
    4: [],
}

length, time = [None] * 4, [None] * 4

for packet in file:
    ip = packet[IP].src
    streams[int(ip[-1])].append(packet)

for k in streams:
    stream = streams.get(k)
    length[k - 1] = len(stream)
    time[k - 1] = functools.reduce(lambda a, b: a + b, map(lambda x: x.time, stream))

print("STREAM INTEGRITY (number of lines based on sample):")
for k, v in streams.items():
    print(f"Stream {k}: {len(v)}")

print(f"conclusion: discard Stream 2")

tym = list(map(lambda x: float(x), time))
lgth = list(map(lambda x: x / max(length), length))

speed = {}

for i, (t, l) in enumerate(zip(tym, lgth)):
    speed[i+1] = l / t

print()
print("ORDER BY SPEED:")
for k in {k: v for k, v in sorted(speed.items(), key=lambda item: item[1], reverse = True)}:
    print(f"Stream {k}")

print("Stick with 3 and 4")
