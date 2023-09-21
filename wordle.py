def wordle_clue_1(hidden: str, candidate: str) -> str:
    """
    Returns a string indicating the letters which are in the correct position.

    Use "x" for correct letters in the correct position, and "-" otherwise.
    """
    output_string = ""

    for hidden_char, candidate_char in zip(hidden, candidate):
        if hidden_char == candidate_char:
            output_string += "x"
        else:
            output_string += "-"

    return output_string


def wordle_clue_2(hidden: str, candidate: str) -> str:
    """
    Returns a string indicating the letters which are in the correct position
    and those which are present in the hidden word but are in the wrong position
    in the candidate word. Use "x" for correct letters in the correct position,
    "o" for correct letters in the wrong position, and "-" otherwise.
    """
    output_string = ""

    for hidden_char, candidate_char in zip(hidden, candidate):
        if hidden_char == candidate_char:
            output_string += "x"

        elif candidate_char in hidden:
            output_string += "o"

        else:
            output_string += "-"

    return output_string


def wordle_clue_3(hidden: str, candidate: str) -> str:
    """
    Returns a string indicating the letters which are in the correct position
    and those which are present in the hidden word but are in the wrong position
    in the candidate word, ensuring a letter is not indicated more times in the
    candidate word than it is present in the hidden word.
    Use "x" for correct letters in the correct position, "o" for indicated
    letters in the wrong position, and "-" otherwise.
    """

    output_clue = ["placeholder"] * len(hidden)
    # record chars we have already iterated on
    candidate_buffer = ["placeholder"] * len(hidden)

    # first pass add the matches
    for index, (hidden_char, candidate_char) in enumerate(zip(hidden, candidate)):
        if hidden_char == candidate_char:
            output_clue[index] = "x"
            candidate_buffer[index] = candidate_char

    # no character match, and no characters the same present anywhere
    for index, (hidden_char, candidate_char) in enumerate(zip(hidden, candidate)):
        if hidden_char != candidate_char and candidate_char not in hidden:
            output_clue[index] = "-"
            candidate_buffer[index] = candidate_char

    # no character match, but the same character is present somewhere
    for index, (hidden_char, candidate_char) in enumerate(zip(hidden, candidate)):
        if hidden_char != candidate_char and candidate_char in hidden:
            # not enough chars in candidate_buffer yet
            if candidate_buffer.count(candidate_char) < list(hidden).count(
                candidate_char
            ):
                output_clue[index] = "o"
                candidate_buffer[index] = candidate_char

            #  already have enough of that character
            elif candidate_buffer.count(candidate_char) == list(hidden).count(
                candidate_char
            ):
                output_clue[index] = "-"
                candidate_buffer[index] = candidate_char

    output_string = "".join(output_clue)
    return output_string
