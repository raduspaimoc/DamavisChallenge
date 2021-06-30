# Simulates snake actions
path_options = {'L': [0, -1], 'R': [0, 1], 'D': [1, 0], 'U': [-1, 0]}


def is_valid_pos(board, pos):
    return 0 <= pos[0] < board[0] \
           and 0 <= pos[1] < board[1]


def find_paths(board, snake, depth):

    head = snake[0]
    visited = snake.copy()

    paths = 0
    if 0 < depth < 20:
        for k, v in path_options.items():
            next_pos = [head[0] + v[1], head[1] + v[0]]
            less = visited.copy()
            less.pop()
            if is_valid_pos(board, next_pos) and next_pos not in less:
                less.insert(0, next_pos)
                paths += find_paths(board, less, depth - 1)
    else:
        paths = 1

    return paths


if __name__ == '__main__':

    # Input Test 1
    board = [4, 3]  # num of rows, num of columns
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]  # pos 0 head, pos len - 1 tail
    depth = 3  # 1 <= depth < 20
    print("Test 1")
    print("Result: ", find_paths(board, snake, depth))

    # Input Test 2
    board = [2, 3]  # num of rows, num of columns
    snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]  # pos 0 head, pos len - 1 tail
    depth = 10  # 1 <= depth < 20
    print("Test 2")
    print("Result: ", find_paths(board, snake, depth))

    # Input Test 2
    board = [10, 10]  # num of rows, num of columns
    snake = [[5, 5], [5, 4], [4, 4], [4, 5]]  # pos 0 head, pos len - 1 tail
    depth = 4  # 1 <= depth < 20
    print("Test 3")
    print("Result: ", find_paths(board, snake, depth))
