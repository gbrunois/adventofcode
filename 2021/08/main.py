#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


def find_segments(codes: [str]):
    segments = {}
    codes = list(map(lambda c: sorted(list(c)), codes))

    segments[1] = [c for c in codes if len(c) == 2][0]
    segments[4] = [c for c in codes if len(c) == 4][0]
    segments[7] = [c for c in codes if len(c) == 3][0]
    segments[8] = [c for c in codes if len(c) == 7][0]

    seg_bd = [c for c in segments[4] if c not in segments[1]]
    segments[5] = [c for c in codes if len(c) == 5 and all(map(lambda x: x in c, seg_bd))][0]
    seg_a = [c for c in segments[7] if c not in segments[1]][0]
    seg_c = [c for c in segments[1] if c not in segments[5]][0]
    seg_f = [c for c in segments[1] if c in segments[5]][0]

    segments[3] = [c for c in codes if len(c) == 5 and seg_c in c and seg_f in c and seg_a in c][0]
    segments[2] = [c for c in codes if len(c) == 5 and c not in [segments[3], segments[5]]][0]
    segments[6] = [c for c in codes if len(c) == 6 and seg_c not in c][0]
    seg_d = [c for c in seg_bd if c in segments[2]][0]
    segments[9] = [c for c in codes if len(c) == 6 and c != segments[6] and seg_d in c][0]
    segments[0] = [c for c in codes if len(c) == 6 and c not in [segments[6], segments[9]]][0]

    return segments


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x.split("|") for x in f.readlines()]

        count = 0
        for line in inputs:
            digits = line[1].strip().split(" ")
            for code in digits:
                if len(code) == 2 or len(code) == 7 or len(code) == 4 or len(code) == 3:
                    count += 1
        print(f"Part 1: {count}")

        decrypted_codes = []
        for line in inputs:

            segments = find_segments(line[0].split(" "))
            segments_map = {"".join(i[1]): str(i[0]) for i in segments.items()}
            encoded_digit = list(map(lambda c: "".join(sorted(list(c))), line[1].strip().split(" ")))
            decrypt_code = int("".join(list(map(lambda c: segments_map["".join(sorted(list(c)))], line[1].strip().split(" ")))))
            decrypted_codes.append(decrypt_code)
        print(f"Part 2: {sum(decrypted_codes)}")




