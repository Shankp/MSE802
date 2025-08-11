import math as m

class ComplexNumberCalculator:

    def _convert_catesian_to_polar(self, x , y):
        r = m.sqrt(x*x + y*y)
        angle_radians =  m.atan(y/x)
        angle_degree = m.degrees(angle_radians)

        if(x <0):
            angle_degree = 180 + angle_degree
        elif (x >0 and y<0):
            angle_degree = 360 + angle_degree

        return(r, angle_degree)
    
    def _conver_polar_to_cartesian(self, r, angle):
        angle_rad = m.radians(angle)
        x = r * m.cos(angle_rad)
        y = r * m.sin(angle_rad)
        return (x, y)

def main():
    user_input = ""
    while(user_input != "exit"):
        print("\nSelect 'c' to convert catesian to polar representation")
        print("Select 'p' to convert polar to polar catesian")

        value = input("\nWhich conversion you need : ")
        
        if(value=="exit"):
            print("Convertor terminating...")
            break

        calculator = ComplexNumberCalculator()

        if(value == "c"):
            print("***Catesian to Polar Conversion***\n")
            x_value = int(input("Enter value for x :"))
            y_value = int(input("Enter value for y :"))

            polar_representation = calculator._convert_catesian_to_polar(x_value, y_value)
            print(f"(Polar representation = {polar_representation[0]: .1f},{polar_representation[1]: .1f}\u00B0)")

        elif(value == "p"):
            print("\n***Polar to Catesian Conversion***\n")
            r_value = int(input("Enter value for r :"))
            angle = int(input("Enter value for angle :"))

            catesian_Conversion = calculator._conver_polar_to_cartesian(r_value,angle)
            print(f"(Catesian representation = {catesian_Conversion[0]: .1f},{catesian_Conversion[1]: .1f})")


if __name__ == "__main__":
    main()