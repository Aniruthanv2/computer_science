name = input('enter your username')
if name == ('Admin' or name == 'admin'):
    print('welcom administrator')
passkey = input('enter the password')
passkey = int(passkey)
if passkey == 1234:
    print('welcom,you will have administrator access')
else:
    print('incorrect password for admin,you will have standard user access')
    