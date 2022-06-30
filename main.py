import Morse

mode=str(input("Decode or Encode? [d/e] "))

if mode=="e":
    text=str(input("Enter text >"))
    encoded_messege=Morse.Encoder(text).run()
    print(f">{encoded_messege}")

if mode=="d":
    code=str(input("Enter code >"))
    decoded_messege=Morse.Decoder(code).run()
    print(f">{decoded_messege}")