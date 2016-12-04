# Numbers station helper scripts

Here are helper scripts to encode/decode numbers station messages. For more info, see `numbers.tips.html` (taken from [this page](http://www.spynumbers.com/numbers.tips.html)).

## Format

* Encoded message: only letters and spaces (27) are recognised. Each encoded character is seperated by a newline.
* One-time pad (OTP) and encrypted message: 5-digit numbers seperate by newlines

## Usage

Say your message is in message1.txt. To encode as alphabet offsets:

```
./converter.py encode < message1.txt > message1_encoded.txt
```

To generate a OTP of 100 digit groups:
```
./generate_otp.py 100 > otp1.txt
```

To encrypt alphabet offsets with the generated OTP:
```
./crypter.py otp1.txt encrypt < message1_encoded.txt > message1_encrypted.txt
```

You now have a bunch of numbers you can read out on a number station.

To decrypt, just do the reverse:

```
./crypter.py otp1.txt decrypt < message1_encrypted.txt | ./converter.py decode
```
