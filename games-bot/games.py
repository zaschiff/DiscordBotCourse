import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

player1 = ""
player2 = ""
turn = ""
game_over = True
empty_square = ":white_large_square:"
board = []
winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], 
    [6, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8], 
    [2, 4, 6],
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global game_over

    if game_over:
        global board
        board = [empty_square, empty_square, empty_square, 
            empty_square, empty_square, empty_square, 
            empty_square, empty_square, empty_square]
        turn = ""
        game_over = False
        count = 0
        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        
        # determine who goes first
        num =  random.randint(1, 2)

        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif  num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is in progress. Finish it before starting a new one")

@bot.commands()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global game_over

    if not game_over:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == empty_square:
                board[pos - 1] = mark
                count += 1

                # print baord again
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winning_conditions, mark)

                if game_over:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    game_over = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose the right spot (integer between 1 and 9) and the tiel must be unmarked")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the tictactoe command.")


def checkWinner(winning_conditions, mark):
    global game_over
    for condition in winning_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            game_over = True


bot.run('')