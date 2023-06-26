import random

Checkmate = 1000
Stalemate = 0

def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

def findBestMove(validMoves):
    maxScore = Checkmate
    for playerMove in validMoves:
        pass