import configparser

config=configparser.ConfigParser()

config.read(r"D:\Newlystart\scr\src\config_file.ini")

brick_cost = config["raw_materials"]["brick_cost"]

print(f"{brick_cost},type of brick cost is {type(brick_cost)}")

def total_number_of_bricks(length,breadth,height):

    number_of_bricks_in_length_side = length* (height*2)
    total_number_of_brick_of_length_side = number_of_bricks_in_length_side*2

    number_of_bricks_in_breadth_side = breadth* (height*2)
    total_number_of_brick_of_breadth_side = number_of_bricks_in_breadth_side*2

    total_number_of_bricks = total_number_of_brick_of_length_side + total_number_of_brick_of_breadth_side

    return total_number_of_bricks

def total_cost_for_brick(config):

    brick_cost = float(config["raw_materials"]["brick_cost"])
    total_number_of_bricks1 = total_number_of_bricks(15,15,10)
    final_cost =brick_cost * total_number_of_bricks1

    return final_cost

result = total_cost_for_brick(config)

print(f"total brick cost to make 1 room {result}")
