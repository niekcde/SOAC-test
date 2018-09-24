# MAIO exercise 2
# Fourier transforms
# Niek Collot d'Escury


import numpy as np
from scipy import fftpack
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib as mpl
################################################################
# plotting parameters
mpl.rcParams["figure.figsize"] = [8 , 4.8]
mpl.rcParams['legend.fontsize'] = 12      #legend size
#title params
mpl.rcParams['axes.titlesize'] = 17
mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rcParams['font.style'] = 'italic'    #all fonts italic
#axes params
mpl.rcParams['axes.labelsize'] = 15
mpl.rcParams["xtick.labelsize"] = 13
mpl.rcParams["ytick.labelsize"] = 13
# line width and grid
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams["axes.grid"] = 1
mpl.rcParams["figure.subplot.left"] = 0.15
# mpl.rcParams['savefig.pad_inches'] =  0.6
mpl.rcParams['legend.loc'] =  'best'

###############################################################

np.random.seed(42)

def plot(x , x_extent , steps , ex , title , noise):
    
    plt.figure(1)
    x_axis = np.arange(0 , x_extent , steps)
    plt.plot(x_axis , x)
    plt.title(ex + title)
    plt.xlabel("Time (yr)")
    plt.ylabel("Data")
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    # plt.savefig('/Users/niekcollotdescury/Desktop/MAIO/ex2/figures/' + ex +noise+"data.png" )
    plt.show()

    X = fftpack.fft(x)   # fourier transform
    freqs = fftpack.fftfreq(len(x) , d = 1000) 
    X = np.abs(X)**2



    length = int(len(X) / 2)
    cum    = np.zeros(length)
    cum[0] = X[0]
    for i in range (1 , length):
        cum[i] = X[i] + cum[i-1]
    cum = (cum / cum[-1] ) *100
    
    plt.figure(2)
    plt.bar(freqs[0 : length] , cum  , width = 5e-7)
    plt.title(ex + title +" integrated power")
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude (%)')
    plt.xlim(0, 5e-5)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    # plt.savefig('/Users/niekcollotdescury/Desktop/MAIO/ex2/figures/' + ex + noise+ "cum.png" )
    plt.show()
    
    y_lim = max(X[1:-1]) *1.1
    
    plt.figure(3)
    plt.stem(freqs, X)
    plt.title(ex + title)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.xlim(-1e-6, 5e-5)
    plt.ylim(0, y_lim)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    # plt.savefig('/Users/niekcollotdescury/Desktop/MAIO/ex2/figures/' + ex + noise+ "freq.png" )
    plt.show()

############### exercise 2.1 ###############

x = np.zeros(600)
x[299:300] = 1

x_axis = len(x)
plot(x , x_axis , 1 , "Exercise 2.1 ","\nDelta function" , "")

############### exercise 2.2 ###############
k = 2*np.pi /1e5
listsin = np.arange(0,1e6,1000)
datasin =  np.sin(listsin*  k)

plot(datasin , 1e6 , 1000 , "Exercise 2.2 ","\nSine-wave" , "")

############## exercise 2.3 ###############

time = np.linspace(0, 1e6, 1000)
k = 20
saw = (signal.sawtooth(k * np.pi *time)) 


plot(saw , 1e6 , 1000 , "Exercise 2.3 ","\nSawtooth" , "")

############### exercise 2.5 ###############
saw_tot = []
time_tot = []
for i in range(11):
    T_high = 1.2e5   # +0.02 myr
    T_low = 8e4      # -0.02 myr
    T = np.random.uniform( T_low, T_high)
    k = 2 * np.pi / T
    
    T = np.arange(0 , T , 1000)
    saw = (signal.sawtooth(k *T)  )  
    time_tot.extend(T)
    saw_tot.extend(saw)
saw_tot = saw_tot[0:1000]

plot(saw_tot[0:1000] , 1e6 , 1000 , "Exercise 2.5 ","\nSawtooth varying wavelength" , "")

############## exercise 2.6 ###############

saw_tot = []
time_tot = []
for i in range(11):
    T_high = 1.2e5   # +0.02 myr
    T_low = 8e4      # -0.02 myr
    T = np.random.uniform( T_low, T_high)
    k = 2 * np.pi / T
    
    T = np.arange(0 , T , 1000)
    saw = (signal.sawtooth(k *T))  
    time_tot.extend(T)
    saw_tot.extend(saw)
    
saw_tot = saw_tot[0: 1000]
noise = np.random.normal(0, 0.5 , len(saw_tot))
saw_n = saw_tot + noise

plot(saw_tot , 1e6 , 1000 , "Exercise 2.6","\n Sawtooth varying wavelength" , "")
plot(saw_n , 1e6 , 1000 , "Exercise 2.6","\n Sawtooth varying wavelength\n"," with noise")




