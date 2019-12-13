Requirements:

- Python 3.7
- The only library required is scapy, for pcap analysis.

The provided script is meant to analyse the speed of the streams provided in the data file. 

My first idea was to check latency, but after reading about the way to extract it I run into trouble:
The latency is defined as the time elapsed between sent and received communications. I used scapy to find both, but none of the packets seems to contain information about the time it was sent. 

I then checked the number of lines to make sure all streams where equally long. I found out that one of them was shorter, which is an immediate red flag. 
A shorter stream means sometime communication is failing for whatever reason. I don't really care why, since I have another 3 healthy streams I can use.

As a substitute for latency, I just aggregated the received times to see which one arrived sooner. 
It still doesn't provide information as crucial as latency, but at least we would have an idea of the speed. If all streams are meant to provide the same information, having the total time over a substantial number of lines seemed relevant.
I aggregated the received times and divided them by the length, just to be able to check the shorter stream and compare to it. 
The fastest streams where 3 and 4. 

The only thing I wish I had was sent times to provide latency. I am no expert in TCP/IP protocols, but that information doesn't seem to be in the file. 



