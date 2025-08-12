from enum import Enum

# Set up an enum to ensure car sizes are consistent with what is allowed by the 
# problem description
class CarSizes(Enum):
    SMALL = 0,
    MEDIUM = 1,
    LARGE = 2

SIZE_STRING = {
    CarSizes.SMALL: "Small",
    CarSizes.MEDIUM: "Medium",
    CarSizes.LARGE: "Large"
}

ALLOWED_CAR_SIZES = {value:key for key, value in SIZE_STRING.items()}

class Car:
    def __init__(self, size, color, brand):
        self.size = size
        self.color = color
        self.brand = brand

class ParkingLot:
    def __init__(self, n):
        self.total_spots = n
        self.free_spots = n
        self.lot = [None]*n
    
    def park(self, spot_num, car):
        if self.free_spots != 0:
            for i in range(spot_num, self.total_spots):
                if self.lot[i] is None:
                    self.lot[i] = car
                    self.free_spots -= 1
                    return i
            for i in range(0, spot_num):
                if self.lot[i] is None:
                    self.lot[i] = car
                    self.free_spots -= 1
                    return i
        return -1
    
    def remove(self, spot_num):
        if self.lot[spot_num] is not None:
            self.lot[spot_num] = None
            self.free_spots += 1
        return str(self.free_spots)

    def print(self, spot_num):
        if self.lot[spot_num] is None:
            return "Empty"
        else:
            return f"{self.lot[spot_num].size} {self.lot[spot_num].color} {self.lot[spot_num].brand}"
    
    def print_free_spots(self):
        return self.free_spots




def parking_system(n: int, instructions: list[list[str]]) -> list[str]:
    parking_lot = ParkingLot(n)
    outputs = []
    for line in instructions:
        if line[0] == "park":
            car = Car(line[2], line[3], line[4])
            spot_chosen = parking_lot.park(int(line[1]), car)
        elif line[0] == "print":
            outputs.append(parking_lot.print(int(line[1])))
        elif line[0] == "print_free_spots":
            outputs.append(parking_lot.print_free_spots())
        elif line[0] == "remove":
            free_spots = parking_lot.remove(int(line[1]))
        else:
            outputs.append("Error in the instructions")

    return outputs

if __name__ == "__main__":
    n = int(input())
    instructions = [input().split() for _ in range(int(input()))]
    res = parking_system(n, instructions)
    for line in res:
        print(line)
