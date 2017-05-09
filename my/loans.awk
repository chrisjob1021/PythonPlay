{
if ( $2 == "transport" ) transport += $3;
else if ( $2 == "business" ) business += $3;
else if ( $2 == "special_occasion" ) special_occasion += $3;
else if ( $2 == "other" ) other += $3;
}
END {
print "transport,"transport
print "business,"business
print "special_occasion,"special_occasion
print "other,"other
}
