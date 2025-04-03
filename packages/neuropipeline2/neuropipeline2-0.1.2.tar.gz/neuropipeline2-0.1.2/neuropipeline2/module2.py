 
import numpy as np

def calculate_cross_spectral_density(signals, f):
    """
    Calculates the cross-spectral density matrix S(f) of the measured signals.

    Args:
        signals (list of numpy arrays): List of measured signals x_i(n).
        f (float): Frequency of interest.

    Returns:
        numpy array: Cross-spectral density matrix S(f).
    """
    N = len(signals)
    S = np.zeros((N, N), dtype=complex)  # Initialize S as a complex matrix

    for i in range(N):
        for j in range(N):
            # Placeholder for calculating S_ij(f).
            # In a real implementation, you would use a method like Welch's method
            # or a similar spectral estimation technique to compute the cross-spectral density.
            # Here, we use a simplified placeholder to illustrate the structure.
            # Replace this with the actual cross-spectral density calculation.

            # Simple placeholder: assuming signals are time-domain, take FFT, then multiply
            # and average (this is very simplified and not robust)
            signal_i_fft = np.fft.fft(signals[i])
            signal_j_fft = np.fft.fft(signals[j])

            #find the index related to frequency f.
            freq_axis = np.fft.fftfreq(len(signals[0]), 1) #1 is the sample rate.
            index_f = np.argmin(np.abs(freq_axis - f))

            S[i, j] = signal_i_fft[index_f] * np.conj(signal_j_fft[index_f]) # simplified placeholder

    return S

def calculate_coherence(S, i, j):
    """
    Calculates the ordinary coherence function C_ij(f).

    Args:
        S (numpy array): Cross-spectral density matrix S(f).
        i (int): Index of the first area.
        j (int): Index of the second area.

    Returns:
        float: Coherence C_ij(f).
    """
    S_ij = S[i, j]
    S_ii = S[i, i].real  # Use the real part for auto-spectra
    S_jj = S[j, j].real

    if S_ii == 0 or S_jj == 0:
      return 0.0 #avoid division by zero.
    return (np.abs(S_ij)**2) / (S_ii * S_jj)

def linear_operator(X_i, T_ji):
    """
    Models the interaction using a linear operator T_ji.

    Args:
        X_i (complex): Frequency-domain representation of signal i.
        T_ji (complex): Linear operator from i to j.

    Returns:
        complex: Frequency-domain representation of signal j.
    """
    return T_ji * X_i

def inverse_linear_operator(X_j, T_ij):
    """
    Models the interaction using the inverse linear operator T_ij.

    Args:
        X_j (complex): Frequency-domain representation of signal j.
        T_ij (complex): Inverse linear operator from j to i.

    Returns:
        complex: Frequency-domain representation of signal i.
    """
    return T_ij * X_j

# Example usage:
# Generate some example signals (replace with your actual data)
N = 3  # Number of areas
signal_length = 1000
signals = [np.random.randn(signal_length) for _ in range(N)]
f = 10.0  # Frequency of interest

# Calculate the cross-spectral density matrix
S = calculate_cross_spectral_density(signals, f)

# Calculate coherence between areas 0 and 1
coherence_01 = calculate_coherence(S, 0, 1)
print(f"Coherence between areas 0 and 1 at frequency {f}: {coherence_01}")

# Example linear operator usage (replace with your actual T_ji and X_i values)
X_i = np.fft.fft(signals[0])[np.argmin(np.abs(np.fft.fftfreq(len(signals[0]), 1) - f))] # example X_i
T_ji = 0.8 + 0.5j #example operator
X_j = linear_operator(X_i, T_ji)
print(f"X_j using T_ji: {X_j}")

T_ij = 1/T_ji #example inverse operator.
X_i_inv = inverse_linear_operator(X_j, T_ij)
print(f"X_i using T_ij: {X_i_inv}")