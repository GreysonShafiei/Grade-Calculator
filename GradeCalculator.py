from GradePointCalculator import WeightedAverageCalculator  # Import from GradePointCalculator

def main():
    grade_types_num = int(input("Enter the number of grade types there are: "))
    grade_types_list = []
    grade_points = []

    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'

    # Reverting back to the original if-elif structure for entering grade types
    for i in range(grade_types_num):
        if i == 0:
            grade_type = input(f"Enter the {i + 1}st grade type: ")
        elif i == 1:
            grade_type = input(f"Enter the {i + 1}nd grade type: ")
        elif i == 2:
            grade_type = input(f"Enter the {i + 1}rd grade type: ")
        else:
            grade_type = input(f"Enter the {i + 1}th grade type: ")
        grade_types_list.append(grade_type)

    # Display the collected grade types
    print(f"\nThere are the following grade types:\n")
    for i in range(grade_types_num):
        print(f"- {bold}{grade_types_list[i]}{reset}")

    # Calculate total points for each grade type
    for grade_type in grade_types_list:
        print(f"\nInitializing calculator with {grade_type}")
        instance_of_grade_type = WeightedAverageCalculator()
        grade_points.append(instance_of_grade_type.calculate_weighted_average(grade_type))

    # Calculate and display total points earned
    total_points_earned = calculate_totals(grade_points)
    print(f"\nYou have earned {bold}{underline}{total_points_earned}{reset} total!")

    # Calculate remaining points to meet the goal
    point_goal = int(input("Enter your total point goal out of 100 points: "))
    points_to_go = point_goal - total_points_earned
    print(f"\nYou have {points_to_go} points left to meet your goal!")

def calculate_totals(grade_points):
    # Summing up all the grade points
    return sum(grade_points)

if __name__ == "__main__":
    main()
