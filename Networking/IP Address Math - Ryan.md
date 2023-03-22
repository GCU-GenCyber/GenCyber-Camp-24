# IP Addresses
IP addresses are the internet versions of our physical addresses. It is formatted as the following:

X.X.X.X

Each X can be replaced with a number between 0-255.
To calculate the total number of IPv4 addresses that are usable we do 255^4
This totals to 4,228,250,625 usable IP addresses.

These IP addresses can also be calculated into binary. Binary is the base language of a computer. This is the infamous 1011010101001001 language. Each X can be calculated into a binary form. The X is technically an octet, meaning 8 1’s or 0’s. So an IP address in binary form could look like:

11000000.10101000.00101101.00000011

Each place where there is a 1 means this slot is on, each on slot represents a number that is added to total the octet. 

&nbsp;

The octet positions are:

128|64|32|16|8|4|2|1

0|0|0|0|0|0|0|0

&nbsp;

When one of these positions are on, we add it to the total.
So the binary we worked with before, the first octet we had 11000000.
If we put it in the chart it looks like this:


128|64|32|16|8|4|2|1

1|1|0|0|0|0|0|0

So we need to add 128+64. That equals 192. So the first X of the IP address is 192.
So if we look at the IP we had previously in total, the next set had 128+32+8 which equals 162.
The next number is 32+8+4+1 which equals 45. The final octet is 2+1 which is 3. So the IP address in total is 192.168.45.3.


Let’s take the IP address of 172.16.89.142


In the first octet we have 172
We can check to see if the addition of each section will be greater than the number.
So is 172 > 128? Yes? Then add a 1 to the 128 slot. Now is 172 > 128+64? No. So we do not add a 1 to the second slot. We do this for each slot until we get to the result. Once we have hit the number, we can stop checking cause we don’t need to add any more to the octet. 

&nbsp;

RESULTS of 172:


128|64|32|16|8|4|2|1

1|0|1|0|1|1|0|0


RESULTS of 16:

128|64|32|16|8|4|2|1

0|0|0|1|0|0|0|0

RESULTS of 89:

128|64|32|16|8|4|2|1

0|1|0|1|1|0|0|1

RESULTS of 142:

128|64|32|16|8|4|2|1

1|0|0|0|1|1|1|0

END RESULT:

10101100.00010000.01011001.10001110
