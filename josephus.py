"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


def find_survivor(num_people, kill_every):

    people = set()
    for i in range(1, num_people+1):
        people.add(i)
    to_die = kill_every
    while len(people) > 1:
        if to_die in people:
            people.remove(to_die)
        next_up = to_die + kill_every
        if next_up > num_people:
            to_die = next_up%(num_people+1) + 1
    survivor = people.pop()
    return survivor


def find_survivor(num_people, kill_every):
    dead = set()
    to_die = kill_every
    while len(dead) < num_people-1:
        dead.add(to_die)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
