class WeightedAverageCalculator:
    total_grade_points = 0
    difference_from_90 = 90

    def calculate_weighted_average(self, object_type="Object"):
        bold = '\033[1m'
        underline = '\033[4m'
        reset = '\033[0m'


        # Get the number of objects (e.g., tests, assignments)
        num_objects = int(input(f"Enter the number of {underline}{bold}{object_type}'s{reset}: "))

        total_weight = 0
        total_weighted_score = 0
        total_score = 0

        if num_objects > 0:
            evenly_weighted = input("Are all of these assignments evenly weighted? (T/F): ").strip().lower()

            if evenly_weighted == "f":  # Not evenly weighted
                for i in range(num_objects):
                    print(f"\n{object_type} {i + 1}:")
                    weight = float(input(f"Enter the weight of the {object_type} (as a percentage, e.g., 20 for 20%): ")) / 100
                    score = float(input(f"Enter the percent earned on the {object_type} (e.g., 85 for 85%): "))
                    
                    # Calculate weighted score for this object
                    total_weighted_score += (score * weight)
                    total_weight += weight

                if total_weight == 0:
                    print("The total weight cannot be zero.")
                    return None
                else:
                    weighted_average = total_weighted_score / total_weight
                    total_adjusted_score = total_weight * weighted_average
                    self.difference_from_90 -= total_adjusted_score

                    # Output the results
                    self.print_results(object_type, weighted_average, total_weight, total_adjusted_score, self.difference_from_90)

                return total_adjusted_score

            else:  # Evenly weighted
                weight = float(input(f"Enter the overall weight of the {object_type}'s (as a percentage, e.g., 20 for 20%): ")) / 100

                for i in range(num_objects):
                    print(f"\n{object_type} {i + 1}:")
                    score = float(input(f"Enter the percent earned on the {object_type} (e.g., 85 for 85%): "))
                    total_score += score  # Summing scores for evenly weighted objects

                weighted_average = total_score / num_objects
                total_weighted_score = weighted_average * weight
                total_adjusted_score = total_weighted_score
                self.difference_from_90 -= total_adjusted_score

                # Output the results
                self.print_results(object_type, weighted_average, weight, total_adjusted_score, self.difference_from_90)

                return total_adjusted_score

        else:
            print("You must have at least one object to calculate the average.")
            return None

    def print_results(self, object_type, weighted_average, total_weight, total_adjusted_score, difference_from_90):
        bold = '\033[1m'
        underline = '\033[4m'
        reset = '\033[0m'

        print(f"\nThe weighted {object_type} percent average is: {underline}{bold}{weighted_average:.2f}%{reset}")
        print(f"The total weight of {object_type} grades is: {underline}{bold}{total_weight * 100:.2f}%{reset}")
        print(f"The total grade points earned from {object_type}s is: {underline}{bold}{total_adjusted_score:.2f}{reset}")
        print(f"There are {underline}{bold}{difference_from_90:.2f}{reset} points left to earn to keep an A")
