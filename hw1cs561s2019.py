import copy
import sys
import operator


class State:
    def __init__(self, n, board):
        self.n=n
        self.board = board
        self.points = 0
        self.draw_beans()  # initial the board with beans drawn
        self.evalfnc()

    def copy(self):
        new_state = State(self.n, copy.deepcopy(self.board))

        return new_state

    def generate_output(self, move):
        with open("output.txt", "w") as outputfile:
            outputfile.write(str(move[0])+ " "+ str(move[1]))


    def printBoard(self):
        print '\n'.join(''.join(str(g) + "\t" for g in horizontal) for horizontal in self.board)

    def evalfnc(self):
        #a player's points is the number of squares covered(look at walls, blocks)
        #caution: add the emitter(which is either 4 or 5) to the points

        for k in range(self.n):
            for j in range(self.n):
                #print "board"
                #print board
                #print "self.board"
                #print self.board

                if self.board[k][j] == 4 or self.board[k][j]==1 or self.board[k][j]==9:
                    self.points += 1
        return self.points

    def makeNextState(self, move):
        newState = self.copy()
        newState.board[move[0]][move[1]] = 1
        newState.draw_beans()
        newState.evalfnc()
        return newState

    def getValidMoves(self):
        moves=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]==0:
                    moves.append([i,j])
        #print "valid moves of len = " + str(len(moves)) + ":"
        #print moves
        return moves

    def draw_beans(self):
        rowindex = 0
        for row in self.board:
            colindex = 0
            for cell in row:
                if cell == 1:
                    #print "1 at: "
                    #print [rowindex, colindex]
                    self.give_bean_number(4, [rowindex, colindex], self.n)
                if cell == 2:
                    #print "2 at: "
                    #print [rowindex, colindex]
                    self.give_bean_number(5, [rowindex, colindex], self.n)
                colindex += 1
            rowindex += 1
        #self.printBoard()


    def give_bean_number(self, beanNumber, pos, n):
        rowindexx = pos[0]
        colindexx = pos[1]
        if beanNumber==4:
            otherBeanNumber = 5
        else:
            otherBeanNumber = 4
        for index in range(3):
            if rowindexx-index-1>=0: #up
                value = self.board[rowindexx-1-index][colindexx]
                if value==0: self.board[rowindexx-1-index][colindexx] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx-1-index][colindexx]=9
                else: break
            else: break
        for index in range(3):
            if rowindexx+index+1<=n-1: #down
                value  = self.board[rowindexx+1+index][colindexx]
                if value==0: self.board[rowindexx+1+index][colindexx] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx+1+index][colindexx]=9
                else: break
            else: break
        for index in range(3):
            if colindexx-index-1>=0: #left
                value = self.board[rowindexx][colindexx-1-index]
                if value==0: self.board[rowindexx][colindexx-1-index] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx][colindexx-1-index] = 9
                else: break
            else: break
        for index in range(3):
            if colindexx+index+1<=self.n-1:  # right
                value = self.board[rowindexx][colindexx+1+index]
                if value==0: self.board[rowindexx][colindexx+1+index] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx][colindexx+1+index]=9
                else: break
            else: break
        for index in range(3):
            if rowindexx-index-1>=0 and colindexx-index-1>=0: #up and left
                value = self.board[rowindexx-1-index][colindexx-index-1]
                if value==0: self.board[rowindexx-1-index][colindexx-index-1] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx-1-index][colindexx-index-1]=9
                else: break
            else: break
        for index in range(3):
            if rowindexx-index-1>=0 and colindexx+index+1<=self.n-1: #up and right
                value = self.board[rowindexx-1-index][colindexx+index+1]
                if value==0: self.board[rowindexx-1-index][colindexx+index+1] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx-1-index][colindexx+index+1]=9
                else: break
            else: break
        for index in range(3):
            if rowindexx+index+1<=self.n-1 and colindexx-index-1>=0: #down and left
                value = self.board[rowindexx+1+index][colindexx-index-1]
                if value==0: self.board[rowindexx+1+index][colindexx-index-1] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx+1+index][colindexx-index-1]=9
                else: break
            else: break
        for index in range(3):
            if rowindexx+index+1<=self.n-1 and colindexx+index+1<=self.n-1: #down and right
                value = self.board[rowindexx+1+index][colindexx+index+1]
                if value==0: self.board[rowindexx+1+index][colindexx+index+1] = beanNumber
                elif value==beanNumber or value==9: continue
                elif value==otherBeanNumber: self.board[rowindexx+1+index][colindexx+index+1]=9
                else: break
            else: break



class MyAgent:
    def __init__(self, depth):
        self.depth = depth
        self.smallestInt = -sys.maxint
        self.largestInt = sys.maxint

    def getmax_move(self, state):
        max_move, value = self.maxVal(self.smallestInt, self.largestInt, 0, state)
        return max_move

    def getevalfnc(self, state, move, newpoints):
        return newpoints


    def getPartialpoints(self, state, move):
        old_points = state.points
        ss = state.copy()
        ss.board[move[0]][move[1]] = 1
        ss.draw_beans()
        new_points = ss.evalfnc()
        partial_points = new_points - old_points
        return partial_points  # going



    def maxVal(self, alpha, beta, d, state):
        points = state.points
        v = self.smallestInt
        bestResult = None
        if d == self.depth:
            return bestResult, points
        else:
            moves = []
            allMoves = state.getValidMoves()
            for move in allMoves:
                partial_points = self.getPartialpoints(state, move)
                moves.append((move, self.getevalfnc(state, move, state.points + partial_points)))
            moves.sort(key = operator.itemgetter(1), reverse=True)
            #print "maxmoves"
            #print moves
            for move in moves:
                theNextState = state.makeNextState(move[0])
                x, compete = self.minVal(theNextState, alpha, beta, d+1)
                if not v >= compete:
                    bestResult = move[0]
                    v = compete
                if not v < beta:
                    return bestResult, v
                alpha = max(alpha, v)
            return bestResult, v

    def minVal(self, state, alpha, beta, d):
        bestResult = None

        v = self.largestInt


        if d == self.depth:
            #this is the cutoff
            return bestResult, state.evalfnc()
        else:
            allMoves = state.getValidMoves()
            #print "MINallMoves", allMoves
            moves = []

            for move in allMoves:
                partial_points = self.getPartialpoints(state, move)
                moves.append((move, self.getevalfnc(state, move, state.points - partial_points)))
            moves.sort(key = operator.itemgetter(1))
            #print "MINmoves"
            #print moves

            for move in moves:
                theNextState = state.makeNextState(move[0])
                x, compete = self.maxVal(alpha, beta, d+1, theNextState)
                if not v <= compete:
                    bestResult = move[0]
                    v = compete
                if not v > alpha:
                    return bestResult, v
                beta = min(beta, v)
            return bestResult, v










if __name__=='__main__':

    with open("input.txt", "r") as inputfile:
        inputdata = inputfile.readlines()

    n = int(inputdata[0])
    board = []
    for i in range(n):
        line = inputdata[1+i].strip()
        row = []
        for x in line:
            row.append(int(x))
        board.append(row)
    #print "board: "
    #print board

    s = State(n, board)
    agent = MyAgent(3)
    #s.getValidMoves()
    bestResult = agent.getmax_move(s)
    #print "bestResult is: "+str(bestResult)
    s.makeNextState(bestResult).generate_output(bestResult)

