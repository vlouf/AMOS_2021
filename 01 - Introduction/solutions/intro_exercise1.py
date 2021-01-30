step = 110
datetime = pd.Timestamp(dset.time[step].to_pandas())

fig = plt.figure(figsize=(12, 10))
ax1 = plt.subplot(1, 1, 1, projection=projection)
ax1.coastlines('10m')
im = ax1.pcolormesh(x, y, (10 ** (refl[step, :, :] / 10) / 200) ** (1 / 1.6), vmin=0, cmap='Blues')

# Plotting the range rings.
theta = np.linspace(0, 2 * np.pi)
for r in [50e3, 100e3, 150e3]:
    ax1.plot(r * np.cos(theta), r * np.sin(theta), 'k', linewidth=1, alpha=0.75)

plt.colorbar(im, ax=ax1, label='Rainfall rate (mm/h)')
plt.title(f'CPOL - {datetime.isoformat()} UTC')
plt.show()