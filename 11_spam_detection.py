p1 = ("Make a lot of money").lower()
p2 = "buy now"
p3 = "send otp"
p4 = "click this"
p5 = "subscribe this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("This is a spam")

else:
    print("This is not a spam")