def dfa_accept(w, start, accept_states, transitions):
    state = start
    for a in w:
        if (state, a) not in transitions:
            return False
        state = transitions[(state, a)]
    return state in accept_states
start = "c0"
accept = {"c2"}

transitions = {
    ("c0", "a"): "q1",
    ("c1", "b"): "q2"
}


tests = ["ab", "aab", "abb", "aa", ""]

for t in tests:
    print(t, "=>", dfa_accept(t, start, accept, transitions))
