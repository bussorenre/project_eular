
digit = 3
diff = 10 ** (digit*2) - 10 ** (digit*2-1) + 9

print("diff:", diff)

# このdiff の最大公約数？を２つ求める
for x in range(1,diff):
	if diff%x ==0:
		y = diff/x
		print("",x,":",y)


# わからん！！！