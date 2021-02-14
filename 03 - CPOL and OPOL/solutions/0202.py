pixel_area = 2.5 ** 2
cloud_area = pixel_area * ((midnight_class == 1) | (midnight_class == 2)).sum()
conv_area = pixel_area * (midnight_class == 2).sum()
domain_area = pixel_area * np.sum(~np.isnan(midnight_class))
caf = conv_area / domain_area

print(f'''1) The total area of clouds = {cloud_area} km2,
2) the total area occupied by convective clouds = {conv_area} km2,
3) the convective area fraction = {100 * caf:0.3} %.''')