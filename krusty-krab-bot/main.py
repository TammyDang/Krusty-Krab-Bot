import os
import discord
import random

from stay_awake import stay_awake

stay_awake

bot = discord.Client()
my_secret = os.environ['TOKEN']


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.formal(bot))


@bot.event
async def on_message(message):
    if message.author == bot:
        return

    if message.content.startswith('hi'):
        await message.channel.send(
            'Hello :) I hope you are having a nice day, I am the krusty krabs.'
        )

    if "shut up" in message.content.lower():
        await message.channel.send('no')

    if "bad" in message.content.lower():
        await message.channel.send('Did you mean good? :eye::lips::eye:')

    if message.content.startswith('$echo'):
        await message.channel.send(message.content[5:].strip())

    if message.content.startswith('$HBD'):
        if len(message.mentions) == 0:
            await message.channel.send("Happy birthday, <@" +
                                       str(message.author.id) +
                                       ">!:partying_face::birthday::cake:")
        else:
            for mention in message.mentions:
                await message.channel.send("Happy birthday, <@" +
                                           str(mention.id) +
                                           ">!:partying_face::birthday::cake:")

    if message.content.startswith('$help'):
        await message.channel.send(
            "Options: \n1. $rolldice #\n2. $wheelspin #\n3. $numberguess #\n4. $flipcoin\n5. $HBD @\n6. $echo [message] \n7. Fortune time!\n8. Tell me a joke!\n9. Pick a person! @\n* fill in # with a numerical value\n* @ with a user's or users' tag(s)\n*  [message] with any message!\n* $numberguess values range from 1-10\nP.S. This bot does not condone negativity! "
        )
        await message.channel.send(" :kissing_heart: ")

    if message.content.startswith('$rolldice'):
        num = int(message.content[9:].strip())
        rolled = 0
        human_array = []
        bot_array = []
        total_person = 0
        total_bot = 0
        while rolled < num:
            randomlist = ["1", "2", "3", "4", "5", "6"]
            human_value = random.choice(randomlist)
            bot_value = random.choice(randomlist)
            total_person += int(human_value)
            total_bot += int(bot_value)
            human_array.append(human_value)
            bot_array.append(bot_value)
            rolled += 1
            if rolled == num:
                await message.channel.send(
                    str(human_array) + ": Total Player Value: " +
                    str(total_person))
                await message.channel.send(
                    str(bot_array) + ": Total Bot Value: " + str(total_bot))
                if total_bot > total_person:
                    await message.channel.send(
                        "You lose, loser! Try harder next time! >:D")
                else:
                    await message.channel.send(
                        "Mom pick me up, I'm scared I lost again :( :cry:")

    if message.content.startswith('$numberguess'):
        randomlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        bot_number = int(random.choice(randomlist))
        num = int(message.content[12:].strip())
        if bot_number == num:
            await message.channel.send(
                "Wow you guessed my number! I would give you a highfive, but I have no hands!"
            )
        else:
            await message.channel.send("Sorry! You guess wrong loser! RUN.")

    if message.content.startswith('$flipcoin'):
        randomlist = ["Tails", "Heads"]
        await message.channel.send(random.choice(randomlist))

    if message.content.startswith('$wheelspin'):
        num = message.content[10:].strip()
        added = 1
        words_list = []
        while added <= int(num):
            words_list.append(added)
            added += 1
        pick = random.choice(words_list)
        await message.channel.send("You landed on option " + str(pick) + "!")

    if message.content.startswith('Fortune time!'):
        fortunelist = [
            "You will have a bad day!", "You will have a good day!",
            "Today, you will meet the love of your life!",
            "You will have 10 kids in the future, I pray for you",
            "You will be rich!!! Quit your job!", "You will live a long life!",
            "Do not leave your house today...", "You will win the lottery!",
            "RUN!", "Lock your front door...", "Do not take the bus today.",
            "There is someone under your bed.",
            "Someone is trying to surprise you.", "Eat an apple today.",
            "Your bank account has been suspended for fraud, please contact your local bank.",
            "You've met your soulmate, it's me ;)", "Don't turn around.",
            "Es hora de comer.", "Do not hesitate when the moment comes."
        ]
        fortune = random.choice(fortunelist)
        await message.channel.send(fortune)

    if "sad" in message.content.lower():
        sadlist = [
            "Keep your head up!", "Things will get better.",
            "Life may be hard, but you are cool!", "It'll be okay.",
            "You're doing great, keep going!", "You can do this!",
            "Things will turn around, don't give up!", "Alexa play despacito.",
            "I love you", "I'm here for you.", "Do you want a krabby patty?",
            "Did you fix the indentation?", "Then stop.",
            "You're not you, when you're hungry.",
            "Have a break, have a KitKat!", "Uno reverse card!"
        ]
        encouragement = random.choice(sadlist)
        await message.channel.send(encouragement)

    if message.content.startswith('Tell me a joke!'):
        jokelist = [
            "My life....hahaha..):",
            "What did the fish say when he swam into a wall\n\nDam.",
            "Did you hear about the Italian chef who died?\n\nHe pasta-away.",
            "I like elephants.\n\nEverything else is irrelephant.",
            "What do you call a fake noodle?\n\nAn impasta.",
            "What do you call an alligator in a vest?\n\nAn in-vest-igator.",
            "Why can't you hear a pterodactyl use the restroom?\n\nBecause they're dead.",
            "What do you call a cow with no legs?\n\nGround Beef.",
            "Why did Snoop Dogg need an unbrella?\n\nFo Drizzle.",
            "Why don't oysters donate to charity?\n\nThey're shellfish.",
            "What does a clock do when it's hungry?\n\nIt goes back four seconds.",
            "What kinds of pictures do hermit crabs take?\n\nShellfies.",
            "What's the action like at a circus?\n\nIn-tents."
        ]
        joke = random.choice(jokelist)
        await message.channel.send(joke)

    if message.content.startswith('Pick a person!'):
        people_list = []
        for mention in message.mentions:
            people_list.append(mention.id)
        picked = random.choice(people_list)
        await message.channel.send("I pick, <@" + str(picked) + ">!")


bot.run(os.environ['TOKEN'])
