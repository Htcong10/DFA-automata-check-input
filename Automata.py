from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
def CreatDfa(_states, _alphabet, _tran, _state_start, _state_final,w):
       dfa = DFA(
          states=set(_states),
          input_symbols=_alphabet,
          transitions=_tran,
          final_states=set(_state_final),
          initial_state=_state_start
       )
       if dfa.accepts_input(w):
           print('accepted')
       else:
           print('rejected')
       dfa = VisualDFA(dfa)
       dfa.show_diagram(w)

