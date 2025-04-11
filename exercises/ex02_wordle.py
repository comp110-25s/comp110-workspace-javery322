"""This is code for the game wordle"""

__author__: str = "730656365"


def contains_char(word: str, char: str) -> bool:
    """checks to see if a word contains a certain character"""
    assert len(char) == 1, f"len('{char}') is not 1"
    count: int = 0
    final = False
    while count < len(word):
        if char == word[count]:
            final = True
        count = count + 1
    return final


def emojified(guess: str, secret: str) -> str:
    """creates emoji string that scores a guess for a wordle game"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emojis = emojis + GREEN_BOX
        elif contains_char(secret, guess[i]):
            emojis = emojis + YELLOW_BOX
        else:
            emojis = emojis + WHITE_BOX
        i = i + 1
    return emojis


def input_guess(N: int) -> str:
    """prompts users to input words until they put one of desired length"""
    return_word: str = ""
    num: int = 0
    while len(return_word) != N:
        if num == 0:
            guess_word: str = input(f"Enter a {N} character word:")
            num = num + 1
        if len(guess_word) == N:
            return_word = guess_word
        else:
            guess_word = input(f"That wasn't {N} chars! Try again:")
    return return_word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    GREEN_BOX: str = "\U0001F7E9"
    turn: int = 1
    secret_length: int = len(secret)
    winner: bool = False
    while winner == False and turn < 7:
        print(f"=== Turn {turn}/6 ===")
        emojis_result: str = emojified(guess=input_guess(secret_length), secret=secret)
        print(emojis_result)
        if emojis_result == f"{len(secret) * GREEN_BOX}":
            winner = True
            print(f"You won in {turn}/6 turns!")
        turn = turn + 1

    if turn == 7:
        print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main(secret="codes")
