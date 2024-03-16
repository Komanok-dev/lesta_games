# Time Complexity O(1)
# Space Complexity O(1)


# All functions have the same complexity with only difference:
# isEven1 could be slower than isEven2 with big numbers
# isEven1 is more understandable than isEven2 for most people


def isEven1(value):
      return value % 2 == 0


def isEven2(value):
      return value & 1 == 0


# Since there can be quite a lot of options here are a couple more functions,
# having the same complexity O(1):


def isEven3(value):
      return False if '.5' in str(value / 2) else True


def isEven4(value):
      return value // 2 * 2 == value
