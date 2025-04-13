import time


def main():
    print(
        """
    ███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗
    ████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝
    ██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗
    ██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║
    ██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝
    """
    )

    print("Welcome to Mad Libs! Ready to create some silly stories?")
    time.sleep(1)

    stories = {
        "1": {
            "title": "A Day at the Zoo",
            "template": "Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree. It {verb_past} {adverb} through the large tunnel that led to its {adjective2} {noun2}. I got some {food} and passed it through the cage to a gigantic gray {animal} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop of {ice_cream}. Afterwards I had to {verb} {adverb2} to catch our bus. What a day at the zoo!",
            "prompts": [
                "adjective",
                "noun",
                "verb_past",
                "adverb",
                "adjective2",
                "noun2",
                "food",
                "animal",
                "adjective3",
                "ice_cream",
                "verb",
                "adverb2",
            ],
        },
        "2": {
            "title": "Space Adventure",
            "template": "Captain {name} and the crew of the starship {ship_name} were on a mission to explore the {adjective} planet {planet_name}. As they {verb_past} through the {adjective2} nebula, their {noun} began beeping wildly. 'Captain!' shouted {name2}, 'We're being attacked by {alien_plural}!'. The crew {verb_past2} to their stations and prepared to {verb} the {adjective3} {ship_part}. After a {adjective4} battle, they escaped to the {adjective5} {place} where they celebrated with {food} and {drink}.",
            "prompts": [
                "name",
                "ship_name",
                "adjective",
                "planet_name",
                "verb_past",
                "adjective2",
                "noun",
                "name2",
                "alien_plural",
                "verb_past2",
                "verb",
                "adjective3",
                "ship_part",
                "adjective4",
                "adjective5",
                "place",
                "food",
                "drink",
            ],
        },
        "3": {
            "title": "Fairytale Madness",
            "template": "Once upon a time in a {adjective} kingdom, there lived a {adjective2} {person}. One day, they found a {adjective3} {object} that could {verb}. This discovery led them on a quest to the {place} where they met a {adjective4} {creature} who offered them {number} {magic_items} in exchange for their {noun}. Along the way, they had to {verb2} {adverb} to avoid the {adjective5} {villain}. In the end, they lived {adverb2} ever after!",
            "prompts": [
                "adjective",
                "adjective2",
                "person",
                "adjective3",
                "object",
                "verb",
                "place",
                "adjective4",
                "creature",
                "number",
                "magic_items",
                "noun",
                "verb2",
                "adverb",
                "adjective5",
                "villain",
                "adverb2",
            ],
        },
    }

    while True:
        print("\nChoose a story:")
        for num, story in stories.items():
            print(f"{num}. {story['title']}")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "4":
            print("\nThanks for playing Mad Libs! Goodbye!")
            break
        elif choice in stories:
            play_story(stories[choice])
        else:
            print("Invalid choice. Please select 1-4.")

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing Mad Libs! Goodbye!")
            break


def play_story(story):
    print(f"\n{story['title']}")
    print("You'll be asked to enter various words to fill in the blanks.")
    print("Let's begin!\n")

    answers = {}
    for prompt in story["prompts"]:
        article = "an" if prompt.startswith(("a", "e", "i", "o", "u")) else "a"
        answers[prompt] = input(f"Enter {article} {prompt.replace('_', ' ')}: ")

    madlib = story["template"]
    for key, value in answers.items():
        madlib = madlib.replace("{" + key + "}", value)

    print("\nHere's your Mad Libs story:\n")
    print(madlib)
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
