from output import *


def play_game_one():
    template = read_template('../assets/dark_and_stormy_night_template.txt')
    string, descriptions = parse_template(template)
    users_selection = get_user_selection(descriptions)
    user_madlib = merge(string, users_selection)
    open_and_write('../assets/dark_and_stormy_night_output.txt', user_madlib)
    print(read_template('../assets/dark_and_stormy_night_output.txt'))

    # print(string)
    # print(descriptions)


def play_game_two():
    template = read_template('../assets/make_me_a_video_game_template.txt')
    string, descriptions = parse_template(template)
    users_selection = get_user_selection(descriptions)
    user_madlib = merge(string, users_selection)
    open_and_write('../assets/make_me_a_video_game_output.txt', user_madlib)
    print(read_template('../assets/make_me_a_video_game_output.txt'))

    # print(string)
    # print(descriptions)


def play_game_three():
    template = read_template('../assets/dark_and_stormy_night_template_b.txt')
    string, descriptions = parse_template(template)
    users_selection = get_user_selection(descriptions)
    user_madlib = merge(string, users_selection)
    open_and_write('../assets/make_me_a_video_game_output_b.txt', user_madlib)
    print(read_template('../assets/make_me_a_video_game_output_b.txt'))

    # print(string)
    # print(descriptions)

