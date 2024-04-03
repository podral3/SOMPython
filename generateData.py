import csv
import random

def generate_and_save_rgb_data(filename, n):

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['r', 'g', 'b', 'color'])  # Write the header row

        for _ in range(n):
            color_choice = random.choice(['red', 'green', 'blue'])
            if color_choice == 'red':
                r = 255
                g = 0  # Limit green for red dominance
                b = 0  # Limit blue for red dominance
                color = "red"
            elif color_choice == 'green':
                r = 0  # Limit red for green dominance
                g = 255
                b = 0  # Limit blue for green dominance
                color = "green"
            else:
                r = 0  # Limit red for blue dominance
                g = 0  # Limit green for blue dominance
                b = 255
                color = "blue"
            writer.writerow([r, g, b, color])

generate_and_save_rgb_data('SomDataGrouping.csv', 1500)  # Generate 150 rows