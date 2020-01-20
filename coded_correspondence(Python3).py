# Casual Coded Correspondence: The Project

# Step 1: Decode Vishal's Message
# decode 'Xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
# with offset 10

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decode(message, offset):
    decoded_message = ''
    for letter in message:
        if letter in alphabet:
          new_letter = alphabet[(alphabet.find(letter) + offset)%26]
          decoded_message += new_letter
        elif letter.lower() in alphabet:
          new_letter = alphabet[(alphabet.find(letter.lower()) + offset)%26].upper()
          decoded_message += new_letter
        else:
          decoded_message += letter
    print(decoded_message)

decode('Xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!',10)  

# Step 2: Send Vishal a Coded Message

def encode(message, offset):
    encoded_message = ''
    for letter in message:
        if letter in alphabet:
          new_letter = alphabet[(alphabet.find(letter)-offset)%26]
          encoded_message += new_letter
        elif letter.lower() in alphabet:
          new_letter = alphabet[(alphabet.find(letter.lower())-offset)%26].upper()
          encoded_message += new_letter
        else:
          encoded_message += letter
    print(encoded_message)

encode('Geronimo!', 10)


# Step 3: Make functions for decoding and coding 
# decode 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud' with offset 10
# decode 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!' with offset found in last message

decode ('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud',10)

decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14)


# #### Step 4: Solving a Caesar Cipher without knowing the shift value
          
#  vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.

for i in range(1, 25):
    print(i)
    decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx", i)


# #### Step 5: The Vigenère Cipher
             
#                 dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
# the keyword to decode my message is :    friends


def decode_viginere(message, keyword):
    decoded_message = ''
    count = 0
    for letter in message:
        if letter in alphabet:
          new_letter = alphabet[(alphabet.find(letter) - alphabet.find(keyword[count]))%26]
          decoded_message += new_letter
          count = (count+1)%len(keyword)
        elif letter.lower() in alphabet:
          new_letter = alphabet[(alphabet.find(letter.lower()) - alphabet.find(keyword[count]))%26].upper()
          decoded_message += new_letter
          count = (count+1)%len(keyword)
        else:
          decoded_message += letter
    print(decoded_message)

decode_viginere('''dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!''', 'friends')


# #### Step 6: Send a message with the  Vigenère Cipher


def encode_viginere(message, keyword):
    encoded_message = ''
    count = 0
    for letter in message:
        if letter in alphabet:
          new_letter = alphabet[(alphabet.find(letter) + alphabet.find(keyword[count]))%26]
          encoded_message += new_letter
          count = (count+1)%len(keyword)
        elif letter.lower() in alphabet:
          new_letter = alphabet[(alphabet.find(letter.lower()) + alphabet.find(keyword[count]))%26].upper()
          encoded_message += new_letter
          count = (count+1)%len(keyword)
        else:
          encoded_message += letter
    print(encoded_message)
    return encoded_message
encode_viginere('you were able to decode this? nice work! you are becoming quite the expert at crytography!', 'friends')
decode_viginere(encode_viginere('you were able to decode this? nice work! you are becoming quite the expert at crytography!', 'friends'),'friends')

