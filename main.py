from dhooks import Webhook
print("Simple Webhook sender")
wh = input("Enter your webhook: ")
message = input("What do you want to print? ")
hook = Webhook(wh)
hook.send(message)

