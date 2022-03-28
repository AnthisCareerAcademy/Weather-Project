def run():
    import plotly.express as px
    import pandas as pd
    import csv
    import numpy

    direction_starts, direction_ends = [float(d) for d in numpy.arange(11.25, 348.75, 22.50)], \
                                       [float(d) for d in numpy.arange(11.25, 371.25, 22.50)]
    direction_starts.insert(0, 348.75)
    compass_rose = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    initial, temp = [], []
    speed, direction, frequency = [], [], []

    for i in range(1, 12):
        with open(f'data/Eminence{i}.csv') as f:
            reader = csv.DictReader(f)

            for j in reader:
                speed.append(float(j['windspeed']))
                direction.append(float(j['winddir']))

    # Calculate the frequency of each speed based on the range it's in and append it to the frequency list
    for i in speed:
        if 4 <= i <= 7:
            frequency.append(0.09)
        elif 8 <= i <= 12:
            frequency.append(0.44)
        else:
            frequency.append(0.47)

    # Create an initial dictionary for speed, direction, and frequency
    for i, j, k in zip(speed, direction, frequency):
        initial.append({'speed': i, 'direction': j, 'frequency': k})

    # Sort initial from least to greatest by degrees
    for i in sorted(direction):
        for j in initial:
            if j['direction'] == i:
                temp.append(j)



    # Turn all the directions from degrees to cardinal
    for h, i in zip(sorted(direction), temp):
        for j, k, l in zip(direction_starts, direction_ends, compass_rose):
            if j <= h < k:
                i['direction'] = l


    # Sorting the speed from least to greatest based on each direction
    speed_sorting = []
    for i in compass_rose:
        for j in temp:
            if j['direction'] == i:
                speed_sorting.append(j['speed'])
        speed_sorting = sorted(speed_sorting)
        for k in temp:
            if k['direction'] == i:
                k['speed'] = speed_sorting.pop(0)
        speed_sorting = []


    # Converting speed to strength and sorting the frequency based on the frequency of strength
    for i in temp:
        if 4 <= i['speed'] < 8:
            i['speed'] = 2
            i['frequency'] = 0.09
        elif 8 <= i['speed'] < 13:
            i['speed'] = 3
            i['frequency'] = 0.44
        elif 13 <= i['speed'] < 19:
            i['speed'] = 4
            i['frequency'] = 0.47


    df = pd.DataFrame(data={'windspeed': [i['speed'] for i in temp], 'winddir': [i['direction'] for i in temp], 'frequency': [i['frequency'] for i in temp]})
    fig = px.bar_polar(df, r="frequency", theta="winddir",
                       color="windspeed", template="plotly_white",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)

    fig.update_layout(
        title='Wind Speed Distribution in Eminence, Indiana',
        font_size=16,
        legend_font_size=16,
        polar_angularaxis_rotation=90,

    )
    fig.show()
