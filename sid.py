import aminofix as amino
client = amino.Client()
client.login(email="feonidont8@gmail.com", password="bisdak")
print("Disclaimer > copy sid and put it in data in case of using heroku as server.\n\n")
print(f"{client.sid}")
