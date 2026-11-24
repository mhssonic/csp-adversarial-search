import copy
import random
import math


def is_consistent(graph: dict[int, set], variable_value_pairs: dict[int, int]):
    """
        returns True if the variables that have been assigned a value so far are consistent with the constraints, 
        and False otherwise.
        
        variable_value_pairs can be used to access any value of any variable from the variable as a key
        you can use variable_value_pairs.items() to traverse it as (state, color) pairs
                    variable_value_pairs.keys() to get all the variables,         
                and variable_value_pairs.values() to get all the values
    """
    for i, value in variable_value_pairs.items():
        if value is None:
            continue
        for node in graph[i]:
            neighbor = variable_value_pairs.get(node)
            if neighbor is not None and neighbor == value:
                return False
    return True


def is_solved(graph: dict[int, set], variable_value_pairs: dict[int, int]):
    """
        returns True if the CSP is solved, and False otherwise
    """
    for i, value in variable_value_pairs.items():
        if value is None:
            return False
        for node in graph[i]:
            if variable_value_pairs[node] is None or value == variable_value_pairs[node]:
                return False
    return True


def get_next_variable(variable_value_pairs, domains):
    """
        returns the index of the next variable from the default order of the unassinged variables
    """
    for i, value in variable_value_pairs.items():
        if value is None:
            return i


def get_chosen_variable(graph: dict[int, set], variable_value_pairs: dict[int, int], domains: list[int, list] or None):
    """
        returns the next variable that is deemed the best choice by the proper heuristic
        use a second heuristic for breaking ties from the first heuristic
    """
    if domains is None:
        removed_value = {}
        for i in variable_value_pairs.keys():
            removed_value[i] = set()
        for i, value in variable_value_pairs.items():
            if value is None:
                continue
            for node in graph[i]:
                if variable_value_pairs[node] is None:
                    removed_value[node].add(value)

        return max(removed_value, key=lambda x: len(removed_value[x]))

    return min(graph, key=lambda x: len(domains[x]) if variable_value_pairs[x] is None else math.inf)


def count_mutual_value(graph: dict[int, set], domains: list[int, list], variable: int, value: int):
    count = 0
    for node in graph[variable]:
        if value in domains[node]:
            count += 1
    return count


def get_ordered_domain(graph: dict[int, set], domains: list[int, list], variable: int):
    """
        returns the domain of the varibale after ordering its values by the proper heuristic
        (you may use imports here)
    """
    domains[variable].sort(key=lambda value: count_mutual_value(graph, domains, variable, value))
    return domains[variable]


def forward_check(graph: dict[int, set], variable_value_pairs: dict[int, int], domains: list[int, list], variable: int,
                  value: int):
    """
        removes the value assigned to the current variable from its neighbors
        returns True if backtracking is necessary, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    for neighbor in graph[variable]:
        if variable_value_pairs[neighbor] is None:
            if value in domains[neighbor]:
                domains[neighbor].remove(value)
            if len(domains[neighbor]) == 0:
                return True
    return False


def ac3(graph: dict[int, set], variable_value_pairs: dict[int, int], domains: list[int, list]) -> bool:
    """
        maintains arc-consistency
        returns True if backtracking is necessary, and False otherwise
    """
    queue = []
    for i, neighbor in graph.items():
        if variable_value_pairs[i] is not None:
            continue
        for value in neighbor:
            if variable_value_pairs[value] is None:
                queue.append((i, value))

    while len(queue) > 0:
        a, b = queue.pop(0)
        if remove_inconsistencies_values(graph, domains, a, b):
            if len(domains[a]):
                return True
            for neighbor in graph[a]:
                queue.append(neighbor, a)
    return False

def remove_inconsistencies_values(graph: dict[int, set], domains: list[int, list], a: int, b: int) -> bool:
    removed = False
    for value in domains[a]:
        for neighbor in graph[a]:
            if len(domains[neighbor]) == 1 and domains[neighbor] == value:
                domains[a].remove(value)
    return removed

def random_choose_conflicted_var(graph, variable_value_pairs):
    """
        returns a random variable that is conflicting with a constrtaint
    """
    conflicts = []
    for node, neighbors in graph.items():
        conflicts.extend([neighbor_node for neighbor_node in neighbors if
                          variable_value_pairs[neighbor_node] == variable_value_pairs[node]])

    if len(conflicts) == 0:
        return None
    return random.choice(conflicts)


def get_chosen_value(graph: dict[int, set], variable_value_pairs: dict[int, int], variable: int):
    """
        returns the value by using the proper heuristic
        NOTE: handle tie-breaking by random
    """
    value = variable_value_pairs[variable]
    possible_colors = list(set(range(4)).difference({value}))
    conflict_count = []
    for possible in possible_colors:
        simulated = copy.deepcopy(variable_value_pairs)
        simulated[variable] = possible
        conf_count = []
        for node, neighbors in graph.items():
            conf_count.extend([neighbor_node for neighbor_node in neighbors if
                              variable_value_pairs[neighbor_node] == variable_value_pairs[node]])
        conflict_count.append(conf_count)

    return possible_colors[conflict_count.index(min(conflict_count))]
