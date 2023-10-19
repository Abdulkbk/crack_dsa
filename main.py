from src.lists.rotated_list import count_rotations, count_rotations2


def main():
    case = [4, 5, 1, 2, 3]
    result = count_rotations(nums=case)
    result2 = count_rotations2(nums=case)
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
