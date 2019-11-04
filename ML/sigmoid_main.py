import numpy as np
import ML.Sigmoid as sg


def main():
    z = np.arange(-7, 7, 1)
    print(z)
    st = sg.Sigmoid()
    st.plot(z)

if __name__ == '__main__':
    main()


