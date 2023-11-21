P='uciok'
O='id author Chess123easy'
N='id name Ofish1'
I='inf'
H=max
D='-inf'
F=print
E=float
C=len
import chess,chess.svg,time as M
L={chess.PAWN:82,chess.KNIGHT:337,chess.BISHOP:365,chess.ROOK:477,chess.QUEEN:1025,chess.KING:0}
Q=[0,0,0,0,0,0,0,0,98,134,61,95,68,126,34,-11,-6,7,26,31,65,56,25,-20,-14,13,6,21,23,12,17,-23,-27,-2,-5,12,17,6,10,-25,-26,-4,-4,-10,3,3,33,-12,-35,-1,-20,-23,-15,24,38,-22,0,0,0,0,0,0,0,0]
R=[-167,-89,-34,-49,61,-97,-15,-107,-73,-41,72,36,23,62,7,-17,-47,60,37,65,84,129,73,44,-9,17,19,53,37,69,18,22,-13,4,16,13,28,19,21,-8,-23,-9,12,10,19,17,25,-16,-29,-53,-12,-3,-1,18,-14,-19,-105,-21,-58,-33,-17,-28,-19,-23]
S=[-14,-21,-11,-8,-7,-9,-17,-24,-8,-4,7,-12,-3,-13,-4,-14,2,-8,0,-1,-2,6,0,4,-3,9,12,9,14,10,3,2,-6,3,13,19,7,10,-3,-9,-12,-3,8,10,13,3,-7,-15,-14,-18,-7,-1,4,-9,-15,-27,-23,-9,-23,-5,-9,-16,-5,-17]
T=[32,42,32,51,63,9,31,43,27,32,58,62,80,67,26,44,-5,19,26,36,17,45,61,16,-24,-11,7,26,24,35,-8,-20,-36,-26,-12,-1,9,-7,6,-23,-45,-25,-16,-17,3,0,-5,-33,-44,-16,-20,-9,-1,11,-6,-71,-19,-13,1,17,16,7,-37,-26]
U=[-28,0,29,12,59,44,43,45,-24,-39,-5,1,-16,57,28,54,-13,-17,7,8,29,56,47,57,-27,-27,-16,-16,-1,17,-2,1,-9,-26,-9,-10,-2,-4,3,-3,-14,2,-11,-2,-5,2,14,5,-35,-8,11,2,8,15,-3,1,-1,-18,-9,10,-15,-25,-31,-50]
V=[-65,23,16,-15,-56,-34,2,13,29,-1,-20,-7,-8,-4,-38,-29,-9,24,2,-16,-20,6,22,-22,-17,-20,-12,-27,-30,-25,-14,-36,-49,-1,-27,-39,-46,-44,-33,-51,-14,-14,-22,-46,-44,-30,-15,-27,1,7,-8,-64,-43,-16,9,8,-15,36,12,-54,8,-28,24,14]
W=[-74,-35,-18,-18,-11,15,4,-17,-12,17,14,17,17,38,23,11,10,17,23,15,20,45,44,13,-8,22,24,27,26,33,26,3,-18,-4,21,24,27,23,9,-11,-19,-3,11,21,23,16,7,-9,-27,-11,4,13,14,4,-5,-17,-53,-34,-21,-11,-28,-14,-24,-43]
def G(board):
	A=board;B=0
	if A.is_checkmate():
		if A.turn==chess.WHITE:return E(D)
		else:return E(I)
	if A.can_claim_draw()or A.is_stalemate()or A.is_insufficient_material():return 0
	for F in chess.SQUARES:
		C=A.piece_at(F)
		if C is not None:
			G=1 if C.color==chess.WHITE else-1;B+=G*(L[C.piece_type]+X(C.piece_type,F,A))
			if C.piece_type in[chess.ROOK,chess.QUEEN]:
				H=chess.BB_FILES[chess.square_file(F)]
				if not H&A.occupied_co[chess.WHITE]|A.occupied_co[chess.BLACK]:B+=G*10
	if A.is_check():
		if A.turn==chess.WHITE:B-=60
		else:B+=60
	return B
def X(piece_type,square,board):
	B=piece_type;A=square
	if B==chess.PAWN:return Q[A]
	elif B==chess.KNIGHT:return R[A]
	elif B==chess.BISHOP:return S[A]
	elif B==chess.ROOK:return T[A]
	elif B==chess.QUEEN:return U[A]
	elif B==chess.KING:
		if C(board.piece_map())<=10:return W[A]
		else:return V[A]
	return 0
def J(board,alpha,beta,color,depth):
	H=depth;D=color;C=beta;B=alpha;A=board
	if H==0:return D*G(A)
	E=D*G(A)
	if E>=C:return C
	if B<E:B=E
	for I in A.legal_moves:
		if A.is_capture(I):
			A.push(I);F=-J(A,-C,-B,-D,H-1);A.pop()
			if F>=C:return C
			if F>B:B=F
	return B
def K(board,depth,alpha,beta,color):
	L=depth;F=color;C=beta;B=alpha;A=board
	if L==0 or A.is_game_over():
		if A.is_capture(A.peek()):return J(A,B,C,F,2)
		else:return F*G(A)
	I=E(D)
	for N in A.legal_moves:
		A.push(N);M=-K(A,L-1,-C,-B,-F);A.pop();I=H(I,M);B=H(B,M)
		if B>=C:break
	return I
def Y(board,depth):
	A=board
	for B in A.legal_moves:
		A.push(B)
		if A.is_checkmate():A.pop();return B
		A.pop()
	G=None;J=E(D);C=E(D);M=E(I)
	if A.turn==chess.WHITE:L=1
	else:L=-1
	for B in A.legal_moves:
		A.push(B);F=-K(A,depth-1,-M,-C,-L);A.pop()
		if F>J:J=F;G=B
		C=H(C,F)
	return G
def Z(board,remaining_time):
	B=board;A=remaining_time
	if B.fullmove_number<15:return A/60
	elif B.fullmove_number<30:return A/40
	else:return A/50
def a(board):return 3
def B():F(N);F(O);F(P)
def A():
	T='moves';G=chess.Board();Q=False;J=1000000;K=1000000;R=1000000
	while True:
		H=input()
		if H=='uci':F(N);F(O);F(P);Q=True
		elif H=='isready':F('readyok')
		elif H.startswith('position'):
			D=H.split()
			if C(D)<2:continue
			S=D[1]
			if S=='startpos':
				G.set_fen(chess.STARTING_FEN)
				if C(D)>2 and D[2]==T:
					for L in D[3:]:G.push_uci(L)
			elif S=='fen':
				if C(D)<8:continue
				U=' '.join(D[2:8]);G.set_fen(U)
				if C(D)>8 and D[8]==T:
					for L in D[9:]:G.push_uci(L)
			d=G.fen()
		elif H.startswith('go'):
			if not Q:continue
			A=H.split()[1:];V=0;W=0
			for B in range(C(A)):
				if A[B]=='depth'and B+1<C(A):W=int(A[B+1])
				elif A[B]=='movetime'and B+1<C(A):V=E(A[B+1])
				elif A[B]=='wtime'and B+1<C(A):J=E(A[B+1])
				elif A[B]=='btime'and B+1<C(A):K=E(A[B+1])
			R=J/1000 if G.turn==chess.WHITE else K/1000;X=M.time();I=1
			while I<=a(G):
				b=Y(G,I);c=M.time()-X
				if c>Z(G,R):break
				F(f"info depth {I} wtime {J} btime {K}");I+=1
			F('bestmove',b.uci())
		elif H=='quit':break
if __name__=='__main__':A()