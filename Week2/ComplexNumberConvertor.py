import math as m
import matplotlib.pyplot as plt
import numpy as np


class ComplexNumberCalculator:

    def _convert_catesian_to_polar(self, x, y):
        z = complex(x, y)
        # r = m.sqrt(x*x + y*y)
        r = abs(z)
        angle_radians = m.atan(y / x)
        angle_degree = m.degrees(angle_radians)
        print(f"Complex number in polar form: {r} at angle {angle_degree} degrees")

        if x < 0:
            angle_degree = 180 + angle_degree
        elif x > 0 and y < 0:
            angle_degree = 360 + angle_degree

        return (r, angle_degree)

    def _conver_polar_to_cartesian(self, r, angle):
        angle_rad = m.radians(angle)
        x = round(float(r * m.cos(angle_rad)), 2)
        y = round(float(r * m.sin(angle_rad)), 2)
        return (x, y)


class ComplexNumberPlotter:

    def plot_complex_number_Catesian_form(self, x, y):
        print(f"Plotting complex number: ({x}, {y})")
        plt.figure(figsize=(6, 6))
        plt.axhline(0, color="black", lw=0.5)
        plt.axvline(0, color="black", lw=0.5)
        plt.grid(color="gray", linestyle="--", linewidth=0.5)
        plt.quiver(0, 0, x, y, angles="xy", scale_units="xy", scale=1, color="blue")
        plt.scatter(x, y, color="red")
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.title(f"Complex Number: ({x}, {y})")
        plt.xlabel("Real Part")
        plt.ylabel("Imaginary Part")
        plt.show()

    def plot_complex_number_polar_form(self, h, angle):
        theta = np.angle(angle)
        angle_in_radians = m.radians(angle)
        print(f"Plotting polar representation: (r={h}, theta={angle_in_radians})")
        fig, (ax2) = plt.subplots(1, figsize=(10, 5))
        ax2 = plt.subplot(projection="polar")
        ax2.arrow(0, 0, angle_in_radians, h, width=0.01, color="blue")  # arrow in polar
        ax2.scatter(angle_in_radians, h, color="red")
        ax2.set_title("Polar Form")
        plt.tight_layout()
        plt.show()


def main():
    user_input = ""
    while user_input != "exit":
        print("\nSelect 'c' to convert catesian to polar representation")
        print("Select 'p' to convert polar to catesian representation")

        value = input("\nWhich conversion you need : ")

        if value == "exit":
            print("Convertor terminating...")
            break

        calculator = ComplexNumberCalculator()
        plotter = ComplexNumberPlotter()

        if value == "c":
            print("***Catesian to Polar Conversion***\n")
            x_value = int(input("Enter value for x :"))
            y_value = int(input("Enter value for y :"))

            polar_representation = calculator._convert_catesian_to_polar(
                x_value, y_value
            )
            print(
                f"(Polar representation = {polar_representation[0]: .1f},{polar_representation[1]: .1f}\u00b0)"
            )
            h_value = polar_representation[0]
            angle = polar_representation[1]
            plotter.plot_complex_number_polar_form(h_value, angle)

        elif value == "p":
            print("\n***Polar to Catesian Conversion***\n")
            r_value = int(input("Enter value for r :"))
            angle = int(input("Enter value for angle :"))

            catesian_representation = calculator._conver_polar_to_cartesian(
                r_value, angle
            )
            print(
                f"(Catesian representation = {catesian_representation[0]},{catesian_representation[1]})"
            )
            x_value = catesian_representation[0]
            y_value = catesian_representation[1]

            plotter.plot_complex_number_Catesian_form(x_value, y_value)
        else:
            print("Invalid input. Please enter 'c' or 'p'.")


if __name__ == "__main__":
    main()
