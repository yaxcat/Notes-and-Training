from enum import Enum

# Enum class
class CarSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

SIZE_STRING = {
    CarSize.SMALL: "Small",
    CarSize.MEDIUM: "Medium",
    CarSize.LARGE: "Large",
}

SIZES = {e: n for n, e in SIZE_STRING.items()}
ALLOWED_CAR_SIZES = {value:key for key, value in SIZE_STRING.items()}

for key, val in SIZE_STRING.items():
    print(key, "-",  val)
print("\n")
for key, val in SIZES.items():
    print(key, "-", val)
print("\n")
for key, val in ALLOWED_CAR_SIZES.items():
    print(key, "-", val)

