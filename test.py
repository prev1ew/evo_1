def direction(facing, turn):
    step = 45

    facings = {
        0:'N',
        1:'NE',
        2:'E',
        3:'SE',
        4:'S',
        5:'SW',
        6:'W',
        7:'NW',
    }

    facing_upper = facing.upper()

    if facing_upper not in facings.values():
        return f'Incorrect value: {facing}'

    try:
        turn = int(turn)
    except ValueError:
        return f'Incorrect value: {turn}'

    for k, v in facings.items():
        if v == facing_upper:
            curr_position = k
            break

    steps = ((turn / step) + curr_position) % 8

    # если число целое то возврат одного значения, иначе "гдето между 1 и 2 "
    if steps == int(steps):
        return facings[0 if steps == 8 else steps]
    else:
        steps = int(steps)
        first_element = 0 if steps == 8 else steps
        second_element = 0 if first_element == 7 else first_element + 1
        return f'Between {facings[first_element]} and {facings[second_element]}'
