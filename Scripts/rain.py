def run():
    import csv
    import plotly.graph_objects as go

    precip = []
    for i in range(1, 12):
        current = []
        with open(f'data/Eminence{i}.csv') as f:
            reader = csv.DictReader(f)

            for j in reader:
                current.append(j['precip'])
            precip.append(current)

    fig = go.Figure(data=
        go.Contour(
            z=precip,
            contours=dict(
                showlabels=True,
                labelfont=dict(
                    size=12,
                    color='purple',
                )
            ),
            colorscale='Blues',
            colorbar=dict(
                title='Millimeters (mm)', # title here
                titleside='right',
                titlefont=dict(
                    size=14,
                    family='Arial, sans-serif')
            ),
            x=[1, 2, 3, 4, 5],
            y=[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        ),
        layout=dict(title='Eminence, Indiana Precipitation', xaxis=dict(title='July 21 - 25', dtick=1), yaxis=dict(title='2011 - 2021', dtick=1))
    )
    print(precip)
    fig.show()

