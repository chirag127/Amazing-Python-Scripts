from termcolor import colored
from random import randint
from time import sleep

symbol = [
    [
        "\u30A0",
        "\u30A1",
        "\u30A2",
        "\u30A3",
        "\u30A4",
        "\u30A5",
        "\u30A6",
        "\u30A7",
        "\u30A8",
        "\u30A9",
        "\u30AB",
        "\u30AC",
        "\u30AD",
        "\u30AE",
        "\u30AF",
    ],
    [
        "\u30B0",
        "\u30B1",
        "\u30B2",
        "\u30B3",
        "\u30B4",
        "\u30B5",
        "\u30B6",
        "\u30B7",
        "\u30B8",
        "\u30B9",
        "\u30BB",
        "\u30BC",
        "\u30BD",
        "\u30BE",
        "\u30BF",
    ],
    [
        "\u30C0",
        "\u30C1",
        "\u30C2",
        "\u30C3",
        "\u30C4",
        "\u30C5",
        "\u30C6",
        "\u30C7",
        "\u30C8",
        "\u30C9",
        "\u30CB",
        "\u30CC",
        "\u30CD",
        "\u30CE",
        "\u30CF",
    ],
    [
        "\u30D0",
        "\u30D1",
        "\u30D2",
        "\u30D3",
        "\u30D4",
        "\u30D5",
        "\u30D6",
        "\u30D7",
        "\u30D8",
        "\u30D9",
        "\u30DB",
        "\u30DC",
        "\u30DD",
        "\u30DE",
        "\u30DF",
    ],
    [
        "\u30E0",
        "\u30E1",
        "\u30E2",
        "\u30E3",
        "\u30E4",
        "\u30E5",
        "\u30E6",
        "\u30E7",
        "\u30E8",
        "\u30E9",
        "\u30EB",
        "\u30EC",
        "\u30ED",
        "\u30EE",
        "\u30EF",
    ],
    [
        "\u30F0",
        "\u30F1",
        "\u30F2",
        "\u30F3",
        "\u30F4",
        "\u30F5",
        "\u30F6",
        "\u30F7",
        "\u30F8",
        "\u30F9",
        "\u30FB",
        "\u30FC",
        "\u30FD",
        "\u30FE",
        "\u30FF",
    ],
]

while 1:

    chunk_template = ["" for i in range(139)]
    chunk_length = randint(23, 31)
    positions_to_fill = randint(21, 27)
    symbol_positions = set([randint(0, 138) for j in range(positions_to_fill)])
    symbol_positions = list(symbol_positions)

    for x in range(chunk_length):

        for a in symbol_positions:

            row = randint(0, 5)
            col = randint(0, 14)

            chunk_template[a] = symbol[row][col]

        final_line = " ".join(chunk_template)
        print(colored(final_line, "green"))
        sleep(0.07)
