[![Lichess rapid rating](https://lichess-shield.vercel.app/api?username=Ofish&format=rapid)](https://lichess.org/@/Ofish/perf/rapid)
[![Lichess blitz rating](https://lichess-shield.vercel.app/api?username=Ofish&format=blitz)](https://lichess.org/@/Ofish/perf/blitz)
[![Lichess bullet rating](https://lichess-shield.vercel.app/api?username=Ofish&format=bullet)](https://lichess.org/@/Ofish/perf/bullet)
# Ofish-uci-fast
Play against Ofish at <a href="https://lichess.org/@/ofish">lichess.org</a>!
# Current features
- Negamax search with alphabeta pruning
- Basic evaluation (piece values for middlegame and endgame)
- Piece square tables (borrowed from PeSTO's evaluation function for middlegame and endgame)
- Iterative deepening
- Quiscence search limited to depth 2, because it is too slow even at depth 3.. Blame python!
- Simple time management mechanism
- Communicates in UCI
