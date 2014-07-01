import numpy as np

names = ['1_3', '3_5', '2_3', '1_6', '2_6', '4_5', '1_7', '2_7', '3_7', '5_7', '6_7']


def main():
    for i in range(len(names)):
        name = names[i]

        data = np.loadtxt('input/%s.txt' % name, delimiter=",")
        time = data[:, 0]
        counts = data[:, 1]

        time_b = time[0:-1:2]
        counts_b = np.array([counts[j-1] + counts[j] for j in np.arange(1, len(counts)+1, 2)])
        export_data = np.vstack((time_b, counts_b)).T

        print 'saving input/rebinned/%s.txt' % name
        np.savetxt('input/rebinned/%s.txt' % name, export_data, fmt="%1.3lf,%1.3lf,0.000,0.000,0.000")

if __name__ == "__main__":
    main()
