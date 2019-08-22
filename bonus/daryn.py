with open('Phone.txt','r') as f:
    data = f.read().split('\n')[:-1]
    
time_zone = ['UTC-10', 'UTC-9', 'P', 'M/P', 'MP', 'M', 'C/M', 'CM', 'C', 'E/C', 'EC', 'E', 'A']    
west = ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming']
midwest = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin']
south = ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington D.C.', 'West Virginia']
northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania', 'Rhode Island', 'Vermont']
all_states = west + midwest + south + northeast + ['Puerto Rico']
all_states.sort()

def by_state(states):
    parsed_data = []
    if isinstance(states, str):
        for d in data:
            # phone = d.split('@')[0]
            state = d.split('@')[1].split('=')[0]
            # timezone = d.split('=')[1]
            if state.lower() == states.lower():
                parsed_data.append(d)
    else:
        for d in data:
            # phone = d.split('@')[0]
            state = d.split('@')[1].split('=')[0]
            # timezone = d.split('=')[1]
            if state.lower() in [x.lower() for x in states]:
                parsed_data.append(d)

    return parsed_data

def count_by_state(state):
    parsed_data = []
    for d in data:
        st = d.split('@')[1].split('=')[0]
        if st.lower() in state.lower():
            parsed_data.append(d)
    return len(parsed_data)

def count_by_region(region):
   pass

def tz_convert(tz):
    pass  
    
def by_tz(timezone):
    parsed_data = []
    
    switch = {
        'hawaii': 'UTC-10',
        'hst': 'UTC-10',
        'alaska': 'UTC-9',
        'ads': 'UTC-9',
        'pacific': ['P','M/P','MP'],
        'pst': ['P','M/P','MP'],
        'mountian': ['M/P', 'MP', 'M', 'C/M', 'CM'],
        'mst': ['M/P', 'MP', 'M', 'C/M', 'CM'],
        'central': ['C/M', 'CM', 'C', 'E/C', 'EC'],
        'cst': ['C/M', 'CM', 'C', 'E/C', 'EC'],
        'east': ['E/C', 'EC', 'E'],
        'est': ['E/C', 'EC', 'E'],
        'atlantic': 'A',
        'ast': 'A'
    }
    
    if isinstance(switch.get(timezone), str):
        for d in data:
            tz = d.split('=')[1]
            if tz.lower() == switch.get(timezone).lower():
                parsed_data.append(d)
    else:
        for d in data:
            tz = d.split('=')[1]
            if tz.lower() in [x.lower() for x in switch.get(timezone)]:
                parsed_data.append(d)

    return parsed_data

def num_amt_by_state():
    num = []
    for d in range(len(all_states)):
        num.append(count_by_state(all_states[d]),all_states[d])
    
with open('d.txt','w') as f:
    f.write('\n'.join(by_state('iowa')))