def is_bisiesto( num ):
	return ( num % 100 == 0 and num % 400 ) or ( num % 4 == 0 )

res = []
while 1:
	try:
		year = int( raw_input() )
	except EOFError:
		break
	else:
		res.append( "S" if is_bisiesto( year ) else "N" ) 
print "\n".join( res )
