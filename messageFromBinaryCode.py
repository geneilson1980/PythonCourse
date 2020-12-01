def messageFromBinaryCode(code):
    expectedOutput = ''
    brokenCode = []
    tempNumber = ''
    count = 0
    for i in range(len(code)):
        tempNumber += code[i]
        count += 1
        if count == 8:
            brokenCode.append(tempNumber)
            tempNumber = ''
            i = count -1
            count = 0
    return expectedOutput



code = "010010000110010101101100011011000110111100100001"
result = messageFromBinaryCode(code)
print(result)

DEC		BIN				Symbol		
32	“	100000	“	:	“	 	“	,
33	“	100001	“	:	“	!	“	,
34	“	100010	“	:	'	"	'	,
35	“	100011	“	:	“	#	“	,
36	“	100100	“	:	“	$	“	,
37	“	100101	“	:	“	%	“	,
38	“	100110	“	:	“	&	“	,
39	“	100111	“	:	“	'	“	,
40	“	101000	“	:	“	(	“	,
41	“	101001	“	:	“	)	“	,
42	“	101010	“	:	“	*	“	,
43	“	101011	“	:	“	+	“	,
44	“	101100	“	:	“	,	“	,
45	“	101101	“	:	“	-	“	,
46	“	101110	“	:	“	.	“	,
47	“	101111	“	:	“	/	“	,
48	“	110000	“	:		0		,
49	“	110001	“	:		1		,
50	“	110010	“	:		2		,
51	“	110011	“	:		3		,
52	“	110100	“	:		4		,
53	“	110101	“	:		5		,
54	“	110110	“	:		6		,
55	“	110111	“	:		7		,
56	“	111000	“	:		8		,
57	“	111001	“	:		9		,
58	“	111010	“	:	“	:	“	,
59	“	111011	“	:	“	;	“	,
60	“	111100	“	:	“	<	“	,
61	“	111101	“	:	“	=	“	,
62	“	111110	“	:	“	>	“	,
63	“	111111	“	:	“	?	“	,
64	“	1000000	“	:	“	@	“	,
65	“	1000001	“	:	“	A	“	,
66	“	1000010	“	:	“	B	“	,
67	“	1000011	“	:	“	C	“	,
68	“	1000100	“	:	“	D	“	,
69	“	1000101	“	:	“	E	“	,
70	“	1000110	“	:	“	F	“	,
71	“	1000111	“	:	“	G	“	,
72	“	1001000	“	:	“	H	“	,
73	“	1001001	“	:	“	I	“	,
74	“	1001010	“	:	“	J	“	,
75	“	1001011	“	:	“	K	“	,
76	“	1001100	“	:	“	L	“	,
77	“	1001101	“	:	“	M	“	,
78	“	1001110	“	:	“	N	“	,
79	“	1001111	“	:	“	O	“	,
80	“	1010000	“	:	“	P	“	,
81	“	1010001	“	:	“	Q	“	,
82	“	1010010	“	:	“	R	“	,
83	“	1010011	“	:	“	S	“	,
84	“	1010100	“	:	“	T	“	,
85	“	1010101	“	:	“	U	“	,
86	“	1010110	“	:	“	V	“	,
87	“	1010111	“	:	“	W	“	,
88	“	1011000	“	:	“	X	“	,
89	“	1011001	“	:	“	Y	“	,
90	“	1011010	“	:	“	Z	“	,
91	“	1011011	“	:	“	[	“	,
92	“	1011100	“	:	“	\	“	,
93	“	1011101	“	:	“	]	“	,
94	“	1011110	“	:	“	^	“	,
95	“	1011111	“	:	“	_	“	,
96	“	1100000	“	:	“	`	“	,
97	“	1100001	“	:	“	a	“	,
98	“	1100010	“	:	“	b	“	,
99	“	1100011	“	:	“	c	“	,
100	“	1100100	“	:	“	d	“	,
101	“	1100101	“	:	“	e	“	,
102	“	1100110	“	:	“	f	“	,
103	“	1100111	“	:	“	g	“	,
104	“	1101000	“	:	“	h	“	,
105	“	1101001	“	:	“	i	“	,
106	“	1101010	“	:	“	j	“	,
107	“	1101011	“	:	“	k	“	,
108	“	1101100	“	:	“	l	“	,
109	“	1101101	“	:	“	m	“	,
110	“	1101110	“	:	“	n	“	,
111	“	1101111	“	:	“	o	“	,
112	“	1110000	“	:	“	p	“	,
113	“	1110001	“	:	“	q	“	,
114	“	1110010	“	:	“	r	“	,
115	“	1110011	“	:	“	s	“	,
116	“	1110100	“	:	“	t	“	,
117	“	1110101	“	:	“	u	“	,
118	“	1110110	“	:	“	v	“	,
119	“	1110111	“	:	“	w	“	,
120	“	1111000	“	:	“	x	“	,
121	“	1111001	“	:	“	y	“	,
122	“	1111010	“	:	“	z	“	,
123	“	1111011	“	:	“	{	“	,
124	“	1111100	“	:	“	|	“	,
125	“	1111101	“	:	“	}	“	,
126	“	1111110	“	:	“	~	“	,
127	“	1111111	“	:	“		“	
