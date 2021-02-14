total_mean_rain = np.nanmean(midnight_rain)
conv_mean_rain = np.nanmean(midnight_rain[midnight_class == 2])
strat_mean_rain = np.nanmean(midnight_rain[midnight_class == 1])

print(f'''- 1) Total average rainfall rate = {total_mean_rain:0.3} mm/h,
- 2) Mean convective rainfall rate = {conv_mean_rain:0.3} mm/h, 
- 3) Mean stratiform rainfall rate = {strat_mean_rain:0.3} mm/h. \U0001F389''')