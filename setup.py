import sys, os

FILE_PATH = "src/main/java/frc/team0000/robot/Robot.java"

# python 2 or python 3? it doesn't really matter to me.
try:
    input = raw_input
except NameError:
    pass

def drive_string(side, args):
    return side + "Drive = new SpeedControllerGroup(" + args + ")"
    
def motor_controller_args(ctrl, ports):
    ret = ""
    for port in ports:
        ret += "new " + ctrl + "(" + port + "), "
    return ret.strip(", ")

def main():
    if "/" in sys.argv[0] or "\\" in sys.argv[0]:
        print("Please run this file from the directory it is located in.")
        sys.exit(1)
        
    print("WARNING: This file will self-destruct when it has run successfully!\n")
    team_number = input("Team number: ")
    motor_controller = input("Primary motor controller: ")
    left_ports = input("Left drive motor ports (separated by spaces): ").split(" ")
    right_ports = input("Right drive motor ports: ").split(" ")
    
    print("\nTo confirm:")
    print("Team number is " + team_number)
    print("Motor controllers are " + motor_controller + "s")
    print("Left drive ports are " + str(left_ports))
    print("Right drive ports are " + str(right_ports))
    if input("Is this correct? (y/n) ").lower() not in ["y", "yes"]:
        print("Exiting.")
        sys.exit(1)
    
    with open(FILE_PATH, 'r') as rfiler:
        robot_file = rfiler.read()
    robot_file = (robot_file.replace("0000", team_number)
        .replace(drive_string("left", "null"), drive_string("left", motor_controller_args(motor_controller, left_ports)))
        .replace(drive_string("right", "null"), drive_string("right", motor_controller_args(motor_controller, right_ports))))
    with open(FILE_PATH, 'w') as rfilew:
        rfilew.write(robot_file)
    
    with open("build.gradle", 'r') as gfiler:
        gradle_file = gfiler.read()
    gradle_file = gradle_file.replace("0000", team_number)
    with open("build.gradle", 'w') as gfilew:
        gfilew.write(gradle_file)
    
    os.rename("src/main/java/frc/team0000", "src/main/java/frc/team" + team_number)
    
    print("\nSuccess! This file will now self-destruct. Go team " + team_number + "!")
    
    os.remove(sys.argv[0])
    
if __name__ == "__main__":
    main()