# Base64
- All data on computer is stored in a number of bytes
- A **byte** is comprised of 8 bits
- A bit can be a 0 or 1
- Data is sotred in bytes but not dipslayed in bytes, this conversion go through is:
    - **Encoding** from text to bytes
    - **decoding** from bytes to text
- One common method for this type of conversion is, **base64**
- The reason why is Base64 is becuase
    - its 'base' basecuse each character equates to a binary value upto 2^6
    - its '64' represented by 64 characters and becuase its power of 2
- In base64 with a single character you can get upto 64 when converted into binary
- In binary a single character is either 1 or 0 and you can only go as as 2^0

- This means:
    - **4 character** in base64 is equal to **3 bytes**, because
        - 3 * 8 bits = 24 bits
        - 2 ^ 24 = 16777216
        - 64 ^ 4 = 16777216
        - 4 character in base64 = 3 bytes

![Base64 Table](../images/base64_table.png)

