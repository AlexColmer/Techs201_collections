story1 = {
    "start": "This is a story of how one man saved a nation. He was a simple man who no one thought that much of. "
             "However what no one knew was this man had a secret fortune where he built some amazing contraptions ",
    "middle": "one of these contraptions that this man had built was a sword hat could be turned into a gun whenever "
              "he needed it. HE didn't realise how much he would need this weapon. Because on day a man came to his "
              "town and started to terrorize the civilians. Our hero realised that he had the means to stop this man "
              "from destroying his neighbourhood and went out to face him. he got his swung which is what he called "
              "hid sword gun contraption and met this man in the middle of the street adn the battle the ensured no "
              "one had ever seen anything like it before he could use the gun when he was able to get some distance "
              "and the sword when the evil man came to close. After hours of fighting our hero had finally won.",
    "end": "In the end the towns people rejoinced in finally having the man defeated and they could go back and live "
           "out there normal lives and our hero was no longer an ordinary man he was a hero in the eyes of everyone "
           "in his neighbourhood "
}

print(story1)

print(type(story1))

print(story1.keys())

print(story1.values())

print(story1.items())

print(story1.get("start"))

print(story1.get("middle"))

print(story1.get("end"))

new_key = "hero"
new_value = "The swung man"

story1["hero"] = "The swung man"
print(story1)

