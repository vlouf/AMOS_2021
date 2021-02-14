pixel_area = 2.5 ** 2
area = np.zeros(len(slices))
for idx, sl in enumerate(slices):
    area[idx] = pixel_area * np.sum(conv_0[sl] == 2)
    
plt.hist(area, range=[0, pixel_area * 100], bins=100)
plt.ylabel('Number of convective tower')
plt.xlabel('Area $(km^2)$')
plt.show()