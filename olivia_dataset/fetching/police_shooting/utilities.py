import requests


def get_county(x) -> str:
    try:
        url = 'https://geo.fcc.gov/api/census/area?lat=' + f"{x['latitude']}&lon={x['longitude']}" + '&format=json'
    except Exception as e:
        import pdb
        pdb.set_trace()

    params = dict(
        origin='Chicago,IL',
        destination='Los+Angeles,CA',
        waypoints='Joplin,MO|Oklahoma+City,OK',
        sensor='false'
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() # Check the JSON Response Conte
    try:
        output = data['results'][0]['county_name']

        if output.lower().endswith('city') or output.lower().endswith('county') or output.lower().endswith('parish'):
            return ' '.join(output.split(' ')[:-1])
        else:
            return output
    except:
        return 'N/A'
