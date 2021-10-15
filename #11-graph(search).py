from collections import deque

def search(start_node, target):
    search_queue = deque()
    search_queue += graph[start_node]
    # print(search_queue)
    searched = set()
    # print(searched)

    while search_queue:
        print(search_queue)
        person = search_queue.popleft()
        print(person)
        print(searched)
        print()
        if person not in searched:
            if person == target:
                return f'{target.upper()} found'
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


graph = {
    'me': ['faz', 'feruz', 'ozodbek'],
    'ozodbek': ['muslim', 'amir'],
    'feruz': ['nizom', 'jonik'],
    'faz': ['ozod', 'shoxrux'],
    'nizom': [],
    'jonik': ['muslim'],
    'muslim': [],
    'amir': [],
    'ozod': [],
    'shoxrux': []
    }
print(search('me', 'ozod'))