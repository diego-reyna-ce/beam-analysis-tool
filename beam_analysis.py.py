import numpy as np
import matplotlib.pyplot as plt

def beam_analysis():
    print("===================================")
    print(" Simply Supported Beam Analysis Tool")
    print("===================================\n")

    try:
        # Unit selection
        unit_system = input("Select unit system (SI/US): ").strip().upper()

        if unit_system not in ["SI", "US"]:
            print("Invalid unit system. Please restart and choose SI or US.")
            return
        
        # User Inputs
        L = float(input("Enter beam length: "))
        w = float(input("Enter uniform load: "))
        E = float(input("Enter modulus of elasticity: "))
        I = float(input("Enter moment of inertia: "))

        if L <= 0 or w <= 0 or E <= 0 or I <= 0:
            print("All values must be positive.")
            return

        # Engineering Calculations
        max_moment = (w * L**2) / 8
        max_deflection = (5 * w * L**4) / (384 * E * I)

        # Position array
        x = np.linspace(0, L, 500)

        # Deflection equation along beam
        deflection = (w * x * (L**3 - 2*L*x**2 + x**3)) / (24 * E * I)

        # Output
        print("\nResults:")
        print("-------------------------------------")
        print(f"Maximum Bending Moment: {max_moment:.3f}")
        print(f"Maximum Deflection: {max_deflection:.6f}")
        print("--------------------------------------")

        # Plot
        plt.figure()
        plt.plot(x, deflection)
        plt.title("Beam Deflection Curve")
        plt.xlabel("Beam Length")
        plt.ylabel("Deflection")
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

beam_analysis()



          
