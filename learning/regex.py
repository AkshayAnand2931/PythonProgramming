import re

if __name__ == "__main__":

    text = "My name is ABC and phone number is 408-555-1234 "
    pattern = "phone"

    print(re.search(pattern,text))
    matches = re.findall(pattern,text)
    print(len(matches))

    phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d",text)
    phone2 = re.search(r"\d{3}-\d{3}-\d{4}",text)
    phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
    results = re.search(phone_pattern,text)
    print(results.group(1),results.group())

    re.search(r'cat|dog',"The cat is here")
    print(re.findall(r'.at',"the cat in the hat went splat"))
    print(re.findall(r'...at',"the cat in the hat went splat"))

    re.findall(r'^\d',text) #starts with
    re.findall(r'\d$',text) #ends with
    re.findall(r'[^\d]',text) #excludes
    print(re.findall(r'[^!.,?]+',"there, is ,a lot of. punctuation!!!"))
    re.findall(r'cat(fish|nap|erpillar)',"catfish")