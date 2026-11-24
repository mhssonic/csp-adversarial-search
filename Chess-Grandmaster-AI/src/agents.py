import datetime
import random

import chess

import utiles


class Agent:
    """
        Base class for agents.
    """

    def __init__(self, board: chess.Board, next_player) -> None:
        self.board = board
        self.next_player = next_player

    def get_action(self):
        """
            This method receives a GameState object and returns an action based on its strategy.
        """
        pass

    """
            get possible moves : 
                possibleMoves = board.legal_moves

            create a move object from possible move : 
                move = chess.Move.from_uci(str(possible_move))

            push the move : 
                board.push(move)

            pop the last move:
                board.pop(move)
    """


class RandomAgent(Agent):
    def __init__(self, board: chess.Board, next_player):
        super().__init__(board, next_player)

    def get_action(self):
        return self.random()

    def random(self):
        possible_moves_list = list(self.board.legal_moves)

        random_move = random.choice(possible_moves_list)
        return chess.Move.from_uci(str(random_move))


class MinimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        _, best_move = self.minimax(self.depth, self.board.turn, self.board.turn)
        return best_move

    def minimax(self, depth, turn, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), None

        optimal_score = float('-inf') if is_maximizing else float('inf')
        optimal_move = None
        for current_move in self.board.legal_moves:
            self.board.push(current_move)
            score, _ = self.minimax(depth - 1, not turn, not is_maximizing)
            self.board.pop()
            if (is_maximizing and score > optimal_score) or (not is_maximizing and score < optimal_score):
                optimal_score = score
                optimal_move = current_move
        return optimal_score, optimal_move


class AlphaBetaAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        _, best_move = self.alpha_beta(self.depth, self.board.turn, self.board.turn, -float('inf'), float('inf'))
        return best_move

    def alpha_beta(self, depth, turn, is_maximizing, alpha, beta):
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), None

        optimal_score = float('-inf') if is_maximizing else float('inf')
        optimal_move = None
        for current_move in self.board.legal_moves:
            self.board.push(current_move)
            score, _ = self.alpha_beta(depth - 1, not turn, not is_maximizing, alpha, beta)
            self.board.pop()
            if is_maximizing:
                if score > optimal_score:
                    optimal_score = score
                    optimal_move = current_move
                alpha = max(alpha, optimal_score)
                if beta <= alpha:
                    break
            else:
                if score < optimal_score:
                    optimal_score = score
                    optimal_move = current_move
                beta = min(beta, optimal_score)
                if beta <= alpha:
                    break
        return optimal_score, optimal_move


class ExpectimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        _, best_move = self.expectimax(self.depth, self.board.turn, self.board.turn)
        return best_move

    def expectimax(self, depth, turn, is_maximizing):
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), None

        if is_maximizing:
            highest_score = float('-inf')
            best_move = None
            for move in self.board.legal_moves:
                self.board.push(move)
                score, _ = self.expectimax(depth - 1, not turn, not is_maximizing)
                self.board.pop()
                if score > highest_score:
                    highest_score = score
                    best_move = move
        else:
            cumulative_score = 0
            move_count = 0
            for move in self.board.legal_moves:
                self.board.push(move)
                score, _ = self.expectimax(depth - 1, not turn, not is_maximizing)
                self.board.pop()
                cumulative_score += score
                move_count += 1
            highest_score = cumulative_score / max(move_count, 1)
            best_move = None

        return highest_score, best_move

def evaluate_board_state(board, turn):
    node_evaluation = 0
    node_evaluation += utiles.check_status(board, turn)
    node_evaluation += utiles.evaluationBoard(board)
    node_evaluation += utiles.checkmate_status(board, turn)
    node_evaluation += utiles.good_square_moves(board, turn)
    if turn == 'white':
        return node_evaluation
    return -node_evaluation
