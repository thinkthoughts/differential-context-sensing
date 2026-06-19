import numpy as np


def simulate_common_mode_pair(n=1000, signal_amp=0.2, common_noise_amp=1.0, shot_noise_amp=0.05, seed=7):
    """Return two noisy sensor traces and their differential readout."""
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 10, n)
    signal = signal_amp * np.sin(2 * np.pi * 0.35 * t)
    common = common_noise_amp * rng.normal(size=n)
    shot_a = shot_noise_amp * rng.normal(size=n)
    shot_b = shot_noise_amp * rng.normal(size=n)

    # Opposite-sign physical signal makes the differential channel informative.
    sensor_a = signal + common + shot_a
    sensor_b = -signal + common + shot_b
    differential = sensor_a - sensor_b
    common_estimate = 0.5 * (sensor_a + sensor_b)
    return t, signal, common, sensor_a, sensor_b, differential, common_estimate


def rms(x):
    x = np.asarray(x)
    return float(np.sqrt(np.mean(x**2)))
