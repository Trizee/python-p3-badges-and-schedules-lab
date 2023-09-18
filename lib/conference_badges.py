def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    l = []
    for name in names:
        l.append(f'Hello, my name is {name}.')
    return l

def assign_rooms(names):
    
    l = []
    for name in names:
        l.append(f'Hello, {name}! You\'ll be assigned to room {names.index(name) + 1}!')
    return l

    

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)


printer(['1','2','3','4'])