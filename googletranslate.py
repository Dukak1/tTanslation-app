from googletrans import Translator
x =True

while x:
    choice = int(input("1-) EN to TR\n2-) TR to EN\nPlease choose one : "))

    if choice == 1 or choice ==2:
        x=False
    else:
        print("You only can choose 1 or 2!!")
    
    while True:
        text1 = input("Please input your text : ").strip()
        if text1 == "q":
            break
        if choice ==1:
            translator = Translator()
            translated_text = translator.translate(text1, dest='tr').text
            print("Translated text:", translated_text)
        elif choice ==2:
            translator = Translator()
            translated_text = translator.translate(text1, dest='en').text
            print("Translated text:", translated_text)
            