phone = {
	"1": "",
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz"
}


def returnOpt(digits):
	return reduce(lambda agg, digit: [x + y for x in agg for y in phone[digit]], digits, [''])

print returnOpt("23")
