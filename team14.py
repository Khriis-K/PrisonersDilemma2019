import random 

team_name = 'Copycat'
team_strategy =  'copycat, betray first'
strategy_description = "Its hard to suceed in this world... so why not copy people who have already become successful?"
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    if len(my_history) == 0:
      return 'b'
    else:
      if their_history[len(their_history)-1] == 'b':
        return 'b'
      else:
        return 'c'




    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='bbb',
              their_history='bbc', 
              my_score=-400,
              their_score=-1000,
              result='b'):
         print 'Turn 1 test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    if test_move(my_history='bcc',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=100, 
              their_score=-500,
              result='c'):       
      print '4 moves in test passed.'



# copy cat
# always betray first
